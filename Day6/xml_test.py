#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
	print(root.tag,child.attrib)
	for i in child:
		print("--->",i.tag,i.text)

#只遍历year节点
for node in root.iter('year'):
	print(node.tag,node.text)

#修改内容
for node in root.iter('year'):
	new_year = int(node.text) + 1
	node.text = str(new_year)
	node.set("updated","yes")
tree.write("test.xml")

#删除node
for country in root.findall('country'):
	rank = int(country.find('rank').text)
	if rank > 50:
		root.remove(country)
tree.write('output.xml')