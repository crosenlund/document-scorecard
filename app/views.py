# from application.app import scenarios, app, parse, creator, utils
import os
import logging
from app import app, scenarios, groups, fields, utilities, parse, creator, schemaUtilities, output, compare
from flask import render_template, redirect, url_for, request, make_response, Response, json
from werkzeug import secure_filename
import time

ALLOWED_EXTENSIONS = ['txt', 'xml']


# load main page
@app.route('/')
@app.route('/index')
def documentscorecard_index():
    return render_template("index.html", scenarios=get_scenario_list())


# returns a list of all the scenarios (name, id, schema...) in the database in json form
@app.route('/get_scenario_list', methods=['GET'])
def get_scenario_list():
    return Response(json.dumps(scenarios.get_all_scenarios()), mimetype='application/json')


# accepts an uploded file and parses it into a new scenario with the passed information
@app.route('/upload_new_scenario', methods=['POST'])
def upload_new_scenario():
    if request.method == 'POST':
        file = request.files['file']
        data = json.loads(request.form['data'])
        error = ''
        scenario_data = []
        is_valid = False

        if file:
            if utilities.file_allowed(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                scenario_data, new_error = parse.new_scenario(app.config['UPLOAD_FOLDER'] + '/' + filename)
                if scenario_data:
                    is_valid = True
                else:
                    error += new_error
            else:
                error += 'File extension is not allowed.'
        else:
            error += "A file must be uploaded to create a new scenario."

        if is_valid:  # scenario was successfully parsed
            created_scenario, new_error = creator.build_scenario(data, scenario_data)

            if new_error:
                error += new_error
        if len(error) < 1:
            return get_scenario_list()
        else:
            response = make_response(error, 400)
            return response


# delete a scenario if it exists
@app.route('/delete_scenario', methods=['POST'])
def delete_scenario():
    if request.method == 'POST':
        scen_id = request.json['scenID']
        success, error = scenarios.delete_scenario(scen_id)
        if success:
            logging.info("Scenario " + str(scen_id) + " was successfully deleted.")
            return get_scenario_list()
        else:
            return make_response("Unable to deleted scenario " + str(scen_id) + ".", 400)


# copy a scenario that already exists, name must change others are optional
@app.route('/copy_scenario', methods=['POST'])
def copy_scenario():
    if request.method == 'POST':
        scen_id = request.json['scenID']
        scen_name = request.json['scenName']
        success, error = scenarios.copy_scenario(scen_id, scen_name)
        if success:
            logging.info("Scenario " + str(scen_id) + " was successfully copied.")
            return get_scenario_list()
        else:
            return make_response("Unable to copy scenario (" + str(scen_id) + ").  " + error + "", 400)


# renames a scenario that already exists
@app.route('/edit_scenario', methods=['POST'])
def edit_scenario():
    if request.method == 'POST':
        scen_id = request.json['scenID']
        name = request.json['name']
        current_name, error = scenarios.get_info(scen_id)
        current_name = current_name[1]
        if name == current_name:
            same_name = True
        else:
            same_name = False
        schema = request.json['schema']
        description = request.json['description']
        doc_type = request.json['docType']
        root_name = request.json['rootName']
        fulfillment_type = request.json['fulfillmentType']
        success, error = scenarios.edit_scenario(scen_id, name, description, doc_type, fulfillment_type, schema,
                                                 root_name, same_name)
        if success:
            logging.info("Scenario %s was successfully updated(%s, %s, %s, %s, %s, %s)." % (
                scen_id, name, description, doc_type, fulfillment_type, schema, root_name))
            return get_scenario_list()
        else:
            response = make_response(error, 400)
            return response


# returns json of a scenario
@app.route('/get_scenario_json', methods=['POST'])
def get_scenario_json():
    if request.method == 'POST':
        scenario_data = ''
        scen_id = request.json['scenID']

        return scenario_json(scen_id)


# returns json of a scenario
def scenario_json(scen_id):
    scenario_data = ''

    if scenarios.existing_scenario(scen_id, None):
        scenario_data, error = scenarios.to_json(scen_id)
    else:
        error = "That scenario does not exist."
    if len(error) < 1:
        return Response(json.dumps(scenario_data), mimetype='application/json')
    else:
        response = make_response(error, 400)
        return response


# returns XML of a scenario
@app.route('/get_scenario_xml', methods=['POST'])
def get_scenario_xml():
    start_time = time.time()
    if request.method == 'POST':
        scen_id = request.json['id']
        scen_name = request.json['name']
        schema = request.json['schema']
        # validate_to_schema = request.json['validateSchema']
        validate_to_schema = True
        xml_string, error = scenarios.to_xml(scen_id)
        print(xml_string)
        with open(app.config['APP_FOLDER'] + '/output.xml', 'wb') as w:
            w.write(xml_string)

        if schema is not None and validate_to_schema:
            schemaUtilities.order_xml(app.config['APP_FOLDER'] + '/output.xml', schema)

        with open(app.config['APP_FOLDER'] + '/output.xml', 'r') as r:
            xml_string = r.read()
            print(xml_string)
        print('get_scenario_xml took %s seconds' % (time.time() - start_time))
        if error:
            response = make_response(error, 400)
            return response
        else:
            response = make_response(xml_string)
            response.headers["Content-Disposition"] = "attachment;filename=%s.xml" % scen_name
            return response


@app.route('/compare_download', methods=['POST'])
def compare_download():
    start_time = time.time()
    if request.method == 'POST':
        files = []
        for file in request.files.getlist("file"):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            files.append(filename)
        data = json.loads(request.form['data'])
        selected_list = data['testList']
        validate_to_schema = data['validateSchema']
        validate_to_data = data['validateData']
        scenarios_list = selected_list.split(',')
        error = ''

        if files and selected_list:
            compare.compare(files, scenarios_list, validate_to_data, validate_to_schema)
        else:
            response = make_response("Unable to find files and/or scenarios selected", 400)
            return response

        response = make_response("compare and download output", 200)
        # response = make_response(scenarios_list)
        # response.headers["Content-Disposition"] = "attachment;filename=%s.txt" % scen_name
        return response


# --------------------EDITING SCENARIO'S GROUPS AND FIELDS FROM WEBSITE----------
@app.route('/add_group', methods=['POST'])
def add_group():
    if request.method == 'POST':
        scen_id_for_json = request.json['scenID2']
        group_id = ''
        if 'groupID' in request.json:
            group_id = request.json['groupID']
        scen_id = ''
        if 'scenID' in request.json:
            scen_id = request.json['scenID']
        group_name = request.json['newGroupName']
        qualifier_value = ''
        if 'qualifier_value' in request.json:
            qualifier_value = request.json['qualifier_value']
        qualifier_field = ''
        if 'qualifier_field' in request.json:
            qualifier_field = request.json['qualifier_field']

        if scen_id:
            success = scenarios.add_group(scen_id, group_name, qualifier_value, qualifier_field)
        elif group_id:
            success = groups.add_group(group_id, group_name, qualifier_value, qualifier_field)

        if success:
            logging.info("successfully added group '" + group_name + "' (scenario id = " + str(scen_id) + ", " +
                         " " + group_name + ", " + qualifier_value + "," + qualifier_field + ")")

            return scenario_json(scen_id_for_json)
        else:
            response = make_response('Unable to add a new group. If unable to resolve, please report error/bug.', 400)
            return response


@app.route('/add_field', methods=['POST'])
def add_field():
    if request.method == 'POST':
        scen_id_for_json = request.json['scenID2']
        field_name = request.json['fieldName']
        score = request.json['score']
        data = request.json['data']
        notEqual = request.json['notEqual']
        if 'groupID' in request.json:
            group_id = request.json['groupID']
        scen_id = ''
        if 'scenID' in request.json:
            scen_id = request.json['scenID']
        group_name = request.json['newGroupName']
        qualifier_value = ''
        if 'qualifier_value' in request.json:
            qualifier_value = request.json['qualifier_value']
        qualifier_field = ''
        if 'qualifier_field' in request.json:
            qualifier_field = request.json['qualifier_field']

        success = False
        if scen_id:
            success = scenarios.add_group(scen_id, group_name, qualifier_value, qualifier_field)
        elif group_id:
            success = groups.add_group(group_id, group_name, qualifier_value, qualifier_field)

        if success:
            logging.info("successfully added group '" + group_name + "' (scenario id = " + str(scen_id) + ", " +
                         " " + group_name + ", " + qualifier_value + "," + qualifier_field + ")")

            return scenario_json(scen_id_for_json)
        else:
            response = make_response('Unable to add a new group. If unable to resolve, please report error/bug.', 400)
            return response


@app.route('/remove_group', methods=['POST'])
def remove_group():
    if request.method == 'POST':
        group_id = request.json['groupID']
        scen_id_for_json = request.json['scenID2']

        success = groups.delete_group(group_id)

        if success:
            logging.info("successfully deleted group with id = '" + str(group_id) + "' from scenario with id = '" + str(
                scen_id_for_json) + "'")
            return scenario_json(scen_id_for_json)
        else:
            response = make_response(
                'Unable to remove the group. If unable to resolve, please report error/bug.', 400)
            return response


@app.route('/edit_group', methods=['POST'])
def edit_group():
    if request.method == 'POST':
        scen_id_for_json = request.json['scenID2']
        group_id = ''
        if 'groupID' in request.json:
            group_id = request.json['groupID']
        group_name = request.json['newGroupName']
        current_name = request.json['name']
        qualifier_value = ''
        if 'qualifier_value' in request.json:
            qualifier_value = request.json['qualifier_value']
        qualifier_field = ''
        if 'qualifier_field' in request.json:
            qualifier_field = request.json['qualifier_field']

        success = groups.edit_group(group_id, group_name, qualifier_value, qualifier_field)

        if success:
            logging.info(
                "successfully edited group with id = '" + str(group_id) + "'(scenario id = " + str(
                    scen_id_for_json) + ", " + " " + group_name + ", " + qualifier_value + "," + qualifier_field + ")")

            return scenario_json(scen_id_for_json)
        else:
            response = make_response(
                'Unable to edit the group. If unable to resolve, please report error/bug.', 400)
            return response


# --------------------SCHEMA VALIDATION------------------------------------------
@app.route('/get_schema_list', methods=['GET'])
def get_schema_list():
    return json.dumps(schemaUtilities.get_schema_list())


@app.route('/add_schema', methods=['POST'])
def add_schema():
    if request.method == 'POST':
        file = request.files['file']
        data = json.loads(request.form['data'])
        schema_name = data['schema']
        error = ''
        if file:
            # if this is empty, schema was successfully added
            error = schemaUtilities.add_schema(file, schema_name)
        else:
            error = "A schema must be upload."
        if len(error) > 0:
            return make_response(error, 400)
        return get_schema_list()


@app.route('/delete_schema', methods=['POST'])
def delete_schema():
    filename = request.json['delete']
    # if this is empty, schema was successfully deleted
    error = schemaUtilities.delete_schema(filename)
    if len(error) > 0:
        return make_response(error, 400)
    return get_schema_list()
