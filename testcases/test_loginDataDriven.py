import pytest
from selenium import webdriver
from pageobjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtiliy
import time

class Test_002_DDT_Login:
    BaseURL = ReadConfig.getApplicationURL()
    Path = ".//TestData/LoginTestData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("****************** Test_002_DDT_Login ****************")
        self.logger.info("****************** Verifying Login_DDT Test ****************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.lp= loginPage(self.driver)
        self.rows= XLUtiliy.getRowCount(self.Path,"Sheet1")
        print("number of rows",self.rows)
        list_status = []         #empty list

        for r in range(2, self.rows + 1):
            self.username = XLUtiliy.readData(self.Path, "Sheet1", r, 1)
            self.password = XLUtiliy.readData(self.Path, "Sheet1", r, 2)
            self.expected = XLUtiliy.readData(self.Path, "Sheet1", r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassward(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if act_title==expected_title:
                if self.expected=="Pass":
                    self.logger.info("**** Passed ******")
                    self.lp.clickLogot()
                    list_status.append("Pass")
                elif self.expected=="Fail":
                    self.logger.info("**** Failed ******")
                    self.lp.clickLogot()
                    list_status.append("Fail")
            elif act_title != expected_title:
                if self.expected=="Pass":
                    self.logger.info("**** Failed ******")
                    list_status.append("Fail")
                elif self.expected=="Fail":
                    self.logger.info("**** Passed ******")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("********Login DDT Test Passed*********")
            self.driver.close()
            assert  True
        else:
            self.logger.info("**********Login DDT Test Failed********")
            self.driver.close()
            assert False

        self.logger.info("*************End of Login DDt Test**************")
        self.logger.info("**********Completd Test_002_DDT_Login*************")










