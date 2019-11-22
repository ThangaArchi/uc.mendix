import unittest
from cast.application.test import run
from cast.application import create_postgres_engine
import logging
logging.root.setLevel(logging.DEBUG)
import unittest
import cast.analysers.test

class TestIntegration(unittest.TestCase):

    def test1(self):
       
        # run(kb_name='db_apptest_local', application_name='JVTEST', engine=create_postgres_engine(user='operator',password='CastAIP',host='KSHLAP',port=2280))
        # run(kb_name='db_xpdl_local', application_name='XPDL_APP', engine=create_postgres_engine(user='operator', password='CastAIP', host='KSHLAP', port=2280))  
        run(kb_name='f_8314_2028_local', application_name='NProject', engine=create_postgres_engine(user='operator', password='CastAIP', host='localhost', port=2280))   


        analysis = cast.analysers.test.UATestAnalysis('he')
        
        # mandatory for the ast
#         analysis.add_dependency('com.castsoftware.internal.platform')

        analysis.add_selection('jee_mongo_01')
 
        analysis.set_verbose()
         
        analysis.run()
        
#         analysis2 = cast.analysers.ua.Extension()
#         analysis2.

#         analysis2.set_verbose()
        
#         analysis2.



if __name__ == "__main__":
    unittest.main()

