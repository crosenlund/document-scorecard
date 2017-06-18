from lxml import etree
import re
import decimal


def format_text(results, v_data, v_schema, for_download):
    output_string = ""
    # format the data for downloading as a text file
    if for_download:
        for scenarios in results:
            for (scenario, data) in scenarios.items():
                output_string += '************************************************************************************************************************\r\n'
                output_string += 'Scenario: %s\r\n\r\n\r\n' % scenario
                for info in data:
                    design_score_string = ""
                    if 'file_name' in info:
                        output_string += 'Results for: %s\r\n' % info['file_name']
                        output_string += '------------------------------------------------------------\r\n\r\n'

                    if 'total_score' in info and 'actual_score' in info:
                        score_percent = 0.0
                        try:
                            int(info['total_score'])
                            int(info['actual_score'])
                            score_percent = round((info['actual_score'] / info['total_score']) * 100, 2)
                        except ValueError:
                            None

                        output_string += 'Score earned: %r/%r, %r%%\r\n\r\n' % (
                            info['actual_score'], info['total_score'], score_percent)

                    # ---------------------------------- MISSING FIELDS ------------------------------------------------
                    if 'missing_fields' in info and info['missing_fields']:
                        output_string += '---Missing Fields---\r\n'
                        design_string_array = []
                        for field in info['missing_fields']:
                            output_string += '(-%r) Missing %s\r\n' % (field[0], field[1])

                            # Output for DESIGN SCORE function-----------------------------------------------
                            design_string = field[1].split('/')[-1]
                            if ': requires one of ' in design_string:
                                design_string_after_colon = design_string.split(": requires one of ")[1]
                                design_string_after_colon = design_string_after_colon.replace("[", "")
                                design_string_after_colon = design_string_after_colon.replace("]", "")
                                design_string_after_colon = design_string_after_colon.replace("'", "")
                                design_string_after_colon = design_string_after_colon.replace(" ", "")
                                design_string = design_string_after_colon.split(",")
                                for element in design_string:
                                    if element not in design_string_array:
                                        design_string_array.append(element)
                                        design_score_string += '%s\r\n' % element
                            elif ' with ' in field[1]:
                                design_string = field[1].split(" with ")[0].split('/')[-1]
                                if design_string not in design_string_array:
                                    design_string_array.append(design_string)
                                    design_score_string += '%s\r\n' % design_string
                            elif ' = ' in design_string:
                                design_string = design_string.split(" = ")[0]
                                if design_string not in design_string_array:
                                    design_string_array.append(design_string)
                                    design_score_string += '%s\r\n' % design_string.split(" = ")[0]
                            else:
                                design_string = field[1].split('/')[-1]
                                if design_string not in design_string_array:
                                    design_string_array.append(design_string)
                                    design_score_string += '%s\r\n' % field[1].split('/')[-1]

                        output_string += '\r\n'

                    # ----------------------------------- MISSING DATA -------------------------------------------------
                    if 'missing_data' in info and info['missing_data']:
                        output_string += '---Missing/Incorrect Data---\r\n'
                        for field in info['missing_data']:
                            output_string += '(-%r) Missing %s\r\n' % (field[0], field[1])
                        output_string += '\r\n'

                    # ----------------------------------- NOT IN SCHEMA ------------------------------------------------
                    if 'not_in_schema' in info and info['not_in_schema']:
                        output_string += '---Field Not in Schema---\r\n'
                        for field in info['not_in_schema']:
                            output_string += 'Missing %s\r\n' % field
                        output_string += '\r\n'

                    # -------------------------------------- ERRORS ----------------------------------------------------
                    if 'errors' in info and info['errors']:
                        output_string += '---Errors processing---\r\n'
                        for error in info['errors']:
                            output_string += 'Error: %s\r\n' % error
                        output_string += '\r\n'

                    if 'missing_fields' in info and not info['missing_fields'] and 'not_in_schema' in info and not info[
                        'not_in_schema'] and 'missing_data' in info and not info['missing_data']:
                        output_string += 'No missing fields, data, or qualifiers for this scenario and file'

                    if design_score_string:
                        output_string += '\r\n---Design Score---\r\n'
                        output_string += design_score_string

                    output_string += '\r\n'
                output_string += '\r\n'

    return output_string
