from lxml import etree
from lxml.etree import XMLSyntaxError
from app import app, scenarios, utilities


def find_qualifier(tree):
    qualifier_fields = {}
    qualifier_list = ['ContactTypeCode', 'AddressTypeCode', 'DateTimeQualifier1']
    for element in tree.iter():
        print(element)
        if len(element) < 1 and element.tag in qualifier_list:
            print("is qual {%s)" % element.text)
            qualifier_fields[element.tag] = element.text

    return qualifier_fields


def check_for_qualifiers(con_sub_tree, scen_sub_tree, qualifier_fields):
    found_all_qualifiers = True
    for qualifier_field in qualifier_fields:
        found_this_quailifer = False
        for scen_qual_field in scen_sub_tree.iter(qualifier_field):
            # need to make the xpaths play nice and look pretty, removes any repetition notation
            scen_qual_field_path = utilities.clean_xml_path(scen_sub_tree.getpath(scen_qual_field))
            qualifier_field_path = utilities.clean_xml_path(con_sub_tree.getpath(qualifier_field))
            if utilities.same_path(scen_qual_field_path, qualifier_field_path):
                # found this qualifier, move to next
                found_this_quailifer = True
                break
        if not found_this_quailifer:
            # not all qualifiers were found
            found_all_qualifiers = False
            break

    return found_all_qualifiers


def check_qualifiers_match(scen_quals, con_quals):
    for e,v in scen_quals.items():
        qual_found = False
        for c_e, c_v in con_quals.items():
            if e == c_e and v == c_v:
                qual_found = True
            if qual_found:
                break
        if not qual_found:
            return False
    return True


def mark_visited(group):
    for node in group.iter():
        node.attrib['visited'] = 'yes'


def process_tree(consolidated_xml, scen_tree):
    for node2 in scen_tree.iter():
        if len(node2) == 0 and 'visited' not in node2.attrib:  # is an element
            scen_parent = node2.getparent()
            mark_visited(scen_parent)
            scen_qualifier_fields = find_qualifier(scen_parent)
            print('-', scen_parent)
            scen_node_path = utilities.clean_xml_path(scen_tree.getpath(scen_parent))

            found_in_consolidated = False
            for c_node in consolidated_xml.iter(scen_parent.tag):

                if scen_qualifier_fields:
                    consolidated_qualifier_fields = find_qualifier(c_node)
                    con_node_path = utilities.clean_xml_path(consolidated_xml.getpath(c_node))
                    if utilities.same_path(scen_node_path, con_node_path):
                        if check_qualifiers_match(scen_qualifier_fields, consolidated_qualifier_fields):
                            found_in_consolidated = True
                            # sub_consolidated_tree = etree.ElementTree(c_node)
                            for scen_node in scen_parent:
                                if not c_node.find(".//%s" % scen_node):
                                    c_node.append(scen_node)

            if not found_in_consolidated:
                print(scen_parent)

    return consolidated_xml, scen_tree


def consolidate_scenarios(scenarios_list):
    first_scenario = True
    consolidated_xml = None
    print("consolidation")
    for scenario in scenarios_list:
        print("scenario:"+scenario)
        if scenarios.existing_scenario(None, scenario):
            scen_tree = None
            scen_id = scenarios.get_id(scenario)
            scenario_xml, error = scenarios.to_xml(scen_id, False)
            scenario_xml = scenario_xml.decode("utf-8")

            with open(app.config['UPLOAD_FOLDER'] + "/scen_to_consolidate.xml", 'w') as scen_file:
                scen_file.write(scenario_xml)
            with open(app.config['UPLOAD_FOLDER'] + "/scen_to_consolidate.xml") as scen_file:
                parsing = etree.XMLParser(ns_clean=True)
                try:
                    scen_tree = etree.parse(scen_file, parsing)
                except XMLSyntaxError:
                    errors = None, 'consolidate.consolidate_scenarios getting scen_to_consolidate.xml'

            if scen_tree is not None:
                if first_scenario:
                    first_scenario = False
                    consolidated_xml = scen_tree
                    continue

            consolidated_xml, scen_tree = process_tree(consolidated_xml, scen_tree)

    if consolidated_xml:
        return etree.tostring(consolidated_xml, pretty_print=True)
    else:
        return ''


# print("Process_tree")
# for node2 in scen_tree.iter():
#     if len(node2) > 0:  # has children, then its a group
#         print("-1-", node2)
#         sub_scen_tree = etree.ElementTree(node2)
#         scen_qualifier_fields = find_qualifier(sub_scen_tree)
#         group_in_consolidated_xml = False  # flag to determine if this group already exists
#         for c_node in consolidated_xml.iter(node2.tag):
#
#             group_in_consolidated_xml = True
#             sub_consolidated_tree = etree.ElementTree(c_node)
#             consolidated_qualifier_fields = find_qualifier(sub_consolidated_tree)
#             found_all_qualifiers = check_for_qualifiers(consolidated_xml, sub_scen_tree,
#                                                         consolidated_qualifier_fields)
#
#             # all qualifiers in group c_node were found in the matching scenario group
#             # check that all fields in the scenario group are within this c_node group, add any missing fields
#             print("scen_qualifier_fields: %r      found_all_qualifiers: %r" % (scen_qualifier_fields, found_all_qualifiers))
#             if scen_qualifier_fields and found_all_qualifiers:
#                 for scen_node in sub_scen_tree.iter():
#                     print("-----", scen_node)
#                     # if scen_node is a group, recursively do this same process
#                     if len(scen_node) > 0:
#                         process_tree(sub_consolidated_tree, sub_scen_tree)
#                         continue
#                     # check if this consolidated group has this scenario field, if not add it
#                     if not sub_consolidated_tree.xpath(scen_node.tag):
#                         sub_consolidated_tree.append(scen_node)
#
#             if scen_qualifier_fields is None:
#                 # TODO loop through groups and ensure fields are present
#                 pass
