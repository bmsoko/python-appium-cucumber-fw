from appium import webdriver
from selenium.webdriver.common.by import By
from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        "platformName": "Android",
        "appium:app": "/Users/brunosoko/Documents/dev/python-appium-cucumber-fw/app_binaries/James Rider_1.22.0.apk",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.hdw.james.rider",
        "appium:appActivity": ".viewlayer.launcher.LauncherActivity",
        "appium:noReset": "true",
        "appium:adbExecTimeout": "1200000",
    }
    context.driver = webdriver.Remote('http://localhost:4723', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5000)
    context.app = Application(context.driver)
    context.first_name_update = ''
    context.last_name_update = ''


def after_scenario(context, scenario):
    # context.driver.quit()
    pass