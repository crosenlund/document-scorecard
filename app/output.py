from lxml import etree
import re
import decimal


def format_text(results, v_data, v_schema, for_download):
    output_string = ""
    # format the data for downloading as a text file
    if for_download:
        for scenarios in results:
            for (scenario, data) in scenarios.items():
                output_string += '******************************\r\n'
                output_string += 'Scenario: %s\r\n\r\n\r\n' % scenario
                for info in data:
                    if 'file_name' in info:
                        output_string += 'Results for: %s\r\n' % info['file_name']
                        output_string += '------------------------------\r\n\r\n'

                    if 'total_score' in info and 'actual_score' in info:
                        try:
                            int(info['total_score'])
                        except ValueError:
                            continue
                        try:
                            int(info['actual_score'])
                        except ValueError:
                            continue
                        score = round((info['actual_score'] / info['total_score']) * 100, 2)
                        output_string += 'Score earned: %r/%r, %r%%\r\n\r\n' % (
                            info['actual_score'], info['total_score'], score)

                    if 'missing_fields' in info and info['missing_fields']:
                        output_string += '---Missing Fields---\r\n'
                        for field in info['missing_fields']:
                            output_string += '(-%r) Missing %s \r\n' % (field[0], field[1])
                        output_string += '\r\n'

                    if 'missing_data' in info and info['missing_data']:
                        output_string += '---Missing/Incorrect Data---\r\n'
                        for field in info['missing_data']:
                            output_string += '(-%r) Missing %s \r\n' % (field[0], field[1])
                        output_string += '\r\n'

                    if 'not_in_schema' in info and info['not_in_schema']:
                        output_string += '---Field Not in Schema---\r\n'
                        for field in info['not_in_schema']:
                            output_string += 'Missing %s \r\n' % field
                        output_string += '\r\n'

                    if 'missing_fields' in info and not info['missing_fields'] and 'not_in_schema' in info and not info[
                        'not_in_schema'] and 'missing_data' in info and not info['missing_data']:
                        output_string += 'No missing fields, data, or qualifiers for this scenario and file'

                    output_string += '\r\n'
                output_string += '\r\n'

    return output_string
