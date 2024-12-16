from xml.dom import minidom
#from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET

doc = minidom.parse('./data.xml')

print(doc)

items = doc.getElementsByTagName('item')

print('A #2 elem attribuuma:')
print(items[1].attributes['name'].value)

print('Az osszes attributum')
for item in items:
    print(item.attributes['name'].value)

print('A #2 elem adata:')
print(items[1].firstChild.data)
print(items[1].childNodes[0])

for item in items:
    print(item.firstChild.data)


#tree = ElementTree()
#tree.parse('./data.xml')
tree = ET.parse('./data.xml')
root = tree.getroot()

print('A #2 elem attribuuma ET-vel:')
print(root[0][1].attrib)

print('Az osszes attributum ET-vel')
for item in root:
    for sub_item in item:
        print(sub_item.attrib)


print('A #2 elem adata ET-vel:')
print(root[0][1].text)

for item in root:
    for sub_item in item:
        print(sub_item.text)


data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name', 'elem1')
item2.set('name', 'elem2')
item1.text = 'Adat1'
item2.text = 'Adat2'

export_data = ET.tostring(data, encoding='unicode')
print(export_data)

with open('./data2.xml', 'w', encoding='utf-8') as file:
    file.write(export_data)

for item in root:
    print(item.find('item').get('name')) # az elsőt írja ki

for i in root:
    print(i.findall('item'))
    for item in i.findall('item'):
        print(item.attrib)


tree = ET.parse('./data2.xml')
root = tree.getroot()

for item in root.iter('item'):
    item.text = 'Modositva!'
    item.set('age', '33')

tree.write('./data2.xml', encoding='utf-8')