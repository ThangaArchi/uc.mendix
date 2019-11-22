'''
Created on 12-Nov-2019

@author: TKA
'''
import csv
import xlrd
from cast.application import open_source_file # @UnresolvedImport
import shutil
import xml.etree.cElementTree as ET
from distutils.tests.test_install_scripts import InstallScriptsTestCase
from tests.GeneratorConfiguration import ExtensionConfiguration as configr
import os


class ReadRules(object):
    '''
    classdocs
    '''
    
    

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def createMetaModelWithArtifacts(self, filName, loc, langID, metaModel_fileNo, metricsCategoryName):
          
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0) 
        sheet.cell_value(0, 0) 
          
        f = open(filName, "w+")
        f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        f.write("<metaModel file_level=\"client\" file_no=\""+ metaModel_fileNo +"\">\n\n")
        
        f.write("\t<category name=\"APM Mendix Module\" rid=\"0\">\n");
        f.write("\t\t<description>Mendix</description>\n");
        f.write("\t\t<inheritedCategory name=\"APM Client Modules\" />\n");
        f.write("\t</category>\n");
        
        f.write("\t<category name=\"APM Mendix Artifacts\" rid=\"1\">\n");
        f.write("\t\t<description>Mendix Artifacts</description>\n");
        f.write("\t\t<inheritedCategory name=\"APM Client Language Artifacts\"/>\n");
        f.write("\t</category>\n");
        
        f.write("\t<type name=\"Mendix_Subset\" rid=\"2\">\n");
        f.write("\t\t<description>Mendix_Subset</description>\n");
        f.write("\t\t<inheritedCategory name=\"PROJECT_SUBSET\" />\n");
        f.write("\t\t<inheritedCategory name=\"Mendix\" />\n");
        f.write("\t\t<inheritedCategory name=\"APM Mendix Module\" />\n");
        f.write("\t</type>\n");
        
#        f.write("\t<type name=\"EnlightenMendix\" rid=\"3\">\n");
#        f.write("\t\t<description>Mendix</description>\n");
#        f.write("\t\t<tree parent=\"EnlightenUniversalObjects\" category=\"EnlightenTree\" />\n");
#        f.write("\t</type>\n\n");
        
        f.write("\t<category name=\"Mendix\" rid=\"9\">\n")
        f.write("\t\t<description>Mendix</description>\n")
        f.write("\t\t<attribute name=\"extensions\" stringValue=\"*.xml\" />\n")
        f.write("\t\t<inheritedCategory name=\"UniversalLanguage\" />\n")
        f.write("\t\t<inheritedCategory name=\"CsvLanguage\" />\n")
        f.write("\t</category>\n\n")
            
        f.write("\t<type name=\"MendixProject\" rid=\"10\">\n")
        f.write("\t\t<description>MendixProject</description>\n")
        f.write("\t\t<inheritedCategory name=\"UAProject\" />\n")
        f.write("\t\t<inheritedCategory name=\"Mendix\" />\n")
        f.write("\t\t<inheritedCategory name=\"APM Mendix Module\" />\n")
        f.write("\t</type>\n\n")
        print()
        for i in range(sheet.nrows): 
            if i>0:
                artifIDActual = sheet.cell_value(i, 0)
                artifIDManipulated = artifIDActual.replace(" ", "_")
                f.write("\t<type name=\""+ langID +"_"+ artifIDManipulated +"\" rid=\""+ str(i+10) +"\">\n")
                f.write("\t\t<description>"+ artifIDActual +"</description>\n")
                f.write("\t\t<inheritedCategory name=\"Mendix\" />\n")
                f.write("\t\t<inheritedCategory name=\"UAObject\" />\n")
                f.write("\t\t<inheritedCategory name=\"APM All Artifacts\" />\n")
                f.write("\t\t<inheritedCategory name=\""+ metricsCategoryName +"\" />\n")
                
                f.write("\t\t<tree parent=\"EnlightenUniversalObjects\" category=\"EnlightenTree\" />\n");
                f.write("\t</type>\n")
                
