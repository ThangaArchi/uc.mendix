import os
import traceback
import re
from cast.analysers import log
import cast.analysers.ua
from cast.analysers import create_link,CustomObject,Bookmark
import xml.etree.ElementTree as ET
import uuid

from io import StringIO

class OmNextAnalysisLevel(cast.analysers.ua.Extension):
    
    def _init_(self):
        log.debug ('In __init__ ... ')

    def start_analysis(self):
        log.debug ('In start_analysis ...OMNEXT ' + str(os.listdir(os.curdir))) 
        log.info ('In start_analysis ... OMNEXT' + str(os.listdir(os.curdir))) 
        
    def start_file(self, file):
        log.debug ('In start_file ... ' + str(file))
        log.info ('In start_file ... ' + str(file))
        self.file_obj = file
        self.file_path = self.file_obj.get_path()
        log.debug("File lists.." + self.file_path)
        
        omnxtObj = CustomObject()
        omnxtObj.set_name("module")
        omnxtObj.set_fullname("C:\\Users\\MKU\\Desktop\\kamal")
        omnxtObj.set_type("OMNEXT_module")
        
        omnxtObj.set_parent(file)
        omnxtObj.set_guid(str(uuid.uuid4())) 
        
        omnxtObj.save()
        
        log.debug ('Object created ... ' + str(omnxtObj))
        log.info ('Object created ... ' + str(omnxtObj))        
        

    def end_analysis(self):
#         
        log.debug ('In end_analysis ... OMNEXT')
        log.info ('In end_analysis ... OMNEXT')
        
        
    def saveObject(self, obj_refr, name, fullname, obj_type, parent, guid):
        obj_refr.set_name(name)
        obj_refr.set_fullname(fullname)
        obj_refr.set_type(obj_type)
        obj_refr.set_parent(parent)
        obj_refr.set_guid(guid) 
        obj_refr.save()           
