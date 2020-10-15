import pytest
from selenium import webdriver
@pytest.fixture()

def setup(browser):
    if browser=='chrome':
        driver= webdriver.Chrome(executable_path = "C:\\Users\\Owner\\Downloads\\chromedriver_win32\\chromedriver.exe")
        print("Lauching chrome browser.......")
    elif browser=='Firefox':
        driver= webdriver.firefox()
        print("Lauching firefox browser.......")
    else:
        driver= webdriver.ie()
    return driver

def pytest_addoption(parser):  # it will tkae input from Command line
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Adding env info into HTMLreports
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Amandeep Kaur"