#            print(i , sheet.cell_value(i, 0)) 
            
        f.write("</metaModel>")
        f.close()
        print("MetaModel file created as [", filName ,"] with Artifacts...!")
        
        
    def createLanguagePattern(self, filName, langID):
        xmlVer = ET.Element("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
        root = ET.Element("root")
        doc = ET.SubElement(root, "doc")
        f = open(filName, "w+")
        f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        f.write("<languagePattern id=\""+ langID +"\">\n\n")
        f.write("</languagePattern>")
        f.close()
        print("LanguagePattern file created as [", filName ,"]...!")
    
        
        
    def prepareCSVs(self, loc, csv_filename, destinationToCopy):
        print("Preparing CSVs using [prepareCSVs()]")
#        loc = ("C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.Mendix.1.0.0/tests/Mendix_Objects_Rules.xlsx") 

#        csv_filename = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_003.csv"   
             
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(1) 
        sheet.cell_value(0, 0) 
    
        with open(csv_filename, 'w', newline='') as csvfile: 
            fieldnames = ['ApplicationName', 'Severity', 'AffectedSource', 'AffectedSourceLine', 'object_id', 'MasterFindingName']
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
            
            writer.writeheader()
            for i in range(sheet.nrows): 
                if i>0:
                    mappedArtifact = sheet.cell_value(i, 0)
                    ruleName = sheet.cell_value(i, 1)
                    ruleDescription = sheet.cell_value(i, 2)
#                    print(i , mappedArtifact, ruleName, ruleDescription) 
                    
                    ruleName = ruleName.lstrip()
                    ruleName = ruleName.rstrip()
                    ruleName = ruleName.replace(" ", "_")
        
                    writer.writerow({'ApplicationName': 'Mendix', 'Severity': '1', 'AffectedSource': '1', 'AffectedSourceLine': '1', 'object_id': '1', 'MasterFindingName': ruleName })
        csvfile.close()
        
#        destinationToCopy = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.labs.3rdparty.csv.integration.2.2.0/generators/Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_003.csv"
        shutil.copyfile(csv_filename, destinationToCopy)
        print("CSV generted as ", csv_filename, " Copied into ["+ destinationToCopy +"]")
        
        
    def generateInstallCommonADGConfigDataModel(self, fromRangeID, toRangeID):        
#        f = open(templateFile,'r')
#        filedata = f.read()
#        f.close()
#        newdata = filedata.replace("{{FROM-RANGE-ID TO-RANGE-ID}}", str(fromRangeID)+" "+str(toRangeID) )        
#        f = open(dataFile,'w')
#        f.write(newdata)
#        f.close() 
        templateFile = configr.installScriptsTemplatePath + "/Common/ADG/ADG_ConfigDataModelTemplate.xml"      
        dataFile     = configr.installScriptsDataPath + "/Common/ADG/ADG_ConfigDataModel.xml"      
        ReadRules.processDataFile("", templateFile, dataFile, "{{FROM-RANGE-ID TO-RANGE-ID}}", str(fromRangeID)+" "+str(toRangeID))
        print("[/Common/ADG/ADG_ConfigDataModel.xml] has been generated successfully with RangeID [", fromRangeID, " TO ", toRangeID ,"]" )
       
    
    def generateInstallCommonDIAGTableDefintion(self, fromRangeID, toRangeID):
        templateFile = configr.installScriptsTemplatePath + "/Common/DIAG/set_tablesTemplate.xml"
        dataFile     = configr.installScriptsDataPath + "/Common/DIAG/set_tables.xml"
        ReadRules.processDataFile("", templateFile, dataFile, "{{FROM-RANGE-ID TO-RANGE-ID}}", str(fromRangeID)+" "+str(toRangeID))
        print("[/Common/DIAG/set_tables.xml] has been generated successfully with RangeID [", fromRangeID, " TO ", toRangeID ,"]" )
        
    def generateInstallCommonDIAGLocalPackageTemplate(self,  clientAppName):
        templateFile = configr.installScriptsTemplatePath + "/Common/DIAG/localTemplate.pck"
        dataFile     = configr.installScriptsDataPath + "/Common/DIAG/local.pck"
        ReadRules.processDataFile("", templateFile, dataFile, "{{CLIENT_APP_NAME}}", clientAppName)
        print("[/Common/DIAG/local.pck] has been generated successfully with CLIENT APPLICATION NAME [", clientAppName ,"]")
        
        
    def generateInstallCommonADGMetricTreeTemplate(self, clientAppName):        
        templateFile = configr.installScriptsTemplatePath + "/Common/ADG/ADG_MetricTreeTemplate.pck"
        dataFile     = configr.installScriptsDataPath + "/Common/ADG/ADG_MetricTree.pck"
        ReadRules.processDataFile("", templateFile, dataFile, "{{CLIENT_APP_NAME}}", clientAppName)
        print("[/Common/ADG/ADG_MetricTree.pck] has been generated successfully with CLIENT APPLICATION NAME [", clientAppName ,"]")
        
    def generateInstallCommonDIAGSqlSetDefinitionTemplate(self, fromRangeID, functionName):  
        
        procedureName = functionName+"_"+str(fromRangeID)
        templateFile = configr.installScriptsTemplatePath + "/Common/DIAG/set_dataTemplate.xml"
        dataFile     = configr.installScriptsDataPath + "/Common/DIAG/set_data.xml"
        ReadRules.processDataFile("", templateFile, dataFile, "{{FROM-RANGE-ID}}", str(fromRangeID) )
        ReadRules.processDataFile("", dataFile, dataFile, "{{FUNCTION-NAME}}", functionName)
        ReadRules.processDataFile("", dataFile, dataFile, "{{FUNCTION-NAME_FROM-RANGE-ID}}", procedureName)
        print("[", dataFile ,"] has been generated successfully with [", fromRangeID ,",", functionName ,",", procedureName ,"]")
        
    def generateInstallCastStorageServiceDIAGSqlFunctionTemplate(self, fromRangeID, functionName, metricsCategoryName):
        procedureName = functionName+"_"+str(fromRangeID)
        templateFile = configr.installScriptsTemplatePath + "/CastStorageService/DIAG/set_localTemplate.sql"
        dataFile     = configr.installScriptsDataPath + "/CastStorageService/DIAG/set_local.sql"
        ReadRules.processDataFile("", templateFile, dataFile, "{{FUNCTION-NAME_FROM-RANGE-ID}}", procedureName)
        ReadRules.processDataFile("", dataFile, dataFile, "{{RULE_CATEGORY_NAME}}", metricsCategoryName)
        print("[", dataFile ,"] has been generated successfully with [", procedureName ,",", metricsCategoryName ,"]")
            
    def processDataFile(self, inPath, outPath, templStr, dataStr):
        f = open(inPath,'r')
        filedata = f.read()
        f.close()
        
        newdata = filedata.replace(templStr, dataStr )
        
        f = open(outPath,'w')
        f.write(newdata)
        f.close() 
        
    
    def mergeMetaModelFiles(self, artifactMetaFile, ruleMetaFile, mergedMetaFileName):
        
        mytree = ET.parse(artifactMetaFile)
        myroot = mytree.getroot()       
        
        # adding an element to the root node
#        attrib = {}
#        element = myroot.makeelement('seconditems', attrib)
        
        # adding an element to the seconditem node
#        attrib = {'name2': 'secondname2'}
#        subelement = myroot[0][1].makeelement('seconditem', attrib)
#        ET.SubElement(myroot[1], 'seconditem', attrib)
#        myroot[0][1].text = 'seconditemabc'
#        myroot.append(element)
     

        ruleMetaTree = ET.parse(ruleMetaFile)
        ruleRoot = ruleMetaTree.getroot()
        partial_categoryTags =  ruleRoot.find('partial_category')  
        myroot.append(partial_categoryTags)
        print("<partial_category> is appended...!!!")
        categories = ruleRoot.find('category') 
        print("<category> is appended...!!!")
        myroot.append(categories)       
        
        # create a new XML file with the new element
        mytree.write(mergedMetaFileName)
        print("Merged into ["+ mergedMetaFileName +"]  \n\tfrom [", artifactMetaFile ,"] \n\twith [", ruleMetaFile ,"]")
        
        # ToDo : find and replace for 
        # CVM_CustomMetrics   to    Mendix_CustomMetrics
        # CVM:                to    Mendix:


    def formatXMLHeader(self, generatedMetaFileName, finalMetaFileName, metricsCategoryName):

        generatedMeta = open(generatedMetaFileName,'r')
        generatedMetaFiledata = generatedMeta.read()
        generatedMeta.close()
        
        generatedMetaFiledata = generatedMetaFiledata.replace("CVM_CustomMetrics", metricsCategoryName)
        print("Formated [CVM_CustomMetrics -> Mendix_CustomMetrics]")
        generatedMetaFiledata = generatedMetaFiledata.replace("CVM:", "Mendix:")
        print("Formated [CVM: -> Mendix:]")
        
        f = open(finalMetaFileName, "w+")
        f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        f.write(generatedMetaFiledata)
        print("MetaModel is ready to use; Place in [", finalMetaFileName ,"]")
          
        
    def copyAllMasterFileXMLsIntoCurrentWorkspace(self, firstSourceXMLRootPath, destinationXMLRootPath):
#        firstSourceXMLRootPath = "C:/SOURCES/DEV/com.castsoftware.labs.3rdparty.csv.integration/generators/output/"
#        destinationXMLRootPath = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFiles/"

#        IMPLParametersFile = "IMPLParameters.xml"
#        sourceFileIMPLParameters = firstSourceXMLRootPath + IMPLParametersFile
#        destinationIMPLParameters = destinationXMLRootPath + IMPLParametersFile

        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "IMPLQualityRules.xml")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "IMPLTechnologies.xml")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "IMPLParameters.xml")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "SPECContributors.xml")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "SPECDocumentation.xml")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "SPECThresholds.xml")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "MetricsDirectory.xml")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "Config.xml.template")
        ReadRules.deleteFilesWithExceptionHandling("", destinationXMLRootPath, "MetricsCompiler.jar")

        try:
            os.rmdir(destinationXMLRootPath)
        except Exception as ex:
            print("Error while deleting the folder \n", ex)
        
        try:
            shutil.copytree(firstSourceXMLRootPath, destinationXMLRootPath, symlinks = True)  
            print("All MASTERFILES are successfully placed into [", destinationXMLRootPath ,"]")
        except Exception as ex:
            print("Error while copying MASTERFILES the folder \n", ex)
        
        
    def deleteFilesWithExceptionHandling(self, filePath, fileName):
        try:
            os.remove( filePath + fileName )
        except Exception as ex:
            print("Error while deleting files \n", ex)
        
