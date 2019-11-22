# -*- coding: latin-1 -*-
#import cast_upgrade_1_5_7 # @UnusedImport
from cast.application import open_source_file # @UnresolvedImport
import csv
import sys
import logging
from lxml import etree as ET         # benefit from a pretty print feature

# DONE: scratch generation : read CSV, and store all MasterFindingName (unique) in a DicoMFN (entry = prop + ID) or OrderedList, get maxID.
# TODO: incremental generation : read existing MM.xml and store the existing properties in same Set, before reading CSV for new ones.
# TODO: incremental generation with multiple .csv files.
# TODO: make some column mandatory, some others optional (descriptions). When col is absent, don't generate the corresponding SubElement.

############ variable initialization ##############################################
# input & output : hard-coded for this independent batch program
csv_filename = ".\Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_003.csv"
#csv_filename = ".\Dala_Utilities_6cols_1unknownFile_1unknownFinding_TC_4.csv"
metamodel_file_gen = "C:\SOURCES\DEV\com.castsoftware.labs.3rdparty.csv.integration\generators\output\CVM_CustomMetrics_MetaModel_generated.xml"
master_file_folder =  "C:\Kumar\Workspace\CASTExtensionDevWS\com.castsoftware.uc.OMNEXT.1.0.0\MasterFilesTemplate"

baseCategoryName = "CVM_CustomMetrics"  # CHANGE this name for any new 3rd party integration.
baseCategory_id = 2103000               # CHANGE this value for any new 3rd party integration.
metric_id = baseCategory_id             # init metric ID
property_id = baseCategory_id + 1       # init property ID
INF_SUB_TYPE_id = 1                     # base ID for property's INF_SUB_TYPE

setMasterFindingName = []               # init set  (we want to collect unique names form a CSV...having potentially several violations of same kind
dictStandardTechnology = {}             # init dict  (it will be filled in function initDictStandardTechnology)
def initDictStandardTechnology():
    global dictStandardTechnology       # a question of variable scope, dict is defined and used outside this function
    dictStandardTechnology["ALL TECHNOLOGIES"] = "0"

###########################################
# CSV reading and XML documents  generation
###########################################

logging.info("Begin generation of Metamodel file : " + metamodel_file_gen + " from CSV file : " + csv_filename)

with open_source_file(csv_filename) as csvfile: 
            mydictreader = csv.DictReader(csvfile, delimiter=';')       # wo fieldnames : line #1 is used to get the column names
            # format validation to prevent KeyError :
            # mandatory columns for MM and MT : MasterFindingName + TBD: some MasterFinding long name (for QR name)
            # optional columns for MM and MT: Severity, FindingDescription, BusinessImpact, MasterFindingRemediationInstructions, ...
            logging.info("CSV format validation - mydictreader.fieldnames = "+str(mydictreader.fieldnames))
            if 'MasterFindingName' not in mydictreader.fieldnames:
                logging.info("CSV invalid format - mandatory column MasterFindingName is missing, exiting")
                sys.exit()
            nbRecord = 0
            for row in mydictreader:
                nbRecord +=1
                #logging.debug (str(row['MasterFindingName']) + ' at line ' + str(row['AffectedSourceLine']) + ' of file ' + str(row['AffectedSource']))   # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe0 in position 1512: invalid continuation byte
                # Build a Set : add an element only if not already present
                if str(row['MasterFindingName']) not in setMasterFindingName:
                        setMasterFindingName.append(str(row['MasterFindingName']))
                        logging.debug ("Added MasterFindingName " + str(row['MasterFindingName']))

# 0. Build XML document for MetaModel
docMetaModel = ET.Element('metaModel', attrib={'file_level': "client",'file_no': "103" })
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  # 
partial_cat = ET.SubElement(docMetaModel, 'partial_category',  attrib={'name': "APM Sources"})
my_dict = {}
my_dict['name'] = baseCategoryName
parent = ET.SubElement(partial_cat, 'inheritedCategory', attrib=my_dict)

my_dict = {}
my_dict['name'] = baseCategoryName
my_dict['id'] = str(baseCategory_id)                        # an integer as string (str(my_integer))
custom_cat = ET.SubElement(docMetaModel, 'category',  attrib=my_dict)    # made it with 2 variables

