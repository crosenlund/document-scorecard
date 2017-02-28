from lxml import etree
from lxml.etree import XMLSyntaxError
from app import app, utilities, scenarios, schemaUtilities


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
    missing_data = []
    missing_fields = []
    not_in_schema = []

    # get data from file as lxml etree
    with open(app.config['UPLOAD_FOLDER'] + "/" + file) as xml_file:
        parsing = etree.XMLParser(ns_clean=True)
        try:
            file_tree = etree.parse(xml_file, parsing)
            for node in file_tree.iter():
                if '}' in node.tag:  # remove name space if present
                    node.tag = node.tag.split("}")[1][0:]

        except XMLSyntaxError:
            errors = 'There was a problem parsing %s. Please report a bug if issue cannot be resolved from the' \
                     ' following: ( TODO: insert web link to help page)' % file
            results.append({'errors': errors})
            return results

    # copy trees for use and manipulation
    scen_tree_copy = scen_tree
    file_tree_copy = file_tree
    for node in scen_tree_copy.iter():
        node.attrib['visited'] = 'no'
    for node in file_tree_copy.iter():
        node.attrib['visited'] = 'no'

    missing_fields, missing_data, total_score, actual_score = process_nodes(scen_tree_copy, file_tree_copy,
                                                                            validate_data, missing_data, missing_fields,
                                                                            0, 0, '')

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
                    # field was not found in the schema, add to error message
                    if not field_found:
                        not_in_schema.append(file_node_path)
    # end validate against the schema

    file_results['file_name'] = file
    file_results['total_score'] = total_score
    file_results['actual_score'] = actual_score
    file_results['missing_fields'] = missing_fields
    file_results['missing_data'] = missing_data
    file_results['not_in_schema'] = not_in_schema
    results.append(file_results)
    return file_results


