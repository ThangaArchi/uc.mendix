'''
Created on 13-Nov-2019

@author: TKA
'''
from tests.prepareCSV import ReadRules as rRul
from tests.GeneratorConfiguration import ExtensionConfiguration as configr

class MetaGenerator(object):
    '''
    classdocs
    '''
#    loc = ("C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/Mendix_Objects_Rules.xlsx") 
        
#    csv_filename = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_003.csv"

#    destinationToCopy = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.labs.3rdparty.csv.integration.2.2.0/generators/Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_003.csv"
   
#    metaModelFileName = "MendixMetaModel.xml"
    
#    languageFileName = "MendixLanguagePattern.xml"
    
#    langID = "Mendix"
#    metricsCategoryName = "Mendix_CustomMetrics"

#    metaModel_fileNo = "723"

    print("started...........!!!")
    rRul.createMetaModelWithArtifacts("", configr.metaModelFileName, configr.loc, configr.langID, configr.metaModel_fileNo, configr.metricsCategoryName)
    
    rRul.createLanguagePattern("", configr.languageFileName, configr.langID)
    
    rRul.prepareCSVs("", configr.loc, configr.csv_filename, configr.destinationToCopy)
    
#    baseCategory_id = 2103000
#    toRangeID = 2103000+999
    
#    XML files {{FROM-RANGE-ID TO-RANGE-ID}}
    rRul.generateInstallCommonDIAGTableDefintion("", configr.baseCategory_id, configr.toRangeID )
        
    rRul.generateInstallCommonDIAGLocalPackageTemplate("", configr.clientAppName)
        
    rRul.generateInstallCommonADGConfigDataModel("", configr.baseCategory_id, configr.toRangeID )
    
    rRul.generateInstallCommonADGMetricTreeTemplate("", configr.clientAppName)
    
    rRul.generateInstallCommonDIAGSqlSetDefinitionTemplate("", configr.baseCategory_id, configr.sqlFunctionName)
    
    rRul.generateInstallCastStorageServiceDIAGSqlFunctionTemplate("", configr.baseCategory_id, configr.sqlFunctionName, configr.metricsCategoryName)

#    artifactMetaFile = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/MendixMetaModel.xml"
#    ruleMetaFile     = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.labs.3rdparty.csv.integration.2.2.0/generators/output/CVM_CustomMetrics_MetaModel_generated.xml"
#    rRul.mergeMetaModelFiles(self, artifactMetaFile, ruleMetaFile)
    
    def __init__(self, params):
        '''
        Constructor
        '''
        