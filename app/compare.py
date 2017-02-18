from lxml import etree
from lxml.etree import XMLSyntaxError
from app import app, utilities, scenarios, schemaUtilities
import re


def compare(files, scenarios_list, validate_data, validate_schema):
    errors = ''
    test_results = []
    scen_tree = None

    for scenario in scenarios_list:
        if scenarios.existing_scenario(None, scenario):
            scenario_results = []
            scen_id = scenarios.get_id(scenario)
            # get the schema name if we are validating against it
            schema = ''
            if validate_schema:
                schema = scenarios.get_schema_name(scen_id)
            scenario_xml, error = scenarios.to_xml(scen_id)
            scenario_xml = scenario_xml.decode("utf-8")
            with open(app.config['UPLOAD_FOLDER'] + "/scen_to_compare.xml", 'w') as scen_file:
                scen_file.write(scenario_xml)
            with open(app.config['UPLOAD_FOLDER'] + "/scen_to_compare.xml") as scen_file:
                parsing = etree.XMLParser(ns_clean=True)
                try:
                    scen_tree = etree.parse(scen_file, parsing)
                except XMLSyntaxError:
                    errors += 'Compare.process_file getting scen_to_compare.xml'
            for file in files:
                if utilities.file_allowed(file):
                    scenario_results.append(process_file(file, scen_tree, validate_data, validate_schema, schema))
                else:
                    errors += "Unable to retrieve file '" + file.name + "' because of invalid extension."

            test_results.append({scenario: scenario_results})

        else:
            errors += "scenario '" + scenario + "' was not found."

    return test_results


def process_file(file, scen_tree, validate_data, validate_schema, schema):
    results = []
    file_results = {}
    total_score = 0
    actual_score = 0
    errors = ''
    missing_fields = []
    not_in_schema = []
    missing_data = []
    file_tree = None

    with open(app.config['UPLOAD_FOLDER'] + "/" + file) as xml_file:
        parsing = etree.XMLParser(ns_clean=True)
        try:
            file_tree = etree.parse(xml_file, parsing)
            root = file_tree.getroot()
            for node in file_tree.iter():
                if '}' in node.tag:  # remove name space if present
                    node.tag = node.tag.split("}")[1][0:]

        except XMLSyntaxError:
            errors = 'There was a problem parsing %s. Please report a bug if issue cannot be resolved from the' \
                     ' following: ( TODO: insert web link to help page)' % file
            results.append({'errors': errors})
            return results

    # start with the scenario data and compare to the data in the test file
    for scenario_node in scen_tree.iter():
        scenario_node_path = utilities.clean_xml_path(scen_tree.getpath(scenario_node))
        if scenario_node.getparent() is None:  # skip the root node
            continue
        if len(scenario_node) > 1:  # group that has children/fields
            process_node(scenario_node)
            continue
        if len(scenario_node) < 1:  # field
            node_score = 0
            if 'score' in scenario_node.attrib:  # this should always be true, fields must have a score
                node_score = int(scenario_node.attrib['score'])
                total_score += node_score

            node_found = False
            path_present = False
            for file_node in file_tree.iter(scenario_node.tag):
                file_node_path = utilities.clean_xml_path(file_tree.getpath(file_node))
                # check if the strings are within each other to avoid starting with different root tags
                # ie ItemRegistries/ItemRegistry vs ItemRegistry will be the same
                if scenario_node_path in file_node_path or file_node_path in scenario_node_path:
                    if validate_data:
                        path_present = True
                        print("file_node.text:", file_node.text)
                        print("scenario_node.text:", scenario_node.text)
                        if file_node.text == scenario_node.text:
                            print(scenario_node_path)
                            node_found = True
                        else:
                            continue
                    else:
                        node_found = True

                if node_found:
                    actual_score += node_score
                    break

            if path_present and not node_found:
                missing_data.append([node_score, scenario_node_path])
            elif not node_found:
                missing_fields.append([node_score, scenario_node_path])

    # validate against the schema
    # run the test file through the order_xml function to give us the fields in the file that are in the schema
    # compare the original test file against the new file to find the fields that are not in the schema, return them
    if validate_schema and schema:
        schema_file = schemaUtilities.order_xml(app.config['UPLOAD_FOLDER'] + "/" + file, schema)
        if schema_file:
            with open(app.config['APP_FOLDER'] + '/output.xml') as schema_file:
                parsing = etree.XMLParser(ns_clean=True)
                try:
                    schema_tree = etree.parse(schema_file, parsing)
                except XMLSyntaxError:
                    errors = 'There was a problem validating against the schema for %s. If this does not resolve,' \
                             ' please report a bug/issue' % file
                    results.append({'errors': errors})
                    return results

                for file_node in file_tree.iter():
                    field_found = False
                    file_node_path = utilities.clean_xml_path(file_tree.getpath(file_node))
                    for schema_node in schema_tree.iter(file_node.tag):
                        schema_node_path = utilities.clean_xml_path(schema_tree.getpath(schema_node))
                        # check if the strings are within each other to avoid starting with different root tags
                        # ie ItemRegistries/ItemRegistry vs ItemRegistry will be the same
                        if schema_node_path in file_node_path or file_node_path in schema_node_path:
                            field_found = True
                            break
                    # field was not found in the schema
                    if not field_found:
                        not_in_schema.append(file_node_path)

    file_results['file_name'] = file
    file_results['total_score'] = total_score
    file_results['actual_score'] = actual_score
    file_results['missing_fields'] = missing_fields
    file_results['missing_data'] = missing_data
    file_results['not_in_schema'] = not_in_schema
    print('-----------')
    print(not_in_schema)
    results.append(file_results)
    return file_results


def process_node(node):
    return True
