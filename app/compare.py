from lxml import etree
from lxml.etree import XMLSyntaxError
from app import app, utilities, scenarios
import re


def compare(files, scenarios_list, validate_data, validate_schema):
    errors = ''
    test_results = []
    scen_tree = None
    for scenario in scenarios_list:
        if scenarios.existing_scenario(None, scenario):
            scen_id = scenarios.get_id(scenario)
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
                    test_results = process_file(file, scen_tree, validate_data, validate_schema)
                else:
                    errors += "Unable to retrieve file '" + file.name + "' because of invalid extension."
        else:
            errors += "scenario '" + scenario + "' was not found."


def process_file(file, scen_tree, validate_data, validate_schema):
    results = []
    total_score = 0
    actual_score = 0
    errors = ''
    file_tree = None

    with open(app.config['UPLOAD_FOLDER'] + "/" + file) as xml_file:
        parsing = etree.XMLParser(ns_clean=True)
        try:
            file_tree = etree.parse(xml_file, parsing)
            root = file_tree.getroot()
            print(root.getchildren())
            for child in root.getchildren():
                print(child.tag)
                if child.tag == 'ItemRegistry':
                    print(child.tag)
            scen_tree_root_node = scen_tree.getroot()
            scen_tree_root_node_name = scen_tree_root_node.tag
            print(scen_tree.getpath(scen_tree_root_node).split('/')[-1].split("}")[1][0:])
            find_node = scen_tree.getpath(scen_tree_root_node)
            for node2 in file_tree.iter(find_node):
                print(node2)
            # file_tree = file_tree.find('/'+scen_tree.getroot().tag)
            print(file_tree)
        except XMLSyntaxError:
            errors += 'There was a problem parsing %s. Please report a bug if issue cannot be resolved from the' \
                      ' following: ( TODO: insert web link to help page)' % file
            results.append({'errors': errors})
            return results

    # start with the scenario data and compare to that in the test file
    for node in scen_tree.iter():
        scenario_node_path = re.sub("\\[\d\\]", "", scen_tree.getpath(node))
        print(scenario_node_path)
        node_score = 0
        print(node.attrib)
        if 'score' in node.attrib:
            print(node.attrib['score'])
            node_score = int(node.attrib['score'])
            total_score += node_score
            print(total_score)
        print(node)
        print('xpath: %r' % scen_tree.xpath('/ItemRegistry'))
        # print("%s - %s" % (node.tag, node.text))
        # print(scen_tree.getpath(node))
        for node2 in file_tree.iter(node.tag):
            print(node2)
            file_node_path = re.sub("\\[\d\\]", "", file_tree.getpath(node2))
            if scenario_node_path == file_node_path:
                print('match! - ')
                print(scen_tree.getpath(node))
                print(file_tree.getpath(node2))
            # print("%s - %s - %s" % (node2.tag, node2.text, node2.getparent().tag))
            # print(file_tree.getpath(node2))

    # for node in nodes:
    #     print(node)
    #     print(node.tag)
    #     print(node.text)
    #     print(node.attrib)

    return results
