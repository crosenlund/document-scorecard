import os
from lxml import etree
import re
import time
import logging
from app import app


class create:
    @staticmethod
    def remove_empty_lines(txt):
        return '\n'.join([x for x in txt.split("\n") if x.strip() != ''])

    @staticmethod
    def configure_xsd(xsd):
        logging.info("configuring_xsd")
        REGEX_single_line = {'<xs:enumeration value=".+?">': '', '</xs:enumeration>': '', '<xs:enumeration.+?/>': '',
                             ' minOccurs="0"': '', ' maxOccurs="unbounded"': ''}
        REGEX_multiple_lines = {'<xs:annotation.+?</xs:annotation>': '',
                                '<xs:simpleType>.+?<xs:restriction base="(.+?)">.+?</xs:simpleType>': '\\1'}
        # this adds the type attribute to field element tags when they appear inside the element
        REGEX_add_element_type = {
            '(\s+?<xs:element name=\"[^\"]+?\")\s?>\n?\s+?(xs:string)\n\s+?</xs:element>': '\\1 type="\\2"/>\n'}
        # change all element types from xs:string to xs:attributes-string to allow for the attributes we have added
        REGEX_change_element_type = {'type="xs:.+?"': 'type="attributes-string"'}

        f = open(xsd, 'r+')
        file_string = f.read()
        f.close()

        for regex, replacement in REGEX_single_line.items():
            file_string = re.sub(regex, replacement, file_string)

        for regex, replacement in REGEX_multiple_lines.items():
            regex = re.compile(regex, re.DOTALL)
            file_string = re.sub(regex, replacement, file_string)

        for regex, replacement in REGEX_add_element_type.items():
            regex = re.compile(regex, re.DOTALL)
            file_string = re.sub(regex, replacement, file_string)

        for regex, replacement in REGEX_change_element_type.items():
            file_string = re.sub(regex, replacement, file_string)

        # remove any blank lines in the file
        file_string = create.remove_empty_lines(file_string)

        # add the attributes to the xsd file
        file_string = re.sub('</xs:schema>', create.add_attributes() + '\n</xs:schema>', file_string)
        w = open(xsd, 'w')
        w.write(file_string)
        w.close()
        return True

    @staticmethod
    def add_attributes():
        logging.info("add_attributes")
        attribs = ''
        # ATTRIBUTE_TYPES = {'integer', 'string', 'date', 'decimal', 'boolean', 'date', 'time'}
        ATTRIBUTE_TYPES = {'string'}
        ATTRIBUTES = {'score': 'int', 'qualified-rep': 'string', 'requires-one': 'string', 'not-equal': 'string',
                      'requires-others': 'string'}
        for attribtypes in ATTRIBUTE_TYPES:
            attribs = '<xs:complexType name = "attributes-%s">\n<xs:simpleContent>\n<xs:extension base = "xs:%s">\n' \
                      % (attribtypes, attribtypes)
            for attribute, Att_type in ATTRIBUTES.items():
                attribs += '<xs:attribute name = "%s" type = "xs:%s"/> \n' % (attribute, Att_type)
            attribs += '</xs:extension>\n</xs:simpleContent>\n</xs:complexType>'
        # print("add_attributes--- %s seconds ---" % (time.time() - start_time))
        return attribs

    @staticmethod
    def create_schema(xsd):
        logging.info("create_schema")
        schema = etree.parse(xsd)
        schema.write(xsd)  # This needs to be done only one time when the file is first uploaded
        root = schema.getroot()
        string_o = root[0].attrib['name']
        string_s = root[1].attrib['name']
        # string_o = 'schemasLayout'
        # string_s = 'schema'
        _object = '%s/%s.py' % (app.config['APP_FOLDER'], string_o)
        sub_object = '%s.py' % string_s
        _super = string_o
        xsd_name = xsd
        generateDS_path = app.config['GENERATEDS_FOLDER']
        print(generateDS_path)
        print(_object)
        print(xsd_name)

        try:
            import subprocess
            # print(subprocess.call('python %s/generateDS.py --silence -f -o %s %s'
            #                       % (generateDS_path, _object, xsd_name)))
            print(subprocess.call('python %s/generateDS.py -f -o %s -s %s --super="%s" %s'
                      % (generateDS_path,_object, sub_object, _super, xsd_name)))
            # process.wait()
            # print(process.returncode)
            # success = os.system('python %s/generateDS.py --silence -f -o %s %s'
            #       % (generateDS_path, _object, xsd_name))
            # retcode = os.call('python %s/generateDS.py --silence -f -o %s %s'
            #       % (generateDS_path, _object, xsd_name), shell=True)
            # if process < 0:
            #     print("Child was terminated by signal")
            # else:
            #     print("Child returned", process)
        except OSError as e:
            logging.info("SchemaCreation.py: there was an issue with creating the schema layout (schemaLayout.py)")
        # os.system('python generateDS/generateDS.py -f -o "app/schemasLayout.py" -s "schema.py" --super="schemasLayout" app/SCHEMAS/ItemRegisty-7.6.1.xsd')
        print('creating schema')
        # os.system('python %s/generateDS.py -f -o %s -s %s --super="%s" %s'
        #           % (generateDS_path,_object, sub_object, _super, xsd_name))
        return True
