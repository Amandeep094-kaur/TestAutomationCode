import pytest
from selenium import webdriver
from pageobjects.LoginPage import loginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    BaseURL = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUsername()
    Password= ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_home_Page_Title(self, setup):
        self.logger.info("****************** Test_001_Login ****************")
        self.logger.info("****************** Verifying Home PAge Title ****************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************** HomePAge Title Test Passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_Page_Title.png")
            self.driver.close()
            self.logger.error("****************** HomePAge Title Test Failed ****************")
            assert False

    def test_login(self,setup):
        self.logger.info("****************** Verifying Login Test ****************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.lp= loginPage(self.driver)
        self.lp.setUserName(self.Username)
        self.lp.setPassward(self.Password)
        self.lp.clickLogin()
        act_title= self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****************** Login Test Passed ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************** Login Test Failed ****************")
            assert  False
