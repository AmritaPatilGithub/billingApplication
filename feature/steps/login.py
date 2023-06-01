

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from feature.steps.BaseSteps import BaseSteps


class LoginSteps(BaseSteps):

    @when('open homepage')
    def openHomepage(context):
        context.driver.get('https://opensource-demo.orangehrmlive.com/')

    @when('Enter "{user}" and "{pwd}"')
    def enterCredentials(context,user, pwd):
        wt= WebDriverWait(context.driver,10)
        wt.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@name='username']")))
        context.driver.find_element(By.XPATH, "//input[@name='username']").click()
        context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(user)
        context.driver.find_element(By.XPATH, "//input[@name='password']").click()
        context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pwd)

    @when('Click on login button')
    def clickLogin(context):
        context.driver.find_element(By.XPATH,"//button[text()=' Login ']").click()

    @when ('I login to application')
    def loginToApplication(self):
        self.enterCredentials("admin","admin123")
        self.clickLogin()

    @then('User must successfully login to the dashboard page')
    def loginToAccount(context):
        try:
            wt = WebDriverWait(context.driver, 10)
            wt.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
            text = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
        except:
            context.driver.close()
            assert False, 'Test Failed'

        if text == 'Dashboard':
            context.driver.close()
            assert True,'Test passed'



