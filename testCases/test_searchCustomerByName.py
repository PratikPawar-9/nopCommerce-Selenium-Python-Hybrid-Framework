import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_005:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("******** SearchCustomerByEmail_005 ********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("******** Login Successful ********")

        self.logger.info("******** Starting Search Customer By Name *******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("******** Search Customer By Name *******")
        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstName("Victoria")
        searchCust.setLastName("Terces")
        searchCust.clickSearch()
        time.sleep(3)
        status = searchCust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("******** TC_SearchCustomerByName_005 Completed *******")
        self.driver.close()