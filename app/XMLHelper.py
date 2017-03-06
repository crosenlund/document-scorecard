from lxml.etree import XMLSyntaxError
from lxml import etree
import re
import logging


# add a score attribute to every field, score defaults to 1 unless user specifies one
def add_scores(file_name, default_score):
    score = 1
    if default_score:
        score = default_score

    with open(file_name) as xml_file:
        parsing = etree.XMLParser(ns_clean=True)
        try:
            data_tree = etree.parse(xml_file, parsing)
        except XMLSyntaxError:
            #TODO insert help page
            return '', 'There was a problem parsing %s. Please report a bug if issue cannot be resolved from the' \
                       ' following: ( TODO: insert web link to help page)' % file_name

    # remove the namespace from the nodes' tag/name
    nodes = data_tree.iter()
    for node in nodes:
        # give every field a 'score' attribute = variable score
        if len(node) < 1:
            node.set('score', str(score))

    return etree.tostring(data_tree, pretty_print=True), ''
