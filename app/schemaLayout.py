import os
from lxml import etree
import re
import time
import logging
from app import app


def remove_empty_lines(txt):
    return '\n'.join([x for x in txt.split("\n") if x.strip() != ''])


def configure_xsd(xsd):
    logging.info("configuring_xsd")
    regex_single_line = {'<xs:enumeration value=".+?">': '', '</xs:enumeration>': '', '<xs:enumeration.+?/>': '',
                         ' minOccurs="0"': ''}
    regex_multiple_lines = {'<xs:annotation.+?</xs:annotation>': '',
                            '<xs:simpleType>.+?<xs:restriction base="(.+?)">.+?</xs:simpleType>': '\\1'}
    # this adds the type attribute to field element tags when they appear inside the xsd
    regex_add_element_type = {
        '(\s+?<xs:element name=\"[^\"]+?\")\s?>\n?\s+?(xs:string)\n\s+?</xs:element>': '\\1 type="\\2"/>\n'}
    # change all element types from xs:string to xs:attributes-string to allow for the attributes we have added
    regex_change_element_type = {'type="xs:.+?"': 'type="attributes-string"'}

    f = open(xsd, 'r+')
    file_string = f.read()
    f.close()

    for regex, replacement in regex_single_line.items():
        file_string = re.sub(regex, replacement, file_string)

    for regex, replacement in regex_multiple_lines.items():
        regex = re.compile(regex, re.DOTALL)
        file_string = re.sub(regex, replacement, file_string)

    for regex, replacement in regex_add_element_type.items():
        regex = re.compile(regex, re.DOTALL)
        file_string = re.sub(regex, replacement, file_string)

    for regex, replacement in regex_change_element_type.items():
        file_string = re.sub(regex, replacement, file_string)

    # remove any blank lines in the file
    file_string = remove_empty_lines(file_string)

    # add the field and group attributes to the xsd file
    file_string = re.sub('</xs:schema>', add_attributes() + '\n</xs:schema>', file_string)
    file_string = re.sub('<xs:sequence>', '<xs:sequence>' + add_group_attributes(), file_string)

    w = open(xsd, 'w')
    w.write(file_string)
    w.close()
    return True


def add_attributes():
    logging.info("add_attributes")
    attribs = ''
    ATTRIBUTE_TYPES = {'string'}
    ATTRIBUTES = {'score': 'int', 'requires': 'string', 'not-equal': 'string'}
    for attribtypes in ATTRIBUTE_TYPES:
        attribs = '<xs:complexType name = "attributes-%s">\n<xs:simpleContent>\n<xs:extension base = "xs:%s">\n' \
                  % (attribtypes, attribtypes)
        for attribute, Att_type in ATTRIBUTES.items():
            attribs += '<xs:attribute name = "%s" type = "xs:%s"/> \n' % (attribute, Att_type)
        attribs += '</xs:extension>\n</xs:simpleContent>\n</xs:complexType>'

    return attribs


def add_group_attributes():
    attribs = ''

    GROUP_ATTRIBUTES = {'qualifying-field': 'string', 'qualifying-value': 'string', 'requires-one': 'string'}
    for attribute, Att_type in GROUP_ATTRIBUTES.items():
        attribs += '\n<xs:attribute name = "%s" type = "xs:%s"/>' % (attribute, Att_type)

    return attribs


def create_schema_layout(xsd, schema_name):
    logging.info("create_schema_layout")
    schema = etree.parse(xsd)
    schema.write(xsd)  # This needs to be done only one time when the file is first uploaded
    root = schema.getroot()
    string_o = root[0].attrib['name']
    string_s = root[1].attrib['name']
    _object = '%s/%s.py' % (app.config['SCHEMA_LAYOUTS_FOLDER'], schema_name)
    sub_object = '%s/%s.py' % (app.config['UPLOAD_FOLDER'], string_s)
    _super = string_o
    xsd_name = xsd
    generateDS_path = app.config['GENERATEDS_FOLDER']
    print(generateDS_path)
    print(_object)
    print(xsd_name)

    try:
        import subprocess
        print(subprocess.call('python %s/generateDS.py -f -o %s -s %s --super="%s" %s'
                              % (generateDS_path, _object, sub_object, _super, xsd_name)))
    except OSError as e:
        logging.info("SchemaCreation.py: there was an issue with creating the schema layout (schemaLayout.py)")
    return True