desc = ET.SubElement(custom_cat, 'description')
desc.text = 'Custom category for additional properties on CVM integration'            # automatic description


# 00. Build XML document for MetricsDirectory
docMetricsDirectory = ET.Element('root')
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  # 
#metric_tmpl = ET.SubElement(docMetricsDirectory, 'metric',  attrib={'id': "-1", 'type': "N/A",'originalName': "",'active': "N/A",'detached': "N/A",'ignored': "false"})
# For CVM, 1 single TC, custom 
#tech_criteria = ET.SubElement(docMetricsDirectory, 'metric',  attrib={'id': "2103999", 'type': "technical-criterion",'originalName': "Secure Coding - 3rd party analyzers",'active': "true",'detached': "false",'ignored': "false"})
# For others, declare here standard parent TC(s) (each TC having a contributor QR in this set of Master Files)
tech_criteria = ET.SubElement(docMetricsDirectory, 'metric',  attrib={'id': "61024", 'type': "technical-criterion",'originalName': "Programming Practices - Structuredness",'active': "N/A",'detached': "N/A",'ignored': "N/A"})
# 1 row per QR, in main loop below

# 1. Build XML document for IMPLQualityRules
docIMPLQualityRules = ET.Element('root')
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  # 

# 2. Build XML document for IMPLParameters
docIMPLParameters = ET.Element('root')
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  #

# 3. Build XML document for IMPLTechnologies
docIMPLTechnologies = ET.Element('root')
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  #

# 4. Build XML document for SPECContributors
docSPECContributors = ET.Element('root')
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  #

# 5. Build XML document for SPECDocumentation
docSPECDocumentation = ET.Element('root')
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  #

# 6. Build XML document for SPECThresholds
docSPECThresholds = ET.Element('root')
comment = ET.Comment("This file has been automatically generated from CSV file XYZ, by generator XYZ")  #

