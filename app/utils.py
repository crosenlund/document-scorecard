from lxml import etree
ALLOWED_EXTENSIONS = ['txt', 'xml']


# function to check whether a file is a type of file that is acceptable
def file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_scenario_as_xml_tree(scenario_data):
    scenario_data = scenario_data[0]
    if scenario_data:
        root = scenario_data['rootName']
        print(scenario_data)
        print(root)
        rootNode = etree.Element(root)
        print(rootNode)
        tree = etree.ElementTree(rootNode)
        print(tree)
        rootNode2 = etree.Element("here")
        rootNode2.text = 'text-data'
        node = rootNode.append(rootNode2)
        return etree.tostring(rootNode, pretty_print=True), ''
    else:
        return None, 'Issue getting the scenario as XML'


