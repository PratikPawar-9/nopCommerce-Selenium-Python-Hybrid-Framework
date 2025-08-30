from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tbl_SearchResults_xpath = "(//table[@aria-describedby='customers-grid_info'])[2]"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_id).clear()
        self.driver.find_element(By.ID,self.txtFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLastName_id).clear()
        self.driver.find_element(By.ID,self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.ID,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.ID,self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        rows = self.driver.find_elements(By.XPATH, self.tableRows_xpath)
        for r in range(1, len(rows) + 1):
            emailid = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]").text
            if emailid.strip().lower() == email.strip().lower():  # case-insensitive check
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        rows = self.driver.find_elements(By.XPATH, self.tableRows_xpath)
        for r in range(1, len(rows) + 1):
            cust_name = self.driver.find_element(
                By.XPATH, f"//table[@id='customers-grid']/tbody/tr[{r}]/td[3]"
            ).text
            if cust_name.strip().lower() == name.strip().lower():  # case-insensitive match
                flag = True
                break
        return flag