# begin loop from MasterFindingName Set
for finding in setMasterFindingName:
    # 0. Build XML document for MetaModel
    my_dict = {}
    my_dict['name'] = finding
    my_dict['type'] = 'integer'
    my_dict['id'] = str(metric_id)
    prop = ET.SubElement(custom_cat, 'property', attrib=my_dict) # made it with 2 variables out of 3 attributes
    propitem1 = ET.SubElement(prop, 'description')
    propitem1.text = 'CVM: Number of ' + finding                 # automatic description
    propitem2 = ET.SubElement(prop, 'attribute', attrib={'name': "INF_TYPE", 'intValue': "2103000" }) # fixed
    my_dict = {}
    my_dict['name'] = 'INF_SUB_TYPE'
    my_dict['intValue'] = str(INF_SUB_TYPE_id)
    propitem3 = ET.SubElement(prop, 'attribute', attrib=my_dict)
    propitem4 = ET.SubElement(prop, 'attribute', attrib={'name': "ACCESS_APPVIEW", 'intValue': "1" })
    propitem5 = ET.SubElement(prop, 'attribute', attrib={'name': "ACCESS_CVS", 'intValue': "1" })
    propitem6 = ET.SubElement(prop, 'attribute', attrib={'name': "ACCESS_HTML", 'intValue': "1" })
    
    # 00. Build XML document for MetricsDirectory
    metricDir_dict = {}
    metricDir_dict['id'] = str(metric_id)
    metricDir_dict['type'] = "quality_rule"
    metricDir_dict['originalName'] = finding        # another col is expected here
    metricDir_dict['active'] = "true"
    metricDir_dict['detached'] = "false"
    metricDir_dict['ignore'] = "false"
    metricDirMetric = ET.SubElement(docMetricsDirectory, 'metric',  attrib=metricDir_dict)
    
    # 1. Build XML document for IMPLQualityRules
    implQR_dict = {}
    implQR_dict['id'] = str(metric_id)
    implQR_dict['type'] = "quality_rule"
    implQR_dict['originalName'] = finding           # another col is expected here
    implQR_dict['xxl'] = "N/A"
    implQR_dict['unify'] = "N/A"
    implQR_dict['executionLocation'] = "local-central"
    implQR_dict['scopeID'] = "2103100"              # make scopeID a var : scope is base + 100
    implQR_dict['executionPrecedenceConstraint'] = ""
    implQR_dict['scopeLabel'] = "NO LABEL"
    implQR_dict['propertyID'] = str(property_id)
    implQR_dict['diagnosisValueType'] = "integer"
    implQR_dict['localSiteInitialize'] = "DSS_FILTER_SCOPE"
    implQR_dict['localSiteDiagnose'] = "DSS_DIAG_SCOPE_GENERIC_NUM"
    implQR_dict['localSiteCountViolations'] = "count-distinct"
    implQR_dict['localSiteCountTotal'] = "DSS_DIAG_TOTAL_GENERIC"
    implQR_dict['centralSiteInitialize'] = "ADG_CENTRAL_SCOPE_INIT"
    metricIMPLQualityRules = ET.SubElement(docIMPLQualityRules, 'metric',  attrib=implQR_dict)
        
    # 2. Build XML document for IMPLParameters
    # no parameters for this kind of QRs in general

    # 3. Build XML document for IMPLTechnologies
    #TODO: think on how (smart) to add custom technologies
    #TODO: document a case of fileName rejection : could be inserted by custom UA for non-standard AIP technologies
    implTechno_dict = {}
    implTechno_dict['id'] = str(metric_id)
    implTechno_dict['type'] = "quality_rule"
    implTechno_dict['originalName'] = finding           # another col is expected here
    # initialization of global dictionary
    ret = initDictStandardTechnology()
    # looping through the 37 standard technologies
    for key in dictStandardTechnology:
        implTechno_dict['filter'] = dictStandardTechnology[key]
        implTechno_dict['filterLabel'] = key
        metricIMPLTechnologies = ET.SubElement(docIMPLTechnologies, 'metric',  attrib=implTechno_dict)
    
    # 4. Build XML document for SPECContributors
    specContrib_dict = {}
    specContrib_dict['id'] = "2103999"   # TODO: make var
    specContrib_dict['type'] = "technical-criterion"
    specContrib_dict['originalName'] = "Secure Coding - 3rd party analyzers"   # TODO: make var       
    specContrib_dict['contributorId'] = str(metric_id)
    specContrib_dict['contributorType'] = "quality_rule"
    specContrib_dict['contributorOriginalName'] = finding           # another col is expected here
    specContrib_dict['critical'] = "false"                          
    specContrib_dict['weight'] = "9"                                # TODO: make var from CSV : invert value of #20 Severity
    metricSPECContributors = ET.SubElement(docSPECContributors, 'metric',  attrib=specContrib_dict)
    
    # 5. Build XML document for SPECDocumentation
    # 5.1 Build XML document for SPECDocumentation - associatedValueName section
    specDocumentationAssocValue_dict = {}
    specDocumentationAssocValue_dict['id'] = str(metric_id)
    specDocumentationAssocValue_dict['type'] = "quality_rule"
    specDocumentationAssocValue_dict['originalName'] = finding                 # another col is expected here 
    specDocumentationAssocValue_dict['section'] = "associatedValueName"  
    metricSPECDocumentationAssocValue = ET.SubElement(docSPECDocumentation, 'metric',  attrib=specDocumentationAssocValue_dict)
    metricSPECDocumentationAssocValueEnglish = ET.SubElement(metricSPECDocumentationAssocValue, 'english')
    metricSPECDocumentationAssocValueEnglish.text = "Number of violation pattern"
    
    # 5.2 Build XML document for SPECDocumentation - description section
    specDocumentationDescription_dict = {}
    specDocumentationDescription_dict['id'] = str(metric_id)
    specDocumentationDescription_dict['type'] = "quality_rule"
    specDocumentationDescription_dict['originalName'] = finding                 # another col is expected here 
    specDocumentationDescription_dict['section'] = "description"  
    metricSPECDocumentationDescription = ET.SubElement(docSPECDocumentation, 'metric',  attrib=specDocumentationDescription_dict)
    metricSPECDocumentationDescriptionEnglish = ET.SubElement(metricSPECDocumentationDescription, 'english')
    metricSPECDocumentationDescriptionEnglish.text = "This quality rules has been computed by a third-party analyzer and integrated in AIP on the matching source file."
                                                                                # or from CSV : #48 FindingDescription
                                                                                
    # 5.3 Build XML document for SPECDocumentation - name section
    specDocumentationName_dict = {}
    specDocumentationName_dict['id'] = str(metric_id)
    specDocumentationName_dict['type'] = "quality_rule"
    specDocumentationName_dict['originalName'] = finding                 # another col is expected here 
    specDocumentationName_dict['section'] = "name"  
    metricSPECDocumentationName = ET.SubElement(docSPECDocumentation, 'metric',  attrib=specDocumentationName_dict)
    metricSPECDocumentationNameEnglish = ET.SubElement(metricSPECDocumentationName, 'english')
    metricSPECDocumentationNameEnglish.text = finding                   # another col is expected here , NOT specified in spec v2.
    
    # 5.4 Build XML document for SPECDocumentation - output section
    specDocumentationOutput_dict = {}
    specDocumentationOutput_dict['id'] = str(metric_id)
    specDocumentationOutput_dict['type'] = "quality_rule"
    specDocumentationOutput_dict['originalName'] = finding                 # another col is expected here 
    specDocumentationOutput_dict['section'] = "output"  
    metricSPECDocumentationOutput = ET.SubElement(docSPECDocumentation, 'metric',  attrib=specDocumentationOutput_dict)
    metricSPECDocumentationOutputEnglish = ET.SubElement(metricSPECDocumentationOutput, 'english')
    metricSPECDocumentationOutputEnglish.text = "Associated to each artifact with violations, the Quality Rule provides: - The number of violation patterns - Bookmarks for violation patterns found in source code."

    # 5.5 Build XML document for SPECDocumentation - rationale section
    specDocumentationRationale_dict = {}
    specDocumentationRationale_dict['id'] = str(metric_id)
    specDocumentationRationale_dict['type'] = "quality_rule"
    specDocumentationRationale_dict['originalName'] = finding                 # another col is expected here 
    specDocumentationRationale_dict['section'] = "rationale"  
    metricSPECDocumentationRationale = ET.SubElement(docSPECDocumentation, 'metric',  attrib=specDocumentationRationale_dict)
    metricSPECDocumentationRationalEnglish = ET.SubElement(metricSPECDocumentationRationale, 'english')
    metricSPECDocumentationRationalEnglish.text = "A rationale from CSV file"   # TODO: #18 BusinessImpact

    # 5.6 Build XML document for SPECDocumentation - reference section
    # none at this time. Keep section for future use
    
    # 5.7 Build XML document for SPECDocumentation - remediation section
    specDocumentationRemediation_dict = {}
    specDocumentationRemediation_dict['id'] = str(metric_id)
    specDocumentationRemediation_dict['type'] = "quality_rule"
    specDocumentationRemediation_dict['originalName'] = finding                 # another col is expected here 
    specDocumentationRemediation_dict['section'] = "remediation"  
    metricSPECDocumentationRemediation = ET.SubElement(docSPECDocumentation, 'metric',  attrib=specDocumentationRemediation_dict)
    metricSPECDocumentationRemediationEnglish = ET.SubElement(metricSPECDocumentationRemediation, 'english')
    metricSPECDocumentationRemediationEnglish.text = "A remediation from CSV file"    # TODO: #17 MasterFindingRemediationInstructions

    # 5.8 Build XML document for SPECDocumentation - total section
    specDocumentationTotal_dict = {}
    specDocumentationTotal_dict['id'] = str(metric_id)
    specDocumentationTotal_dict['type'] = "quality_rule"
    specDocumentationTotal_dict['originalName'] = finding                 # another col is expected here 
    specDocumentationTotal_dict['section'] = "total"  
    metricSPECDocumentationTotal = ET.SubElement(docSPECDocumentation, 'metric',  attrib=specDocumentationTotal_dict)
    metricSPECDocumentationTotalEnglish = ET.SubElement(metricSPECDocumentationTotal, 'english')
    metricSPECDocumentationTotalEnglish.text = "Number of source files (types inheriting from category APM Sources)"    # depends on the scope used.
    
    # 6. Build XML document for SPECThresholds
    specThresholds_dict = {}
    specThresholds_dict['id'] = str(metric_id)
    specThresholds_dict['type'] = "quality_rule"
    specThresholds_dict['originalName'] = finding           # another col is expected here
    specThresholds_dict['thresholdToGet1'] = "80"           # TODO: align on specification (mine) 
    specThresholds_dict['thresholdToGet2'] = "90" 
    specThresholds_dict['thresholdToGet3'] = "95" 
    specThresholds_dict['thresholdToGet4'] = "96" 
    metricSPECThresholds = ET.SubElement(docSPECThresholds, 'metric',  attrib=specThresholds_dict)
    
    # increment IDs
    metric_id +=2
    property_id +=1
    INF_SUB_TYPE_id +=1
    
