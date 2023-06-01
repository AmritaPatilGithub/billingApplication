from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class BaseSteps:
    @given('Launch Chrome browser')
    def launchBrowser(context):
        context.driver = webdriver.Chrome(
            executable_path='/Users/amruta/Desktop/Amruta/IT/drivers/chrome/chromedriver_mac64/chromedriver')
