from app import database
import re

ALLOWED_EXTENSIONS = ['txt', 'xml']


# function to check whether a file is a type of file that is acceptable
def file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# change a path like: /MasterItemAttribute[10]/ItemAttributeItem/AttributeQualifier  (many reps of MasterItemAttribute)
#                 to: /MasterItemAttribute/ItemAttributeItem/AttributeQualifier
def clean_xml_path(path):
    return re.sub("\\[\d{1,6}\\]", "", path)


# determine if two paths are the same minus plural root tag if present
# check if the strings are within each other to avoid starting with different root tags
# ie ItemRegistries/ItemRegistry vs ItemRegistry will be the same
def same_path(path1, path2):
    return path1 in path2 or path2 in path1


def scenario_from_xml_to_json(xml, scen):
    scen_list = []

    cur, conn = database.connect_to_db()
    if existing_scenario(id, None):
        cur.execute("SELECT * FROM scenarios where id = '" + str(id) + "'")

        row = cur.fetchone()

        fields_built = build_fields_json(cur, id, False)
        groups_built = build_groups_json(cur, id, False)
        if fields_built:
            if groups_built:
                scen_list.append(
                    {"scenId": id, "rootName": row[6], "groups": build_groups_json(cur, id, False),
                     "fields": build_fields_json(cur, id, False)})
            if not groups_built:
                scen_list.append(
                    {"scenId": id, "rootName": row[6], "fields": build_fields_json(cur, id, False)})

        if not fields_built:
            if groups_built:
                scen_list.append(
                    {"scenId": id, "rootName": row[6], "groups": build_groups_json(cur, id, False),
                     "fields": build_fields_json(cur, id, False)})
            if not groups_built:
                scen_list.append({"scenId": id, "rootName": row[6]})

    database.close(cur, conn)

    if 'row' in locals():
        # return json.dumps(scen_list), ''
        return scen_list, ''
    else:
        return [], 'Unable to retrieve the selected scenario. Please try again or report an issue.'


# helper method building the groups in json for the scenario
def build_groups_json(cur, id, group_fields):
    if group_fields:
        cur.execute("SELECT child_group_id FROM groups_in_groups where parent_group_id = '" + str(id) + "'")
    else:
        cur.execute("SELECT child_group_id FROM groups_in_groups where scenario_id = '" + str(id) + "'")

    groups_to_build = cur.fetchall()

    group_list = []

    for group in groups_to_build:
        group_id = str(group[0])

        build_fields_json(cur, id, True)
        cur.execute(
            "SELECT * FROM groups WHERE id = '" + str(group_id) + "';")
        group_info = cur.fetchone()
        fields_built = build_fields_json(cur, group_id, True)
        groups_built = build_groups_json(cur, group_id, True)
        if fields_built:
            if groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3], "groups": groups_built,
                                   "fields": fields_built})
            if not groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3], "fields": fields_built})

        if not fields_built:
            if groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3], "groups": groups_built})
            if not groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3]})

    return group_list


# helper method building the fields in json for the scenario
def build_fields_json(cur, id, group_field):
    if group_field:
        cur.execute("SELECT field_id FROM fields_in_groups where group_id = '" + str(id) + "'")
    else:
        cur.execute("SELECT field_id FROM fields_in_groups where scenario_id = '" + str(id) + "'")

    fields_to_build = cur.fetchall()

    field_list = []

    for field in fields_to_build:
        field_id = str(field[0])

        cur.execute(
            "SELECT * FROM fields WHERE id = '" + str(field_id) + "';")
        field_info = cur.fetchone()
        field_list.append(
            {"fieldId": field_info[0], "name": field_info[1], "score": field_info[2], "data": field_info[3],
             "not_equal": field_info[4]})

    return field_list