def process_nodes(scen_tree, file_tree, validate_data, missing_data, missing_fields, total_score, actual_score,
                  beginning_path):
    for scenario_node in scen_tree.iter():
        if scenario_node.attrib['visited'] == 'yes':
            continue

        # mark that this node has now been visited, so we do not process it again
        scenario_node.attrib['visited'] = 'yes'
        scenario_node_path = utilities.clean_xml_path(scen_tree.getpath(scenario_node))
        file_sub_tree = file_tree
        qual = ''
        value = ''
        requires_one = []
        group_path = ''

        if 'score' not in scenario_node.attrib:  # group that may have children/fields
            print(scenario_node.attrib)
            if 'qualifying-field' in scenario_node.attrib:
                qual = str(scenario_node.attrib['qualifying-field'])
            if 'qualifying-value' in scenario_node.attrib:
                value = str(scenario_node.attrib['qualifying-value'])
            if 'requires-one' in scenario_node.attrib:
                group_path = beginning_path + '/' + scenario_node.getparent().tag + '/' + scenario_node.tag
                requires_one = str(scenario_node.attrib['requires-one']).split('|')

            # validate that one of a set of fields is present in the group
            # allowing for multiple sets of fields to be delimited by pipe |
            # and then delimited by comma , with in the set of fields
            if requires_one:
                print(requires_one)
                for field_set in requires_one:
                    print(field_set)
                    fields = field_set.split(',')
                    for field in fields:
                        print(field)
                        #for each field in the set, set as visited

                        for file_node in file_tree.iter(field):
                            file_node_path = utilities.clean_xml_path(file_tree.getpath(file_node))
                            print(file_node_path)
                            print(group_path + '/' + field)
                            if utilities.same_path(group_path + '/' + field, file_node_path):
                                print(group_path + '/' + field)
                                print(file_node_path)



            if qual and value:
                # if the qualifying field is with in a group within, get the other groups
                qual_groups = []
                qual_field = qual
                if '/' in qual:
                    qual_groups = qual.split('/')
                    qual_field = qual_groups.pop()

                # check if file has qualified group that we are looking for
                # loop through groups in the file that match the current scenario qualified group
                file_qual_found, sub_tree = find_qualifier(file_sub_tree, scenario_node.tag, qual_groups, qual_field,
                                                           value, beginning_path + scenario_node_path)

                if file_qual_found:
                    file_sub_tree = sub_tree

                # add missing qualified fields to the output file
                if not file_qual_found:
                    scen_sub_tree = etree.ElementTree(scenario_node)
                    for node in scen_sub_tree.iter():
                        if 'visited' not in node.attrib or node.attrib['visited'] is not 'yes':
                            # mark the fields/groups with in this qualified group as visited, so we don't process again
                            node.attrib['visited'] = 'yes'

                            if 'score' in node.attrib:
                                node_score = int(node.attrib['score'])
                                total_score += node_score
                                missing_fields.append([node_score, utilities.clean_xml_path(
                                    beginning_path + scen_tree.getpath(node)) + " with %s = %s" % (qual, value)])

            # create a sub tree and remove the group and children from the tree copy so we only process once
            if scenario_node.getparent() is not None:  # skip the root node
                scen_sub_tree = etree.ElementTree(scenario_node)

                missing_fields, missing_data, total_score, actual_score = process_nodes(scen_sub_tree, file_sub_tree,
                                                                                        validate_data, missing_data,
                                                                                        missing_fields, total_score,
                                                                                        actual_score,
                                                                                        # allows full path in the error
                                                                                        beginning_path + '/' +
                                                                                        scenario_node_path.split('/')[
                                                                                            1])

        elif 'score' in scenario_node.attrib:
            scenario_node_text = scenario_node.text
            node_score = int(scenario_node.attrib['score'])  # every field has to have a score
            total_score += node_score

            node_found = False
            path_present = False
            not_equal = True

            for file_node in file_tree.iter(scenario_node.tag):
                file_node_path = utilities.clean_xml_path(file_tree.getpath(file_node))
                if utilities.same_path(scenario_node_path, file_node_path):
                    # print(scenario_node.attrib)

                    # logic for when validating data, not_equals
                    if validate_data:
                        path_present = True
                        if 'not_equal' in scenario_node.attrib and scenario_node.attrib['not_equal']:
                            node_found = True
                            if file_node.text == scenario_node_text:
                                not_equal = False
                        elif file_node.text == scenario_node_text:
                            node_found = True
                        else:
                            continue
                    else:
                        node_found = True

            if not not_equal:
                missing_data.append([node_score,
                                     beginning_path + scenario_node_path + " (expected data not equal to: %s)" % scenario_node_text])
            elif path_present and not node_found:
                missing_data.append(
                    [node_score, beginning_path + scenario_node_path + " (expected data: %s)" % scenario_node_text])
            elif not node_found:
                missing_fields.append([node_score, beginning_path + scenario_node_path])
            else:
                actual_score += node_score

    return missing_fields, missing_data, total_score, actual_score


def missing_component(_list, score, name):
    return _list.append([score, name])


def find_qualifier(file_sub_tree, scenario_node_tag, qual_groups, qual_field, value, scenario_node_path):
    for file_node in file_sub_tree.iter(scenario_node_tag):
        if qual_groups:
            temp_tree = etree.ElementTree(file_node)
            scenario_node_tag = qual_groups.pop(0)
            file_qual_found, sub_tree = find_qualifier(temp_tree, scenario_node_tag, qual_groups, qual_field, value,
                                                       scenario_node_path + "/" + scenario_node_tag)

            if file_qual_found:
                # return the orginal sub tree so we can finish processing now that we could the correct qualified group
                return True, file_sub_tree
            else:
                return False, None

        file_node_path = utilities.clean_xml_path(file_sub_tree.getpath(file_node))
        if utilities.same_path(scenario_node_path, file_node_path):
            temp_tree2 = etree.ElementTree(file_node)
            for temp_node in temp_tree2.iter(qual_field):
                if qual_field == temp_node.tag and value == temp_node.text:
                    file_sub_tree = etree.ElementTree(file_node)
                    return True, file_sub_tree

    return False, None
