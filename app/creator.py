import logging

from app import groups

from app import scenarios


# add the scenario to the database
def build_scenario(scenario_info, scenario_data):
    root_name = ''
    scen_name = ''
    description = ''
    fulfillment_type = ''
    schema_name = ''
    doc_type = ''
    date_created = ''
    print(scenario_info)

    # parsing the scenario_info so that we can add a scenario using the info later
    for (v, info) in scenario_info.items():
        if v == 'rootName':
            root_name = info
        if v == 'name':
            scen_name = info
        if v == 'description':
            description = info
        if v == 'fulfillmentType':
            fulfillment_type = info
        if v == 'schemaName':
            schema_name = info
        if v == 'docType':
            doc_type = info
        if v == 'datecreated':
            date_created = info

    # when creating a scenario from a file
    if scenario_data:
        # if the root_node in the data is the root we are looking for
        if scenario_data['rootName'] == root_name:
            logging.info("(find_root) found %s in %r", root_name, scenario_data)
        else:  # if not, go find it
            scenario_data = find_root(root_name, scenario_data)
        # if it doesn't exist, error
        if not scenario_data:
            logging.info("Error, could not find the correct starting root node that was indicated (rootName)")
            return '', "Error, could not find the correct starting root node that was indicated (rootName)"

        # now add the scenario to the database
        scen_id = scenarios.add_scenario(scen_name, description, doc_type, fulfillment_type, schema_name, root_name, date_created)
        # confirm scenario table row added
        # scen_id = 1
        if scen_id is not -1:
            if 'fields' in scenario_data:
                create_fields(scen_id, None, scenario_data['fields'])

            if 'groups' in scenario_data:
                create_groups(scen_id, None, scenario_data['groups'])
    # when creating a blank scenario
    else:
        scen_id = scenarios.add_scenario(scen_name, description, doc_type, fulfillment_type, schema_name, root_name, None)

    if scen_id is not -1:
        # successfully created the scenario if this point is reached
        return True, ''
    else:
        # Something went wrong
        logging.info("There was an error creating a scenario, please check that the name does not duplicate.")
        return False, 'There was an error creating a scenario, please check that the name does not duplicate.'


# This method is used to find the correct root node to build a scenario from. If the scenario file sent starts with the
# plural (ex. Orders) and we want the scenario root to be the singular (ex. Order).
# It returns new data to build a scenario from.
def find_root(root_name, scenario_data):
    try:
        if 'groups' in scenario_data:
            _groups = scenario_data['groups']
            for group in _groups:
                for (v, info) in group.items():
                    if v == 'name':
                        print(info)
                        if info == root_name:
                            logging.info("(find_root) found %s in %r", root_name, scenario_data)
                            return group
                        else:
                            found_group = find_root(root_name, group)
                            if found_group:
                                logging.info("(find_root) found %s in %r", root_name, scenario_data)
                                return found_group  # only return the group (new root) if it is found, else keep looking
        return None  #
    except KeyError:
        logging.info("(find_root) unable to find 'groups' in %r", scenario_data)


# this is the recursive method to add the scenario to the database.
# It will call method create_fields to create new fields for this group
def create_groups(scenario_id, group_id, groups_data):
    for g in groups_data:
        name = g['name']  # name will always be sent
        if 'qualifier_data' in g:
            qualifier_data = g['qualifier_data']
        else:
            qualifier_data = ''
        if 'qualifier' in g:
            qualifier = g['qualifier']
        else:
            qualifier = ''

        # create the group from the information gathered above
        # add the group to another group if group_id is present
        if group_id:
            new_group_id = groups.add_group(group_id, name, qualifier, qualifier_data)
            logging.info("adding group " + name + " to group " + str(new_group_id))
        # else add the group to the scenario if scenario_id is present
        elif scenario_id:
            new_group_id = scenarios.add_group(scenario_id, name, qualifier, qualifier_data)
            logging.info("adding group " + name + " to scenario " + str(scenario_id))

        if 'fields' in g:
            create_fields(None, new_group_id, g['fields'])
        if 'groups' in g:
            create_groups(None, new_group_id, g['groups'])


# This method creates a field and adds it to a group/scenario
def create_fields(scenario_id, group_id, fields_data):
    # create a new field for each field in the passed data
    for f in fields_data:
        # name will always be sent
        name = f['name']
        # score will always be sent
        score = f['score']
        if 'data' in f:
            data = f['data']
        else:
            data = ''
        if 'not_equal' in f:
            not_equal = f['not_equal']
        else:
            not_equal = ''

        # create a new field based on the above information
        # add to the group if group_id has data
        if group_id:
            groups.add_field(group_id, name, score, data, not_equal)
            logging.info("adding field " + name + " to group " + str(group_id))
        # else add to the scenario if scenario_id has data
        elif scenario_id:
            scenarios.add_field(scenario_id, name, score, data, not_equal)
            logging.info("adding field " + name + " to scenario " + str(scenario_id))


# add the copied scenario to the database
def copy_scenario(scen_id, scenario_data):
    # check that the scenario to the database
    if scenarios.existing_scenario(scen_id, None):
        if 'fields' in scenario_data:
            create_fields(scen_id, None, scenario_data['fields'])

        if 'groups' in scenario_data:
            create_groups(scen_id, None, scenario_data['groups'])

        # successfully created the scenario if this point is reached
        return True, ''
    else:
        # Something went wrong
        logging.info("There was an error creating a scenario, please check that the name does not duplicate.")
        return False, 'There was an error creating a scenario, please check that the name does not duplicate.'