print("0. docMetaModel:")
ET.dump(docMetaModel)   # pretty print with lxml
print("00. docMetricsDirectory:")
ET.dump(docMetricsDirectory)
print("1. docIMPLQualityRules:")
ET.dump(docIMPLQualityRules)
print("2. docIMPLParameters:")
ET.dump(docIMPLParameters)
print("3. docIMPLTechnologies:")
ET.dump(docIMPLTechnologies)
print("4. docSPECContributors:")
ET.dump(docSPECContributors)
print("5. docSPECDocumentation:")
ET.dump(docSPECDocumentation)
print("6. docSPECThresholds:") 
ET.dump(docSPECThresholds)

#############################################
# XML trees serialization to target XML files
#############################################

print("About to save to " + metamodel_file_gen)
# lxml API
lxml_string = ET.tostring(docMetaModel, method='text', encoding="UTF-8")
lxml_tree = ET.ElementTree(docMetaModel)
lxml_tree.write(metamodel_file_gen, pretty_print=True, xml_declaration=True, encoding="utf-8")

#print("00. docMetricsDirectory:")
metricsDirectory_xml_file = master_file_folder +"\MetricsDirectory.xml"
lxml_tree = ET.ElementTree(docMetricsDirectory)
lxml_tree.write(metricsDirectory_xml_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

#print("1. docIMPLQualityRules:")
IMPLQualityRules_xml_file = master_file_folder +"\IMPLQualityRules.xml"
lxml_tree = ET.ElementTree(docIMPLQualityRules)
lxml_tree.write(IMPLQualityRules_xml_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

#print("2. docIMPLParameters:")
IMPLParameters_xml_file = master_file_folder +"\IMPLParameters.xml"
lxml_tree = ET.ElementTree(docIMPLParameters)
lxml_tree.write(IMPLParameters_xml_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

#print("3. docIMPLTechnologies:")
IMPLTechnologies_xml_file = master_file_folder +"\IMPLTechnologies.xml"
lxml_tree = ET.ElementTree(docIMPLTechnologies)
lxml_tree.write(IMPLTechnologies_xml_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

#print("4. docSPECContributors:")
SPECContributors_xml_file = master_file_folder +"\SPECContributors.xml"
lxml_tree = ET.ElementTree(docSPECContributors)
lxml_tree.write(SPECContributors_xml_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

#print("5. docSPECDocumentation:")
SPECDocumentation_xml_file = master_file_folder +"\SPECDocumentation.xml"
lxml_tree = ET.ElementTree(docSPECDocumentation)
lxml_tree.write(SPECDocumentation_xml_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

#print("6. docSPECThresholds:") 
SPECThresholds_xml_file = master_file_folder +"\SPECThresholds.xml"
lxml_tree = ET.ElementTree(docSPECThresholds)
lxml_tree.write(SPECThresholds_xml_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

##############################
# Summary for AIA expectations
##############################

print("End generation of Metamodel file          : " + metamodel_file_gen + " from CSV file : " + csv_filename)
print("End generation of Master Files in folder  : " + master_file_folder + " from CSV file : " + csv_filename)
print("*******")
print("SUMMARY")
print("*******")
print("Input CSV file = "+metamodel_file_gen)
print("Output XML Metamodel file = "+csv_filename)
print("Number of records in CSV file                  = "+str(nbRecord))
print("Number of distinct rules (MasterFindingName)   = "+str(len(setMasterFindingName)))
print("Number of generated properties                 = "+str(len(setMasterFindingName)))  # TODO create new variable for that ?
print("Base ID                   : "+str(baseCategory_id))
print("Next ID for properties    : "+str(property_id))
if (property_id - baseCategory_id >= 1000):
    print("Number of generated property IDs above 1000 : you need to allocate (manually) more than one ID range, add more file_no on line 2")
print("criticity of 9 becomes weight " + str(abs(9-10)))
print("criticity of 1 becomes weight " + str(abs(1-10)))
print("criticity of 2 becomes weight " + str(abs(2-10)))