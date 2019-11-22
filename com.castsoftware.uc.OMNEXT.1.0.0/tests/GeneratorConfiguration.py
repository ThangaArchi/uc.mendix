'''
Created on 22-Nov-2019

@author: TKA
'''

class ExtensionConfiguration(object):
    '''
    classdocs
    '''
    loc = ("C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/Mendix_Objects_Rules.xlsx") 
        
    csv_filename = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_003.csv"

    destinationToCopy = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.labs.3rdparty.csv.integration.2.2.0/generators/Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_003.csv"
   
    metaModelFileName = "MendixMetaModel.xml"
    
    languageFileName = "MendixLanguagePattern.xml"
    
    langID = "Mendix"    
    metricsCategoryName = "Mendix_CustomMetrics"
    clientAppName = langID

    metaModel_fileNo = "723"

    baseCategory_id = 2103000
    toRangeID = 2103000+999
    
    sqlFunctionName = "SET_MENDIX_OMNEXT"

    artifactMetaFile = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/MendixMetaModel.xml"
    
    ruleMetaFile     = "C:/SOURCES/DEV/com.castsoftware.labs.3rdparty.csv.integration/generators/output/CVM_CustomMetrics_MetaModel_generated.xml"
    
    mergedMetaFileName = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/MergedMendixMetaModel.xml"
    
    finalMetaFileName = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/FinalMendixMetaModel.xml"

#    firstSourceXMLRootPath = "C:/SOURCES/DEV/com.castsoftware.labs.3rdparty.csv.integration/generators/output/"
    firstSourceXMLRootPath = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFilesTemplate/"
#    secondSourceXMLRootPath = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFilesTemplate/"    
#    secondSourceXMLRootPath = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFilesTemplate/"    
    destinationXMLRootPath  = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFiles/"

    installScriptsTemplatePath = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/InstallScriptsTemplate"
    installScriptsDataPath     = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/InstallScripts"


    def __init__(self, params):
        '''
        Constructor
        '''
        