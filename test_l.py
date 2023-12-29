import sys
from Selenium2Library import Selenium2Library
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
from ctypes.wintypes import MSG
import pyautogui
from contextlib import nested
from openpyxl.styles.builtins import output
sys.path.append('..\..\libraries\standard') 
sys.path.append('../../libraries/standard')
sys.path.append('..\..\libraries\Application_specific')
import common_importstatements
from common_importstatements import *
import admin
from admin import FromConfigFile
import common_reader
from common_reader import Capturing
from collections import OrderedDict

class TC1(Selenium2Library):
 dict = admin.FromConfigFile.dict
 Test_Results = admin.FromConfigFile.Test_Results
 def testresult1(self):
     self.Test_Results[(self.dict['Executed_Test_Name'])]['name'] = 'Aadhi'
     self.Test_Results[(self.dict['Executed_Test_Name'])]['age'] = '25'
     print "self.Test_Results", self.Test_Results

class TC2(Selenium2Library):
 dict = admin.FromConfigFile.dict
 Test_Results = admin.FromConfigFile.Test_Results
 def testresult2(self):
     self.Test_Results[(self.dict['Executed_Test_Name'])]['name'] = 'Bobby'
     self.Test_Results[(self.dict['Executed_Test_Name'])]['age'] = '12'
     self.Test_Results[(self.dict['Executed_Test_Name'])]['address'] = '25 jail road'
     print "self.Test_Results", self.Test_Results
     #print "self.Test_Results[(self.dict['Executed_Test_Name'])]", self.Test_Results[(self.dict['Executed_Test_Name'])]
     for key, value in self.Test_Results.items():
        print str(key)+"  :"+ str(value)

class TC3(Selenium2Library):
 def testresult3(self):
     my_dict = OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
     for key, value in my_dict.items():
         print key+"  :"+ value   
 

'''from datetime import date

currentdate = date.today()
currentdate = str(currentdate)
print currentdate +"_"+currentdate[8:]'''

'''exception_str_list = ["Undefined", "Null", "Error", "Object Reference", "Parser invalid object", "Server Error", "Not part of the model", "DBNull", "Null", "Sub Query"]
search_str = "dark chocolate null"
for string in exception_str_list:
    print "current string in list", string
    status =  str(string).lower() in str(search_str).lower()
    print "status", status
    if status == False:
       print "No such exception text in this page"
    else:
       print "Exception present in this page"
       break '''
    


'''stxt = 'Object REFERENCE'
ftxt = 'server error used to come. Object Reference'
print str(stxt).lower() in str(ftxt).lower()'''


'''for i in range(0,5):
    print i'''


''''n = "IP 562365"

print n[3:]'''




'''def datePicker(self,loc, r, sheetname):
        self.set_selenium_implicit_wait(10)
        r = int(r)
        date = self.d[r]['birthreg_date']
        today = date.today()
        print today.strftime('%d/%B/%Y')
        #print date
        print "today", today
        print type(today)
        
        picdate = date
        print picdate.strftime('%d/%B/%Y')
        
        print "picdate", picdate
        print type(picdate)
        
        year = picdate.strftime('%Y')
        month = picdate.strftime('%B')
        day = picdate.strftime('%d').lstrip("0")
        pdate = month+' '+year
        loc = 'xpath=//*[@id="txtRDt"]'
        self.click_element(loc)
        if picdate > today:        
            while(True):
                #seldate = self.get_text('xpath=//*[@class="datepicker-switch"]')
                seldate = self.get_text('xpath=//*[@class="datepicker-days"]//th[@class="datepicker-switch"]')              
                if pdate == seldate:
                    break
                else:
                    #self.click_element('xpath=//*[@class="next"]')
                    self.click_element('xpath=//*[@class="datepicker-days"]//th[@class="next"]')
            self.click_element('xpath=/html/body/div/div[1]/table/tbody/tr/td[(text()="'+day+'")]')
        else:
            while(True):
                #seldate = self.get_text('xpath=//*[@class="datepicker-switch"]')
                seldate = self.get_text('xpath=//*[@class="datepicker-days"]//th[@class="datepicker-switch"]')
                if pdate == seldate:
                    break
                else:
                    #self.click_element('xpath=//*[@class="prev"]')
                    self.click_element('xpath=//*[@class="datepicker-days"]//th[@class="prev"]')
            self.click_element('xpath=/html/body/div/div[1]/table/tbody/tr/td[(text()="'+day+'")]')
'''