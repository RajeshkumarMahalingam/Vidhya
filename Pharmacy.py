import sys
from Selenium2Library import Selenium2Library
import pyautogui
sys.path.append('..\..\libraries\standard') 
sys.path.append('../../libraries/standard')
sys.path.append('..\..\libraries\Application_specific')
import common_importstatements
from common_importstatements import *
import admin
from admin import FromConfigFile
import common_reader
from common_reader import Capturing
from selenium.common.exceptions import UnexpectedAlertPresentException

class InPharmacycommon(Selenium2Library):
    dict = admin.FromConfigFile.dict
    objects = common_reader.Capturing.objects
    d = Capturing().data_off("Pharm_PharmacyStore")
    
    def screenshotonfailure(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.register_keyword_to_run_on_failure('capturing_screenshot_on_failure')
        self.dict['BROWSER'] = self._current_browser()
    
    def selecting_the_frame(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.select_frame(self.objects["FO_MainFrame"])
        time.sleep(5)
        self.dict['BROWSER'] = self._current_browser()  
    
    def selecting_storename(self, r):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        time.sleep(5)
        r = int (r)
        #self.d[r]['storename'] = "PHARMACY"
        self.dict['FROMSTORENAME'] = self.d[r]['storename']
        cboelement = self._element_find('xpath=//*[@id="LstStore"]//a[text()="'+self.d[r]['storename']+'"]', True, False)
        jsFunction = "arguments[0].scrollIntoView(true);"
        self.browser.execute_script(jsFunction, cboelement)
        self.double_click_element('xpath=//*[@id="LstStore"]//a[text()="'+self.dict['FROMSTORENAME']+'"]')
        self.dict['BROWSER'] = self._current_browser()
    
    def unselecting_the_frame(self):
        self.set_selenium_implicit_wait(10)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.unselect_frame()
        self.dict['BROWSER'] = self._current_browser()  
        
class InIPDrugIssueCashCreditMode(Selenium2Library):
    dict = admin.FromConfigFile.dict
    objects = common_reader.Capturing.objects

    def screenshotonfailure(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.register_keyword_to_run_on_failure('capturing_screenshot_on_failure')
        self.dict['BROWSER'] = self._current_browser()

    def selecting_the_frame(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.select_frame(self.objects["FO_MainFrame"])
        time.sleep(7)
        self.dict['BROWSER'] = self._current_browser()  

    def searching_ipno(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        #self.dict['IPNO'] = "IP00001674"
        self.wait_until_element_is_visible(self.objects['Pharm_IPSale_IPDrugIssueCashCredit_Searchbtn'])
        self.input_text(self.objects["Pharm_IPSale_IPDrugIssueCashCredit_Searchbtn"], str(self.dict['IPNO']))
        self.dict['BROWSER'] = self._current_browser()
    
    def entering_into_patientdetails(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.wait_until_element_is_visible(self.objects['Pharm_IPSale_IPDrugIssueCashCredit_SelectPatientDetails'])
        #self.click_element(self.objects['Pharm_Sales_IPSales_SelectDet'])
        self.click_element(self.objects['Pharm_IPSale_IPDrugIssueCashCredit_SelectPatientDetails'])
        time.sleep(10)
        self.dict['BROWSER'] = self._current_browser()

    def getting_ReqNo(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.wait_until_element_is_visible(self.objects["Pharm_IPSale_IPDrugIssueCashCredit_RequestNo"], 15, "bill no was not visible")
        ReqnoMsg = self.get_text(self.objects["Pharm_IPSale_IPDrugIssueCashCredit_RequestNo"])
        self.msg = ((str(ReqnoMsg).split('Req.No: ')))[1].split('/ Reg.No :')[0].split('/ Req By :')[0]
        self.dict['REQNO'] = self.msg
        self.dict['REQNO']
        print("ReqNo_is : ", self.dict['REQNO'])
        self.dict['BROWSER'] = self._current_browser()

    def selecting_savebtn(self):        
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        time.sleep(10)
        self.wait_until_element_is_visible(self.objects['Pharm_IPSale_IPDrugIssueCashCredit_SaveBtn'])
        self.click_element(self.objects['Pharm_IPSale_IPDrugIssueCashCredit_SaveBtn'])
        time.sleep(2)
        self.dict['BROWSER'] = self._current_browser()

    def getting_message(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.wait_until_element_is_visible(self.objects['Pharm_IPSale_IPDrugIssueCashCredit_Message'], 30, 'Bill was not saved')
        BillGeneratedmsg = self.get_text(self.objects['Pharm_IPSale_IPDrugIssueCashCredit_Message'])
        print(BillGeneratedmsg)        
        '''try:
            self.wait_until_element_is_visible(self.objects['Pharm_Sales_IPDrugReqCancel_Reject'])
            self.click_element(self.objects['Pharm_Sales_IPDrugReqCancel_Reject'])
        except:
            pass'''
        time.sleep(10)
        pyautogui. FAILSAFE = False
        pyautogui.click(1121,641)
        time.sleep(1)
        pyautogui.click(697,135)
        self.dict['BROWSER'] = self._current_browser()

    def unselecting_the_frame(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.unselect_frame()
        self.dict['BROWSER'] = self._current_browser()
 
class InIPCashCreditReturnReceive(Selenium2Library):
    dict = admin.FromConfigFile.dict
    objects = common_reader.Capturing.objects

    def screenshotonfailure(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.register_keyword_to_run_on_failure('capturing_screenshot_on_failure')
        self.dict['BROWSER'] = self._current_browser()
    def selecting_the_frame(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.select_frame(self.objects["WARD_MainFrame"])
        time.sleep(7)
        self.dict['BROWSER'] = self._current_browser() 
    def searching_ipno(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        #self.dict['IPNO'] = "Ip14229"
        self.wait_until_element_is_visible(self.objects['Pharm_IPSalesReturn_CashCreditReturnReceive_IPNo'])
        self.input_text(self.objects["Pharm_IPSalesReturn_CashCreditReturnReceive_IPNo"], str(self.dict['IPNO']))
        self.press_key(self.objects["Pharm_IPSalesReturn_CashCreditReturnReceive_IPNo"], '\\13')
        self.dict['BROWSER'] =  self._current_browser()          
    def selecting_searchbtn(self):        
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        time.sleep(2)
        self.wait_until_element_is_visible(self.objects['Pharm_IPSalesReturn_CashCreditReturnReceive_SearchBtn'])
        self.click_button(self.objects['Pharm_IPSalesReturn_CashCreditReturnReceive_SearchBtn'])
        time.sleep(5)
        self.dict['BROWSER'] = self._current_browser()
    def entering_into_patientdetails(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.wait_until_element_is_visible('xpath=//*[@id="addmedsbody"]//tr[1]//td[1]')
        #self.click_element(self.objects['Pharm_Sales_IPSales_SelectDet'])
        self.click_element('xpath=//*[@id="addmedsbody"]//tr[1]//td[1]')
        time.sleep(5)
        self.dict['BROWSER'] = self._current_browser()    
    def selecting_savebtn(self):        
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        time.sleep(2)
        self.wait_until_element_is_visible(self.objects['Pharm_IPSalesReturn_CashCreditReturnReceive_Savebtn'])
        self.click_element(self.objects['Pharm_IPSalesReturn_CashCreditReturnReceive_Savebtn'])
        time.sleep(2)
        self.dict['BROWSER'] = self._current_browser()
    
    def getting_message(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.wait_until_element_is_visible(self.objects['Pharm_IPSalesReturn_CashCreditReturnReceive_Message'], 30, 'Bill was not saved')
        Msg = self.get_text(self.objects['Pharm_IPSalesReturn_CashCreditReturnReceive_Message'])
        print(Msg)        
        time.sleep(10)
        pyautogui. FAILSAFE = False
        pyautogui.click(1121,641)
        time.sleep(1)
        #pyautogui.click(697,135)
        self.dict['BROWSER'] = self._current_browser()

    def unselecting_the_frame(self):
        self.set_selenium_implicit_wait(30)
        self._cache.current = self.dict['BROWSER']
        self.browser = self._current_browser()
        self.unselect_frame()
        self.dict['BROWSER'] = self._current_browser()