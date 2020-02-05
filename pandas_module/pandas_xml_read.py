import xml.etree.ElementTree as ET

mytree = ET.parse( 'readable.xml' )
# parse as string frmt
myroot = mytree.getroot()
print( myroot.tag )
print( myroot[0].attrib )
for x in myroot[0]:
    print( x.tag, x.attrib )
for x in myroot[0]:
    print( x.text )
for x in myroot.findall( 'food' ):
    item = x.find( 'item' ).text
    price = x.find( 'price' ).text
    print( item, price )
for x in myroot.iter( 'description' ):
    a = str( x.text ) + "description has been added"
    x.text = str( a )
    x.set( 'update', 'yes' )
# mytree.write('new.xml')
myroot[0][0].attrib.pop( 'name' )
mytree.
