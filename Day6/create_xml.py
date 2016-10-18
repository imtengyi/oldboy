#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name_1 = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name_1,"age",attrib={"checked":"no"})
sex = ET.SubElement(name_1,"sex")
sex.text = '33'
name_2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name_2,"age")
age.text = '19'

et = ET.ElementTree(new_xml)
et.write("new_xml.xml",encoding="utf-8",xml_declaration=True)

ET.dump(new_xml)