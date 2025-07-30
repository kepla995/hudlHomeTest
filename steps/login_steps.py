# features/steps/login_steps.py
from behave import given, when, then
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
PASSWORD_INPUT_LOCATOR = (By.ID, "password")
# TITLE = driver.find_element(By.TAG_NAME, "h1")

# Updated: Using CSS_SELECTOR to find the button by its data-qa-id attribute
# LOGIN_BUTTON = driver.find_element(by.LINK_TEXT, " log in " "/html/body/header/div/div[2]/a")
# DROPDOWN_SELECT = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/div/div/div/div/a[1]") 


@given('I am on the login page')
def step_impl_on_login_page(context):
    """
    Navigates the browser to the specified login page URL.
    """
    print(f"Navigating to login page")
    context.driver.get(LOGIN_PAGE_URL)
    time.sleep(2)  # Wait for the page to load completely


@when('I enter my email')
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



@when('I enter my password')
def step_impl_enter_password(context):
    """
    Finds the password input field and enters a placeholder password.
    """
    print("Entering password...")
    try:
        password_input = context.driver.find_element(*PASSWORD_INPUT_LOCATOR)
        password_input.send_keys("password123!") # Replace with a valid test password
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
        # Give some time for the page to load after clicking, especially if it's an AJAX call
        time.sleep(2) # Consider using explicit waits (WebDriverWait) for better reliability
        print("Login button pressed.")
    except Exception as e:
        raise Exception(f"Could not find or click login button using {continue_button}: {e}")


@then('I should not be able to login')
def step_impl_not_logged_in(context):
    """
    Verifies that the user is not logged in by checking the current URL or the presence of a specific element.
    """
    print("Verifying unsuccessful login...")
    try:
        current_url = context.driver.current_url
        assert SUCCESS_PAGE_URL not in current_url, \
            f"Expected not to be on a page containing '{SUCCESS_PAGE_URL}', but current URL is '{current_url}'"
        print(f"Successfully navigated to URL NOT containing '{SUCCESS_PAGE_URL}'.")
    except Exception as e:
        raise Exception(f"Login verification failed: {e}")


@then('I should see incorrect username or password error message')
def step_impl_user_does_not_exist(context):
    """
    Verifies that the user sees an error message indicating that the user does not exist.
    """
    print("Verifying incorrect username or password error message...")
    try:
        # Example: Check for an error message element
        error_message = context.driver.find_element(By.ID, "error-element-password")  # Adjust the selector as needed
        assert error_message.is_displayed(), "Your email or password is incorrect. Try again."
        print("User does not exist error message found and displayed.")
    except Exception as e:
        raise Exception(f"Error message verification failed: {e}")

# @then('I should be logged in successfully')
# def step_impl_logged_in_successfully(context):
#     """
#     Verifies that the user is successfully logged in by checking the current URL
#     or the presence of a specific element on the post-login page.
#     """
#     print("Verifying successful login...")
#     try:
#         # Option 1: Check the URL
#         current_url = context.driver.current_url
#         assert SUCCESS_PAGE_URL_PARTIAL in current_url, \
#             f"Expected to be on a page containing '{SUCCESS_PAGE_URL_PARTIAL}', but current URL is '{current_url}'"
#         print(f"Successfully navigated to URL containing '{SUCCESS_PAGE_URL_PARTIAL}'.")

#         # Option 2: Check for a specific element on the success page
#         # This is often more robust than just checking the URL.
#         # welcome_message = context.driver.find_element(*WELCOME_MESSAGE_LOCATOR)
#         # assert welcome_message.is_displayed(), "Welcome message not displayed after login."
#         # print("Welcome message found and displayed.")

#         print("Login successful assertion passed!")
#     except Exception as e:
#         raise Exception(f"Login verification failed: {e}")