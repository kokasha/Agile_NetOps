import jxmlease

class FilterModule(object):

    def parse_junos_xml(self,xml_data):
        json_parse = jxmlease.parse(xml_data)
        return json_parse

    def filters(self):
        return {'parse_junos_xml': self.parse_junos_xml}
