from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser......")
    elif browser == "firefox":
        driver = webdriver.firefox()
        print("Launching firefox Browser......")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")  #This will get the value from CLI/hooks

@pytest.fixture()
def browser(request):  #This will return browser value to setup mode
    return request.config.getoption("--browser")

############# Pytest HTML Reports #################

# Set HTML report title
def pytest_html_report_title(report):
    report.title = "nop commerce Test Report"

# Add custom environment info
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name: nop commerce",
        "Module: Customers",
        "Tester: Pratik"
    ])

# Remove unwanted environment info
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)