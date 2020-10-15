from selenium import webdriver

class loginPage:
    textbox_username_id= "Email"
    textbox_passward_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver= driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassward(self,passward):
        self.driver.find_element_by_id(self.textbox_passward_id).clear()
        self.driver.find_element_by_id(self.textbox_passward_id).send_keys(passward)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogot(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()