#        IMPLQualityRulesFile = "IMPLQualityRules.xml"
#        sourceFileIMPLQualityRules = firstSourceXMLRootPath + IMPLQualityRulesFile
#        destinationIMPLQualityRules = destinationXMLRootPath + IMPLQualityRulesFile
#        ReadRules.copyMasterFileXMLs("",  sourceFileIMPLQualityRules, destinationIMPLQualityRules)
        
#        IMPLTechnologiesFile = "IMPLTechnologies.xml"
#        sourceFileIMPLTechnologies = firstSourceXMLRootPath + IMPLTechnologiesFile
#        destinationIMPLTechnologies = destinationXMLRootPath + IMPLTechnologiesFile
#        ReadRules.copyMasterFileXMLs("",  firstSourceXMLRootPath, destinationXMLRootPath)
        
#        MetricsDirectoryFile = "MetricsDirectory.xml"
#        sourceFileMetricsDirectory = firstSourceXMLRootPath + MetricsDirectoryFile
#        destinationMetricsDirectory = destinationXMLRootPath + MetricsDirectoryFile
#        ReadRules.copyMasterFileXMLs("",  sourceFileMetricsDirectory, destinationMetricsDirectory)
        
#        SPECContributorsFile = "SPECContributors.xml"
#        sourceFileSPECContributors = firstSourceXMLRootPath + SPECContributorsFile
#        destinationSPECContributors = destinationXMLRootPath + SPECContributorsFile
#        ReadRules.copyMasterFileXMLs("",  sourceFileSPECContributors, destinationSPECContributors)
        
