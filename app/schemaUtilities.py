import re
import os
from os import listdir
from os.path import isfile, join, dirname
from app import app, schemaLayout, SCHEMA_LAYOUTS
from app.SCHEMA_LAYOUTS import *
from werkzeug import secure_filename

SCHEMA_EXTENSIONS = ['xsd']


def schema_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in SCHEMA_EXTENSIONS


def get_schema_list():
    schemas = []
    for f in listdir(app.config['SCHEMA_FOLDER']):
        if isfile(join(app.config['SCHEMA_FOLDER'], f)) and f.endswith('.xsd'):
            fname = re.sub('.xsd', '', str(f))
            schemas.append({'name': fname})
    return schemas


def add_schema(file, schema_name):
    print("add_schema")
    error = ''
    xsd = app.config['SCHEMA_FOLDER'] + '/' + schema_name + '.xsd'
    if schema_allowed(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.isfile(app.config['SCHEMA_FOLDER'] + '/' + schema_name + '.xsd'):
            file.save(os.path.join(app.config['SCHEMA_FOLDER'], filename))
            os.rename(app.config['SCHEMA_FOLDER'] + '/' + filename, xsd)
            schema_configured = schemaLayout.configure_xsd(xsd)
            if schema_configured:
                layout_created = schemaLayout.create_schema_layout(xsd, schema_name.replace('.', '-'))
                if not layout_created:
                    error += "There was an issue with configuring the schema"
            else:
                error += "there was an issue configuring the schema"
        else:
            error += "A schema with name '%s' already exists." % schema_name
    else:
        error += "File uploaded must be a valid schema with file extension of .xsd."

    return error


def delete_schema(filename):
    print("delete_schema")
    error = ''
    if os.path.isfile(app.config['SCHEMA_FOLDER'] + '/' + filename + '.xsd'):
        os.remove(app.config['SCHEMA_FOLDER'] + '/' + filename + '.xsd')
    else:
        error += 'Unable to find the selected schema, please refresh and try again'

    if os.path.isfile(app.config['SCHEMA_LAYOUTS_FOLDER'] + '/' + filename.replace('.', '-') + '.py'):
        os.remove(app.config['SCHEMA_LAYOUTS_FOLDER'] + '/' + filename.replace('.', '-') + '.py')

    return error


def order_xml(xmlfile, schema_name):
    from subprocess import check_output
    layout_name = schema_name.replace('.', '-')
    try:
        layouts_path = app.config['SCHEMA_LAYOUTS_FOLDER']
        doc = check_output('python %s/%s.py %s' % (layouts_path, layout_name, xmlfile))
        print(doc)
        w = open(app.config['APP_FOLDER'] + '/output.xml', 'wb')
        w.write(doc)
        w.close()
    except:
        print('fail4')
    return True
