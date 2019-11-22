'''
Created on 13-Nov-2019

@author: TKA
'''

from tests.prepareCSV import ReadRules as rRul
from tests.GeneratorConfiguration import ExtensionConfiguration as configr
import subprocess

class MergeMetaGenerator(object):

   
#    artifactMetaFile = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/MendixMetaModel.xml"
    
#    ruleMetaFile     = "C:/SOURCES/DEV/com.castsoftware.labs.3rdparty.csv.integration/generators/output/CVM_CustomMetrics_MetaModel_generated.xml"
    
#    mergedMetaFileName = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/MergedMendixMetaModel.xml"
    
#    finalMetaFileName = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/tests/FinalMendixMetaModel.xml"
    
    rRul.mergeMetaModelFiles("", configr.artifactMetaFile, configr.ruleMetaFile, configr.mergedMetaFileName)
    
    rRul.formatXMLHeader("", configr.mergedMetaFileName, configr.finalMetaFileName, configr.metricsCategoryName)   
    
#    firstSourceXMLRootPath = "C:/SOURCES/DEV/com.castsoftware.labs.3rdparty.csv.integration/generators/output/"
#    secondSourceXMLRootPath = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFilesTemplate/"    
#    destinationXMLRootPath  = "C:/Kumar/Workspace/CASTExtensionDevWS/com.castsoftware.uc.OMNEXT.1.0.0/MasterFiles/"
    rRul.copyAllMasterFileXMLsIntoCurrentWorkspace("", configr.firstSourceXMLRootPath, configr.destinationXMLRootPath)
#    rRul.copyAllMasterFileXMLsIntoCurrentWorkspace1("", configr.destinationXMLRootPath, configr.firstSourceXMLRootPath)
#    rRul.copyAllMasterFileXMLsIntoCurrentWorkspace("", configr.destinationXMLRootPath, configr.firstSourceXMLRootPath, configr.secondSourceXMLRootPath)
    
#    subprocess.call([r'C:\Kumar\Softwares\DevTools_Copy\GenerateAdgConfigData_from_MASTER_FILES.bat'])   
    
    def __init__(self, params):
        '''
        Constructor
        '''
        