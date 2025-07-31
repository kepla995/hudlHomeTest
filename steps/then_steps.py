# features/steps/login_steps.py
from behave import then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# --- Configuration ---
SUCCESS_PAGE_URL = "https://fan.hudl.com/" 

# --- Locators ---
EMAIL_INPUT_LOCATOR = (By.ID, "username")
PASSWORD_INPUT_LOCATOR = (By.ID, "password")

# --- Step Definitions ---
# --- Login ---
@then('I should not be able to login')
def step_impl_not_logged_in(context):
    # Verifies that the user is not logged in by checking the current URL or the presence of a specific element.
    print("Verifying unsuccessful login...")
    try:
        current_url = context.driver.current_url
        assert SUCCESS_PAGE_URL not in current_url, \
            f"Expected not to be on a page containing '{SUCCESS_PAGE_URL}', but current URL is '{current_url}'"
        print(f"Successfully navigated to URL NOT containing '{SUCCESS_PAGE_URL}'.")
    except Exception as e:
        raise Exception(f"Login verification failed: {e}")

@then('I should be logged in successfully')
def step_impl_logged_in_successfully(context):
    # Verifies that the user is successfully logged in by checking the current URL
    print("Verifying successful login...")
    try:
        current_url = context.driver.current_url
        assert SUCCESS_PAGE_URL in current_url, \
            f"Expected to be on a page containing '{SUCCESS_PAGE_URL}', but current URL is '{current_url}'"
        print(f"Successfully navigated to URL containing '{SUCCESS_PAGE_URL}'.")

        print("Login successful assertion passed!")
    except Exception as e:
        raise Exception(f"Login verification failed: {e}")

# --- Error Messages ---
@then('I should see incorrect username or password error message')
def step_impl_user_does_not_exist(context):
    # Verifies that the user sees an error message indicating that the user does not exist.
    print("Verifying incorrect username or password error message...")
    try:
        # Example: Check for an error message element
        error_message = context.driver.find_element(By.ID, "error-element-password")  # Adjust the selector as needed
        assert error_message.is_displayed(), "incorrect username or password"
        print("User does not exist error message found and displayed.")
    except Exception as e:
        raise Exception(f"Error message verification failed: {e}")

@then('I should see incorrect password error message')
def step_impl_incorrect_password(context):
    # Verifies that the user sees an error message indicating that the password is incorrect.
    print("Verifying incorrect password error message...")
    try:
        # Example: Check for an error message element
        error_message = context.driver.find_element(By.ID, "error-element-password")  # Adjust the selector as needed
        assert error_message.is_displayed(), "Your email or password is incorrect. Try again."
        print("Incorrect password error message found and displayed.")
    except Exception as e:
        raise Exception(f"Error message verification failed: {e}")


# --- Logout ---  
@then('I can logout successfully')
def step_impl_logout_successfully(context):
    # Logs out the user by navigating to the logout URL ready for next test
    print("Logging out user...")
    context.driver.get('https://www.hudl.com/logout?forward=https%3A%2F%2Ffan.hudl.com%2Fcallback%3Fstate%3DLw%253D%253D')
    time.sleep(2) 

# --- Password Reset ---
@then('I should be redirected to the password reset page')
def step_impl_password_reset_page(context):
    # Verifies that the user is redirected to the password reset page after clicking the forgot password link.
    print("Verifying redirection to password reset page...")
    try:
        current_url = context.driver.current_url
        assert "https://identity.hudl.com/u/reset-password" in current_url, \
            f"Expected to be on the password reset page, but current URL is '{current_url}'"
        print("Successfully redirected to the password reset page.")
    except Exception as e:
        raise Exception(f"Password reset page verification failed: {e}")