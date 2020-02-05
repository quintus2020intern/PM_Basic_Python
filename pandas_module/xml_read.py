import xml.etree.ElementTree as ET

mytree = ET.parse( 'xml1.xml' )
# parse as string frmt
myroot = mytree.getroot()
print( myroot.tag )
print( myroot[0].attrib )
for x in myroot[0]:
    print( x.tag, x.attrib )

# data='''
# ?xml version="1.0" encoding="UTF-8"?>
# <metadata>
#     <note>
#         <to>Tove</to>
#         <from>Jani</from>
#         <heading>Reminder</heading>
#         <body>Don't forget me this weekend!</body>
#     </note>
# </metadata>
# '''
# myroot=ET.fromstring(data)
# print(myroot.tag)
