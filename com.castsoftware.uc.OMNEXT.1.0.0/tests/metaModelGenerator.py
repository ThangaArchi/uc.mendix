'''
Created on 08-Nov-2019

@author: TKA
'''



import xlrd 
from Tools.Scripts.ndiff import fopen
from tests.prepareCSV import ReadRules as rRul

if __name__ == '__main__':
  
    loc = ("C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/Mendix_Objects_Rules.xlsx") 
      
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
      
    f = open("OMNEXTMetaModel.xml", "w+")
    f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    f.write("<metaModel file_level=\"client\" file_no=\"103\">\n\n")
    
    f.write("\t<category name=\"APM OMNEXT Module\" rid=\"0\">\n");
    f.write("\t\t<description>OMNEXT</description>\n");
    f.write("\t\t<inheritedCategory name=\"APM Client Modules\" />\n");
    f.write("\t</category>\n");
    
    f.write("\t<category name=\"APM OMNEXT Artifacts\" rid=\"1\">\n");
    f.write("\t\t<description>OMNEXT Artifacts</description>\n");
    f.write("\t\t<inheritedCategory name=\"APM Client Language Artifacts\"/>\n");
    f.write("\t</category>\n");
    
    f.write("\t<type name=\"OMNEXT_Subset\" rid=\"2\">\n");
    f.write("\t\t<description>OMNEXT_Subset</description>\n");
    f.write("\t\t<inheritedCategory name=\"PROJECT_SUBSET\" />\n");
    f.write("\t\t<inheritedCategory name=\"OMNEXT\" />\n");
    f.write("\t\t<inheritedCategory name=\"APM OMNEXT Module\" />\n");
    f.write("\t</type>\n");
    
    f.write("\t<type name=\"EnlightenOMNEXT\" rid=\"3\">\n");
    f.write("\t\t<description>OMNEXT</description>\n");
    f.write("\t\t<tree parent=\"EnlightenUniversalObjects\" category=\"EnlightenTree\" />\n");
    f.write("\t</type>\n\n");
    
    f.write("\t<category name=\"OMNEXT\" rid=\"9\">\n")
    f.write("\t\t<description>OMNEXT</description>\n")
    f.write("\t\t<attribute name=\"extensions\" stringValue=\"*.xml\" />\n")
    f.write("\t\t<inheritedCategory name=\"UniversalLanguage\" />\n")
    f.write("\t\t<inheritedCategory name=\"CsvLanguage\" />\n")
    f.write("\t</category>\n\n")
        
    f.write("\t<type name=\"OMNEXTProject\" rid=\"10\">\n")
    f.write("\t\t<description>OMNEXTProject</description>\n")
    f.write("\t\t<inheritedCategory name=\"UAProject\" />\n")
    f.write("\t\t<inheritedCategory name=\"OMNEXT\" />\n")
    f.write("\t\t<inheritedCategory name=\"APM OMNEXT Module\" />\n")
    f.write("\t</type>\n\n")
    for i in range(sheet.nrows): 
        if i>0:
            artifIDActual = sheet.cell_value(i, 0)
            artifIDManipulated = artifIDActual.replace(" ", "_")
            f.write("\t<type name=\"OMNEXT_"+ artifIDManipulated +"\" rid=\""+ str(i+10) +"\">\n")
            f.write("\t\t<description>"+ artifIDActual +"</description>\n")
            f.write("\t\t<inheritedCategory name=\"OMNEXT\" />\n")
            f.write("\t\t<inheritedCategory name=\"UAObject\" />\n")
            f.write("\t\t<inheritedCategory name=\"APM All Artifacts\" />\n")
            f.write("\t\t<tree parent=\"EnlightenUniversalObjects\" category=\"EnlightenTree\" />\n");
            f.write("\t</type>\n")
            
        print(i , sheet.cell_value(i, 0)) 
        
    f.write("</metaModel>")
    f.close()
    
    
