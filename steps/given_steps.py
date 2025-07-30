# features/steps/login_steps.py
from behave import given
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


