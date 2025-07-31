# features/steps/login_steps.py
from behave import when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv 
import os
import time 

# default directory for .env file is the current directory
# if you set .env in different directory, put the directory address load_dotenv("directory_of_.env)
load_dotenv()

# --- Configuration ---
PASSWORD =  os.getenv("PASSWORD")  # Load the password from the .env file

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
    email_input = context.driver.find_element(*EMAIL_INPUT_LOCATOR)
    email_input.send_keys("newemail@gmail.com") # not a real email
    print("Email entered.")
    continue_button = context.driver.find_element(By.NAME, "action")
    continue_button.click()
    print("Continue button clicked.")


@when('I enter a valid email')
def step_impl_enter_valid_email(context):
    # Finds the email input field and enters a placeholder email address.
    print("Entering email...")
    email_input = context.driver.find_element(*EMAIL_INPUT_LOCATOR)
    email_input.send_keys("jbantockmeerza@gmail.com") # Replace with a valid test email
    print("Email entered.")
    continue_button = context.driver.find_element(By.NAME, "action")
    continue_button.click()
    print("Continue button clicked.")


# --- Password ---
@when('I enter a password')
def step_impl_enter_password(context):
    # Finds the password input field and enters a placeholder password.
    print("Entering password...")
    password_input = context.driver.find_element(*PASSWORD_INPUT_LOCATOR)
    password_input.send_keys("password123!") 
    print("Password entered.")


@when('I enter a valid password')
def step_impl_enter_password(context):
    # Finds the password input field and enters a placeholder password.
    print("Entering password...")
    password_input = context.driver.find_element(*PASSWORD_INPUT_LOCATOR)
    password_input.send_keys(*PASSWORD)  # Use the password from the .env file
    print("Password entered.")


# --- Links and Buttons ---
@when('I press the forgot password link')
def step_impl_forgot_password(context):
    # Finds the forgot password link and clicks it.
    print("Pressing forgot password link...")
    forgot_password_link = context.driver.find_element(By.LINK_TEXT, "Forgot Password")
    forgot_password_link.click()
    print("Forgot password link clicked.")
    time.sleep(2)  # Wait for the page to load


@when('I press the login button')
def step_impl_press_login_button(context):
    # Finds the login button and clicks it.
    print("Pressing login button...")
    continue_button = context.driver.find_element(By.NAME, "action")
    continue_button.click()
    print("Continue button clicked.")
    time.sleep(2)
    print("Login button pressed.")