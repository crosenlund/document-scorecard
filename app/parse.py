from lxml.etree import XMLSyntaxError
from lxml import etree
import re
import logging


# returns json data of a parsed xml file
# makes sure that every field has a score
def new_scenario(file_name):
    error = ''
    with open(file_name) as xml_file:
        parsing = etree.XMLParser(ns_clean=True)
        try:
            data_tree = etree.parse(xml_file, parsing)
        except XMLSyntaxError:
            return '', 'There was a problem parsing %s. Please report a bug if issue cannot be resolved from the' \
                       ' following: ( TODO: insert web link to help page)' % file_name

    # remove the namespace from the nodes' tag/name
    nodes = data_tree.iter()
    for node in nodes:
        if '}' in node.tag:
            node.tag = node.tag.split("}")[1][0:]

    # go through all the fields in the document to check for scores, if missing or invalid - err
    nodes = data_tree.iter()
    for node in nodes:
        if len(node) < 1:  # this is a leaf node, or a field
            if 'score' in node.attrib:
                score_is_number = False
                try:
                    score = int(node.attrib['score'])
                    if score or score == 0:  # python does not consider 0 as true in the first argument
                        score_is_number = True
                except ValueError:
                    error += '\n line %s: invalid score for %s' % (node.sourceline, node.tag)
                if score_is_number:
                    if score < 1 or score > 5:
                        error += '\n line %s: invalid score for %s' % (node.sourceline, node.tag)
            else:
                error += '\n line %s: missing score for %s' % (node.sourceline, node.tag)

    if error:
        logging.info(error)
        return "", error

    root_node = data_tree.getroot()
    root_node_name = root_node.tag

    # this is the start of the json building
    fields, groups = process_node(root_node)
    if fields:  # these are used so we don't get messy empty groups in the json data
        if groups:
            return {"rootName": root_node_name, "fields": fields, "groups": groups}, ''
        if not groups:
            return {"rootName": root_node_name, "fields": fields}, ''
    if not fields:
        if groups:
            return {"rootName": root_node_name, "groups": groups}, ''
        if not groups:
            return {"rootName": root_node_name}, ''


# this is a recursive method that builds the json of a scenario xml file, base case is when a field is reached
def process_node(parent_node):
    field_data = []
    group_data = []
    data = []
    for child in parent_node.getchildren():
        if len(child) < 1:
            field_data.append(build_field(child))
        else:
            group_data.append(build_group(child))

    if field_data:
        data.append({"Fields": field_data})
    if group_data:
        data.append({"Groups": group_data})

    return field_data, group_data


# a helper method that builds groups for the scenario json data
def build_group(node):
    print(node.attrib)
    if 'qualifying-field' in node.attrib:
        qualifying_field = node.attrib['qualifying-field']
    else:
        qualifying_field = ''

    if 'qualifying-value' in node.attrib:
        qualifying_value = node.attrib['qualifying-value']
    else:
        qualifying_value = ''

    requires_one = ''
    if 'requires-one' in node.attrib:
        requires_one = node.attrib['requires-one']

    fields, groups = process_node(node)

    if fields:
        if groups:
            return {"name": node.tag, "qualifying_field": qualifying_field, "qualifying_value": qualifying_value,
                    'requires_one': requires_one, "fields": fields, "groups": groups}
        if not groups:
            return {"name": node.tag, "qualifying_field": qualifying_field, "qualifying_value": qualifying_value,
                    'requires_one': requires_one, "fields": fields}
    if not fields:
        if groups:
            return {"name": node.tag, "qualifying_field": qualifying_field, "qualifying_value": qualifying_value,
                    'requires_one': requires_one, "groups": groups}
        if not groups:
            return {"name": node.tag, "qualifying_field": qualifying_field, "qualifying_value": qualifying_value,
                    'requires_one': requires_one}


# helper method to take in individual fields/leaves and give back a dict with the field's xpath, score,
# and required data
# parameters: string xpath, string node.text
# returns: dict
def build_field(node):
    name = node.tag
    data = node.text
    score = node.attrib['score']
    not_equal = False
    if 'not-equal' in node.attrib:
        not_equal = True
    requires = ''
    if 'requires' in node.attrib:
        requires = node.attrib['requires']

    return {'name': name, 'score': score, 'data': data, 'not_equal': not_equal, 'requires': requires}


def input(file_name):
    xpath_list = {}
    empty_nodes = []
    xml = open(file_name)
    parser = etree.XMLParser(ns_clean=True)
    try:
        tree = etree.parse(xml, parser)

    except XMLSyntaxError:
        return "Error", "There was a problem parsing %s." % file_name
    xml.close()
    etree.tostring(tree.getroot())

    for node in tree.iter():
        if len(node) < 1:
            if node.text is not None:
                xpath = re.sub("\[\d*\]", "", tree.getpath(node))
                if xpath not in xpath_list.keys():
                    xpath_list[xpath] = [node.text]
                else:
                    xpath_list[xpath].append(node.text)
            else:
                empty_nodes.append(re.sub("\[\d*\]", "", tree.getpath(node)))
                # print("input parse %s - %s" % (tree.getpath(node), node.text))
    return xpath_list, empty_nodes, tree
