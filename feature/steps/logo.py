# * is for all the gherkin keywords
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from feature.steps.BaseSteps import BaseSteps


class LogoSteps(BaseSteps):
    logoLocator = "//div[@class='orangehrm-login-branding']//img"
    # def __init__(self):
    #     self.logoLocator= "//div[@class='orangehrm-login-branding']//img"
    @when('Open orange HRM homepage')
    def openHomepage(context):
        context.driver.get('https://opensource-demo.orangehrmlive.com/')


    @then('Verify that the logo present on the page')
    def verifyLogo(context):
        # status= context.driver.("//div[@class='orangehrm-login-branding']//img").is_displayed
        # assert status is True
        wt = WebDriverWait(context.driver, 5)
        wt.until(
            expected_conditions.visibility_of_element_located((By.XPATH,context.logoLocator)))
        logo= context.driver.find_element(By.XPATH,context.logoLocator)
        assert logo.is_displayed() is True

    @then('Close the browser')
    def closeBrowser(context):
        context.driver.close()

