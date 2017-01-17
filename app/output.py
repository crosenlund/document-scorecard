from lxml import etree
import re


class Output:
    # parsed_input is the list of xpaths in the xml input file.
    # selected_list is the string of scenario names taken from user input.
    # tree is the whole etree object created from the input XML file.
    # check content is a boolean saying whether we should check for required data or not.
    @staticmethod
    def create_file(parsed_input, empty_nodes, tree, selected_list, check_content):

        scen_names = selected_list.split(',')
        error = ''
        output = ''
        total_score = 0  # will hold the total score for all the scenarios
        total_possible_score = 0  # will hold the total possible score for all the scenarios

        # add the xpaths of any blank fields from the input to the output
        output += "Fields in the input file that are present but have no data: \r\n"
        for node in empty_nodes:
            output += node + '\r\n'
        output += "\r\n*********************************************************************\r\n"

        # compare input to each scenario in the list
        for scenario in scen_names:
            scen_name = scenario
            exists = models.Scenario.check_exists(scen_name)

            # check that the scenario exists
            if exists:
                scen = models.Scenario.get_scenario(scen_name)
                esps = scen.get_esps()
                failures, score, possible_score = compare.Compare.compare(parsed_input, esps, tree, check_content)

                total_score += score
                total_possible_score += possible_score
                scen_percent = "Invalid"
                if possible_score > 0:
                    scen_percent = round(100 - (score / possible_score) * 100, 2)
                # output the score for each scenario
                output += "\r\nScore for Scenario %s, amount of required data that is present : %s%%, %s / %s \r\n\r\n" \
                          % (scenario, str(scen_percent), str((possible_score - score)), str(possible_score))

                # add xpaths of missing fields or repetitions to the output file
                for path in failures:
                    if 'qualified' in path:
                        output += "\r\n%s \r\n\r\n" % path
                    else:
                        output += "Missing field: %s \r\n" % path
                output += "\r\n*********************************************************************\r\n"

            else:
                error += "Scenario %s is not available. Would you like to try another?" % scenario

        if total_possible_score is not 0:
            percentage = round(100 - (total_score / total_possible_score) * 100, 2)
        else:
            percentage = "Invalid"

        # output the total score for all scenarios
        output = "Total Score for all Scenarios, amount of required data that is present: %s%%,  %s / %s \r\n\r\n" % \
                 (str(percentage), str((total_possible_score - total_score)),
                  str(total_possible_score)) + output + '\r\n'
        if len(error) > 1:
            return "Error: " + error
        else:
            return output

    # method to turn all the xpaths, scores, and data from a scenario back into an etree with all fields as children of their
    # correct groups and groups as children of their correct groups
    # the etree is sent back to views.py where it gets downloaded as a text file
    def get_scenario_as_xml_tree(scen_name):
        if models.Scenario.check_exists(scen_name):
            scen = models.Scenario.get_scenario(scen_name)
            esps = scen.get_esps()
            first = esps[0]
            splits = first.xpath.split('/')
            Output.root = etree.Element(splits[1])
            Output.tree = etree.ElementTree(Output.root)

            # for each of the esps in the scenario's list of esps, add the esp at the correct place in the etree
            for esp in esps:
                Output.add_esp(esp)
                # if the ESP is a qualifier, we have to get all its children and add them to only this particular repetition of this group
                if esp.is_qualifier():
                    # if there is more than one of this group, find the correct group by matching data
                    for leaf in Output.tree.xpath('/' + esp.xpath):
                        if leaf.text == esp.data + "[qualified rep]" + ' ' + str(esp.score) + ' ':
                            parent = leaf.getparent()
                            cs = esp.get_qual_children()
                            children = []
                            groups = []
                            # reorder fields and groups contained inside a qualified rep so that fields come first and groups show up at the bottom
                            for c in cs:
                                if '/' in re.sub(Output.get_containing_group(esp.xpath) + '/', "", c.xpath):
                                    groups.append(c)
                                else:
                                    children.append(c)
                            children.extend(groups)
                            # don't add the esp to the group again
                            if esp in children:
                                children.remove(esp)
                            # add all the required fields and other qualifiers to the same group as the initial qualifier
                            for child in children:
                                child_name = re.sub(Output.get_containing_group(esp.xpath) + '/', "", child.xpath)
                                field = Output.add_child(child_name, parent)
                                field.text = child.data + (
                                    "[qualified rep]" if child.is_qualifier() else "") + ' %s ' % str(child.score)
        return etree.tostring(Output.root, pretty_print=True)

    # helper method - checks an individual ESP to see if additional information should be added, and places that and the score in
    # the field's text in xml output
    def add_esp(esp):
        field = Output.parse_xpath(esp.xpath, esp.data)
        txt = ''
        if esp.data is not None and len(esp.data) > 0:
            txt += esp.data
            if esp.is_qualifier():
                txt += "[qualified rep]"
        if esp.has_equals():
            txt += "[equivalent field]"
        txt += ' %s ' % str(esp.score)
        field.text = txt

    # helper method - parses out the xpath string from an ESP and figures out where in the tree the ESP belongs
    # if a child group doesn't exist already, it will create it and add it to the etree
    def parse_xpath(xpath, data):
        node_names = xpath.split('/')
        parent = Output.root
        for name in node_names[2:]:
            if len(name) > 0:
                if parent.find(name) is None:
                    new_child = etree.SubElement(parent, name)

                # if there are multiple qualified reps of the same group, this part will catch them and make sure each
                # one gets created
                elif (name == node_names[-1]) and ((len(data) > 0 and parent.find(name).text is None) or
                                                       (len(data) > 0 and parent.find(
                                                           name).text is not None and not parent.find(
                                                           name).text.startswith(data))):
                    parent = etree.SubElement(parent.getparent(), parent.tag)
                    new_child = etree.SubElement(parent, name)
                parent = parent.find(name)
        return parent

    # helper method specifically for qualified reps - for adding fields to a specific repetition of a group
    def add_child(field_name, parent):
        p = parent
        if '/' in field_name:  # the child is actually a nested group- create or add to the group
            for n in field_name.split('/'):
                if p.find(n) is None:
                    new_child = etree.SubElement(p, n)
                p = p.find(n)
            return p
        else:  # the child is just a field - add the field
            if p.find(field_name) is None:
                new_child = etree.SubElement(p, field_name)
            else:
                new_child = p.find(field_name)
            return new_child

    # helper method to get only the name of a group or field from its string xpath
    def get_field(xpath):
        if '/' in xpath:
            return xpath.split('/')[-1]
        else:
            return xpath

    # helper method to get the string xpath of a field or group's parent
    def get_containing_group(xpath):
        if '/' in xpath:
            group_path = re.sub('/' + Output.get_field(xpath), "", xpath)
            return group_path
        else:
            return xpath
