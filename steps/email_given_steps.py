# features/steps/login_steps.py
from behave import given
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# --- Configuration ---
LOGIN_PAGE_URL = "https://www.hudl.com/login?utm_content=hudl_primary&amp;utm_source=www.hudl.com&amp;utm_medium=login_dropdown&amp;utm_campaign=platform_logins" # Example: Replace with your application's login URL

# --- Locators ---
LOGIN_PAGE_MENU_LOCATOR = (By.CLASS_NAME, "mainnav__item mainnav__item--expandable")
LOGIN_PAGE_SELECTION_LOCATOR = (By.CLASS_NAME, "subnavitem__label")


# --- Step Definitions ---

@given('I am on the login page')
def step_impl_on_login_page(context):
    # Navigates the browser to the specified login page URL.
    # print(f"Navigating to login page")
    # Login_Page_Open_Menu = context.driver.find_element(*LOGIN_PAGE_MENU_LOCATOR)
    # Login_Page_Open_Menu.click()
    # time.sleep(1)
    # Login_Page_Select_Login = context.driver.find_element(*LOGIN_PAGE_SELECTION_LOCATOR)
    # Login_Page_Select_Login.click()
    # time.sleep(2) 
    
    print(f"Navigating to login page")
    context.driver.get(LOGIN_PAGE_URL)
    time.sleep(2)  # Wait for page to load


