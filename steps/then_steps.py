# features/steps/login_steps.py
from behave import then
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

@then('I should be logged in successfully')
def step_impl_logged_in_successfully(context):
    """
    Verifies that the user is successfully logged in by checking the current URL
    or the presence of a specific element on the post-login page.
    """
    print("Verifying successful login...")
    try:
        current_url = context.driver.current_url
        assert SUCCESS_PAGE_URL in current_url, \
            f"Expected to be on a page containing '{SUCCESS_PAGE_URL}', but current URL is '{current_url}'"
        print(f"Successfully navigated to URL containing '{SUCCESS_PAGE_URL}'.")

        print("Login successful assertion passed!")
    except Exception as e:
        raise Exception(f"Login verification failed: {e}")

@then('I can logout successfully')
def step_impl_logout_successfully(context):
    """
    Verifies that the user can log out successfully by checking the current URL
    or the presence of a specific element on the pre-login page.
    """
    print("Verifying successful logout...")
    context.driver.get('https://www.hudl.com/logout?forward=https%3A%2F%2Ffan.hudl.com%2Fcallback%3Fstate%3DLw%253D%253D')
    time.sleep(2) 