#        SPECDocumentationFile = "SPECDocumentation.xml"
#        sourceFileSPECDocumentation = firstSourceXMLRootPath + SPECDocumentationFile
#        destinationSPECDocumentation = destinationXMLRootPath + SPECDocumentationFile
#        ReadRules.copyMasterFileXMLs("",  sourceFileSPECDocumentation, destinationSPECDocumentation)
        
#        SPECThresholdsFile = "SPECThresholds.xml"
#        sourceFileSPECThresholds = firstSourceXMLRootPath + SPECThresholdsFile
#        destinationSPECThresholds = destinationXMLRootPath + SPECThresholdsFile
#        ReadRules.copyMasterFileXMLs("",  sourceFileSPECThresholds, destinationSPECThresholds)
 
#        secondSourceXMLRootPath = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFilesTemplate/"    
#        ConfigXMLTemplateFile = "Config.xml.template"
#        sourceFileConfigXMLTemplate = firstSourceXMLRootPath + ConfigXMLTemplateFile
#        destinationConfigXMLTemplate = destinationXMLRootPath + ConfigXMLTemplateFile
#        ReadRules.copyMasterFileXMLs("",  sourceFileConfigXMLTemplate, destinationConfigXMLTemplate)
        
#        MetricsCompilerJarFile = "MetricsCompiler.jar"
#        sourceFileMetricsCompilerJar = firstSourceXMLRootPath + MetricsCompilerJarFile
#        destinationMetricsCompilerJar = destinationXMLRootPath + MetricsCompilerJarFile
#        ReadRules.copyMasterFileXMLs("",  sourceFileMetricsCompilerJar, destinationMetricsCompilerJar)
        
    def copyMasterFileXMLs(self, sourceFileWithPath, destinationFileWithPath):        
        shutil.copyfile(sourceFileWithPath, destinationFileWithPath)
        
#        ReadRules.copyfile("", sourceFileWithPath, destinationFileWithPath)
          
   
    def copyFile(self, sourceFileWithPath, destinationFileWithPath):
        shutil.copyfile(sourceFileWithPath, destinationFileWithPath)

