# features/steps/login_steps.py
from behave import when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# --- Locators ---
EMAIL_INPUT_LOCATOR = (By.ID, "username")
GOOGLE_EMAIL_INPUT_LOCATOR = (By.ID, "identifierId")
PASSWORD_INPUT_LOCATOR = (By.ID, "password")


# --- Step Definitions ---
# --- Email ---
@when('I enter an un-registered email')
def step_impl_enter_email(context):
    # Finds the email input field and enters a placeholder email address.
    print("Entering email...")
    try:
        email_input = context.driver.find_element(*EMAIL_INPUT_LOCATOR)
        email_input.send_keys("jbantock123abc@gmail.com") # not a real email
        print("Email entered.")
        continue_button = context.driver.find_element(By.NAME, "action")
        continue_button.click()
        print("Continue button clicked.")
    except Exception as e:
        raise Exception(f"Could not find or interact with email input using {EMAIL_INPUT_LOCATOR}: {e}")


@when('I enter a valid email')
def step_impl_enter_valid_email(context):
    # Finds the email input field and enters a placeholder email address.
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


# --- Password ---
@when('I enter a password')
def step_impl_enter_password(context):
    # Finds the password input field and enters a placeholder password.
    print("Entering password...")
    try:
        password_input = context.driver.find_element(*PASSWORD_INPUT_LOCATOR)
        password_input.send_keys("password123!") 
        print("Password entered.")

    except Exception as e:
        raise Exception(f"Could not find or interact with password input using {PASSWORD_INPUT_LOCATOR}: {e}")


@when('I enter a valid password')
def step_impl_enter_password(context):
    # Finds the password input field and enters a placeholder password.
    print("Entering password...")
    try:
        password_input = context.driver.find_element(*PASSWORD_INPUT_LOCATOR)
        password_input.send_keys("James123!") 
        print("Password entered.")

    except Exception as e:
        raise Exception(f"Could not find or interact with password input using {PASSWORD_INPUT_LOCATOR}: {e}")

# --- Links and Buttons ---
@when('I press the forgot password link')
def step_impl_forgot_password(context):
    # Finds the forgot password link and clicks it.
    print("Pressing forgot password link...")
    try:
        forgot_password_link = context.driver.find_element(By.LINK_TEXT, "Forgot Password")
        forgot_password_link.click()
        print("Forgot password link clicked.")
        time.sleep(2)  # Wait for the page to load
    except Exception as e:
        raise Exception(f"Could not find or click forgot password link: {e}")


@when('I press the login button')
def step_impl_press_login_button(context):
    # Finds the login button and clicks it.
    print("Pressing login button...")
    try:
        continue_button = context.driver.find_element(By.NAME, "action")
        continue_button.click()
        print("Continue button clicked.")
        time.sleep(2)
        print("Login button pressed.")
    except Exception as e:
        raise Exception(f"Could not find or click login button using {continue_button}: {e}")
