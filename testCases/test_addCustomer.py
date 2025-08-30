import string
import random

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()  #Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("****** Test_003_AddCustomer *******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("****** Login Successful *******")

        self.logger.info("****** Starting Add Customer Test *********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("****** Providing Customer Info *******")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRole("Registered")
        self.addcust.setManagerOfVender("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pratik")
        self.addcust.setLastName("Pawar")
        self.addcust.setCompanyName("BusyQA")
        self.addcust.setAdminContent("This is for Testing.......")
        self.addcust.clickOnSave()

        self.logger.info("****** Saving Customer Info *******")

        self.logger.info("****** Add Customer Validation Started *******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("****** Add Customer Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addCustomer_scr.png")  #Screenshot
            self.logger.error("****** Add Customer Test Failed *******")
            assert True == False

        self.driver.close()
        self.logger.info("****** Ending Test_003_AddCustomer Test ******")







# To generate Random Emails :
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


