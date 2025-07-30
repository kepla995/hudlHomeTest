
from behave import when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@when('I select the Google login option')
def step_impl_select_google_login(context):
    """
    Finds the Google login option and clicks it.
    """
    print("Selecting Google login option...")
    try:
        google_login_button = context.driver.find_element(By.XPATH, "/html/body/code/div/main/section/div/div/div/div[4]/form[1]/button")
        google_login_button.click()
        print("Google login button clicked.")
        time.sleep(2)
    except Exception as e:
        raise Exception(f"Could not find or click Google login button: {e}")


@when('I enter my Google credentials')
def step_impl_enter_google_credentials(context):
    """
    Finds the Google email and password input fields and enters placeholder credentials.
    """
    print("Entering Google credentials...")
    try:
        email_input = context.driver.find_element(*GOOGLE_EMAIL_INPUT_LOCATOR)
        email_input.send_keys("jbantock95@gmail.com")
        print("Email entered.")
        time.sleep(120)
        next_button = context.driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
        next_button.click()
        print("next button clicked.")
    except Exception as e:
        raise Exception(f"Could not find or interact with email input using {GOOGLE_EMAIL_INPUT_LOCATOR}: {e}")