'''
Created on 08-Nov-2019

@author: TKA
'''



import xml.etree.cElementTree as ET
import xlrd 
from Tools.Scripts.ndiff import fopen

if __name__ == '__main__':
        
    xmlVer = ET.Element("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")
    f = open("OMNEXTLanguagePattern.xml", "w+")
    f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    f.write("<languagePattern id=\"OMNEXT\">\n\n")
    f.write("</languagePattern>")
    f.close()
