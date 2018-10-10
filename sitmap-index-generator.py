import datetime
import xml.etree.cElementTree as ET
from xml.dom import minidom

#get today's date in yyyy-mm-dd format
date = datetime.datetime.now().strftime('%Y-%m-%d')

#list of site locales
sites = ["gb","de","it","es","fr","me","cn","hk"]

#loop through list of locales creating xml structure
root = ET.Element("sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for x in sites:
    doc = ET.SubElement(root, "sitemap")

    ET.SubElement(doc, "loc").text = "http://www.example.com/sitemap-"+x+".xml"
    ET.SubElement(doc, "lastmod").text = date

tree = ET.ElementTree(root)

#beutify xml
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("sitemap-index.xml", "w") as file:
    file.write(xmlstr)
