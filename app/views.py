# from application.app import scenarios, app, parse, creator, utils
import os
import logging
from app import app, scenarios, utils, parse, creator, schemaValidation, schemaOrder
from flask import render_template, redirect, url_for, request, make_response, Response, json
from werkzeug import secure_filename
import time

ALLOWED_EXTENSIONS = ['txt', 'xml']


# load main page
@app.route('/')
@app.route('/index')
def documentscorecard_index():
    return render_template("index.html", scenarios=get_scenario_list())


# returns a list of all the scenarios (name, id, schema...) in the database in json form
@app.route('/get_scenario_list', methods=['GET'])
def get_scenario_list():
    return Response(json.dumps(scenarios.get_all_scenarios()), mimetype='application/json')


# accepts an uploded file and parses it into a new scenario with the passed information
@app.route('/upload_new_scenario', methods=['POST'])
def upload_new_scenario():
    if request.method == 'POST':
        file = request.files['file']
        data = json.loads(request.form['data'])
        error = ''
        scenario_data = []
        is_valid = False

        if file:
            if utils.file_allowed(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                scenario_data, new_error = parse.new_scenario(app.config['UPLOAD_FOLDER'] + '/' + filename)
                if scenario_data:
                    is_valid = True
                else:
                    error += new_error
            else:
                error += 'File extension is not allowed.'
        else:
            error += "A file must be uploaded to create a new scenario."

        if is_valid:  # scenario was successfully parsed
            created_scenario, new_error = creator.build_scenario(data, scenario_data)

            if new_error:
                error += new_error
        if len(error) < 1:
            return get_scenario_list()
        else:
            response = make_response(error, 400)
            return response


# delete a scenario if it exists
@app.route('/delete_scenario', methods=['POST'])
def delete_scenario():
    if request.method == 'POST':
        scen_id = request.json['scenID']
        success, error = scenarios.delete_scenario(scen_id)
        if success:
            logging.info("Scenario " + str(scen_id) + " was successfully deleted.")
            return get_scenario_list()
        else:
            return make_response("Unable to deleted scenario " + str(scen_id) + ".", 400)


# copy a scenario that already exists, name must change others are optional
@app.route('/copy_scenario', methods=['POST'])
def copy_scenario():
    if request.method == 'POST':
        scen_id = request.json['scenID']
        scen_name = request.json['scenName']
        success, error = scenarios.copy_scenario(scen_id, scen_name)
        if success:
            logging.info("Scenario " + str(scen_id) + " was successfully copied.")
            return get_scenario_list()
        else:
            return make_response("Unable to copy scenario (" + str(scen_id) + ").  " + error + "", 400)


# renames a scenario that already exists
@app.route('/edit_scenario', methods=['POST'])
def edit_scenario():
    if request.method == 'POST':
        scen_id = request.json['scenID']
        name = request.json['name']
        current_name, error = scenarios.get_info(scen_id)
        current_name = current_name[1]
        if name == current_name:
            same_name = True
        else:
            same_name = False
        schema = request.json['schema']
        description = request.json['description']
        doc_type = request.json['docType']
        root_name = request.json['rootName']
        fulfillment_type = request.json['fulfillmentType']
        success, error = scenarios.edit_scenario(scen_id, name, description, doc_type, fulfillment_type, schema,
                                                 root_name, same_name)
        if success:
            logging.info("Scenario %s was successfully updated(%s, %s, %s, %s, %s, %s)." % (
                scen_id, name, description, doc_type, fulfillment_type, schema, root_name))
            return get_scenario_list()
        else:
            response = make_response(error, 400)
            return response


# returns json of a scenario
@app.route('/get_scenario_json', methods=['POST'])
def get_scenario_json():
    if request.method == 'POST':
        scenario_data = ''
        scen_id = request.json['scenID']

        if scenarios.existing_scenario(scen_id, None):
            scenario_data, error = scenarios.to_json(scen_id)
        else:
            error = "That scenario does not exist."
        if len(error) < 1:
            return Response(json.dumps(scenario_data), mimetype='application/json')
        else:
            response = make_response(error, 400)
            return response


# returns XML of a scenario
@app.route('/get_scenario_xml', methods=['POST'])
def get_scenario_xml():
    start_time = time.time()
    if request.method == 'POST':
        scen_id = request.json['id']
        scen_name = request.json['name']
        schema = request.json['schema']
        xml_string, error = scenarios.to_xml(scen_id)
        with open(app.config['APP_FOLDER'] + '/output.xml', 'wb') as w:
            w.write(xml_string)
        xml_string = schemaOrder.order.order_xml(app.config['APP_FOLDER'] + '/output.xml', schema)

        with open(app.config['APP_FOLDER'] + '/output.xml', 'r') as r:
            xml_string = r.read()
        print('get_scenario_xml took %s seconds' % (time.time() - start_time))
        if error:
            response = make_response(error, 400)
            return response
        else:
            response = make_response(xml_string)
            response.headers["Content-Disposition"] = "attachment;filename=%s.txt" % scen_name
            return response


# --------------------SCHEMA VALIDATION------------------------------------------
# function to check whether the uploaded schema has a valid '.xsd' file extension
@app.route('/get_schema_list', methods=['GET'])
def get_schema_list():
    return json.dumps(schemaValidation.validate.get_schema_list())


@app.route('/add_schema', methods=['POST'])
def add_schema():
    if request.method == 'POST':
        file = request.files['file']
        data = json.loads(request.form['data'])
        schema_name = data['schema']
        error = ''
        if file:
            # if this is empty, schema was successfully added
            error = schemaValidation.validate.add_schema(file, schema_name)
        else:
            error = "A schema must be upload."
        if len(error) > 0:
            return make_response(error, 400)
        return get_schema_list()


@app.route('/delete_schema', methods=['POST'])
def delete_schema():
    filename = request.json['delete']
    # if this is empty, schema was successfully deleted
    error = schemaValidation.validate.delete_schema(filename)
    if len(error) > 0:
        return make_response(error, 400)
    return get_schema_list()
