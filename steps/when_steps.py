# features/steps/login_steps.py
from behave import when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# --- Configuration ---
# IMPORTANT: Replace with your actual login page URL and expected success URL
LOGIN_PAGE_URL = "https://www.hudl.com/login?utm_content=hudl_primary&amp;utm_source=www.hudl.com&amp;utm_medium=login_dropdown&amp;utm_campaign=platform_logins" # Example: Replace with your application's login URL
SUCCESS_PAGE_URL = "https://fan.hudl.com/" 

# --- Locators ---
# IMPORTANT: Replace these with the actual locators (ID, Name, CSS Selector, XPath)
# # for your application's elements.
EMAIL_INPUT_LOCATOR = (By.ID, "username")
GOOGLE_EMAIL_INPUT_LOCATOR = (By.ID, "identifierId")
PASSWORD_INPUT_LOCATOR = (By.ID, "password")
# TITLE = driver.find_element(By.TAG_NAME, "h1")

# Updated: Using CSS_SELECTOR to find the button by its data-qa-id attribute
# LOGIN_BUTTON = driver.find_element(by.LINK_TEXT, " log in " "/html/body/header/div/div[2]/a")
# DROPDOWN_SELECT = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div/div/a[1]") 



@when('I enter an email')
def step_impl_enter_email(context):
    """
    Finds the email input field and enters a placeholder email address.
    """
    print("Entering email...")
    try:
        email_input = context.driver.find_element(*EMAIL_INPUT_LOCATOR)
        email_input.send_keys("jbantock123abc@gmail.com") # Replace with a valid test email
        print("Email entered.")
        continue_button = context.driver.find_element(By.NAME, "action")
        continue_button.click()
        print("Continue button clicked.")
    except Exception as e:
        raise Exception(f"Could not find or interact with email input using {EMAIL_INPUT_LOCATOR}: {e}")


@when('I enter a valid email')
def step_impl_enter_valid_email(context):
    """
    Finds the email input field and enters a placeholder email address.
    """
    print("Entering email...")
    try:
        email_input = context.driver.find_element(*EMAIL_INPUT_LOCATOR)
        email_input.send_keys("jbantockmeerza@gmail.com") # Replace with a valid test email
        print("Email entered.")
        continue_button = context.driver.find_element(By.NAME, "action")
        continue_button.click()
        print("Continue button clicked.")
    except Exception as e:
        raise Exception(f"Could not find or interact with email input using {EMAIL_INPUT_LOCATOR}: {e}")



@when('I enter a password')
def step_impl_enter_password(context):
    """
    Finds the password input field and enters a placeholder password.
    """
    print("Entering password...")
    try:
        password_input = context.driver.find_element(*PASSWORD_INPUT_LOCATOR)
        password_input.send_keys("password123!") 
        print("Password entered.")

    except Exception as e:
        raise Exception(f"Could not find or interact with password input using {PASSWORD_INPUT_LOCATOR}: {e}")


@when('I enter a valid password')
def step_impl_enter_password(context):
    """
    Finds the password input field and enters a placeholder password.
    """
    print("Entering password...")
    try:
        password_input = context.driver.find_element(*PASSWORD_INPUT_LOCATOR)
        password_input.send_keys("James123!") 
        print("Password entered.")

    except Exception as e:
        raise Exception(f"Could not find or interact with password input using {PASSWORD_INPUT_LOCATOR}: {e}")


@when('I press the login button')
def step_impl_press_login_button(context):
    """
    Finds the login button and clicks it.
    """
    print("Pressing login button...")
    try:
        continue_button = context.driver.find_element(By.NAME, "action")
        continue_button.click()
        print("Continue button clicked.")
        time.sleep(2)
        print("Login button pressed.")
    except Exception as e:
        raise Exception(f"Could not find or click login button using {continue_button}: {e}")
