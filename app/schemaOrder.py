from app import app, schemaCreation
import logging


class order:
    @staticmethod
    def order_xml(_file, schema):
        print(_file)
        print(schema)
        if _file and schema:
            xsd = app.config['SCHEMA_FOLDER'] + '/' + schema + '.xsd'
            print(xsd)
            configure_xsd = True  # schemaCreation.create.configure_xsd(xsd)
            print(configure_xsd)
            if configure_xsd:
                create_schema = schemaCreation.create.create_schema(xsd)
                if create_schema:
                    return order.print_xml(_file)
        return False

    @staticmethod
    def print_xml(xmlfile):
        from app import schemasLayout
        doc = schemasLayout.parsexml_(xmlfile, None)
        rootNode = doc.getroot()
        print(rootNode)
        rootTag, rootClass = schemasLayout.get_root_tag(rootNode)
        print(rootTag, rootClass)
        if rootClass is None:
            print("here!!!!!!!!!!!!!!!")
            from subprocess import check_output
            try:
                # rootTag = 'schema'
                # rootClass = schemasLayout.supermod.shipment
                rootClass = check_output('python %s' % 'schemasLayout.' + rootTag)
            except:
                logging.info("cannot find method/class '" + rootTag + "' in schemaLayout")
            if rootClass is None:
                try:
                    rootClass = check_output('python %s' % 'schemasLayout.' + rootTag + "Type")
                except:
                    logging.info("cannot find method/class '" + rootTag + "Type' in schemaLayout")
            # try:
            #     rootClass = schemasLayout.GDSClassesMapping().get(rootTag + "Type")
            # except:
            #     logging.info("cannot find method/class " + rootTag + "Type in schemaLayout")
            # try:
            #     # rootClass = schemasLayout.GDSClassesMapping().get(rootTag)
            #     rootTag = rootTag
            #     rootClass = schemasLayout.supermod.schemasLayout
            # except:
            #     logging.info("cannot find method/class " + rootTag + " in schemaLayout")
        print(rootTag, rootClass)
        rootObj = rootClass.factory()
        rootObj.build(rootNode)
        # rootObj = schemasLayout.parse(xmlfile, None)
        w = open(app.config['APP_FOLDER'] + '/output.xml', 'w')
        rootObj.export(w, 0, name_=rootTag, namespacedef_='', pretty_print=True)
        w.close()
        return True
