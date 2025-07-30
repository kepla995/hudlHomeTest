# features/environment.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

HOMEPAGE_URL = "https://www.hudl.com"

def before_all(context):
    print("\nSetting up WebDriver...")

    # Installing ChromeDriver using webdriver-manager
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())

    # options = Options()
    # # Uncomment the line below if you want to run Chrome in headless mode (without UI)
    # # options.add_argument("--headless")
    # options.add_argument("--no-sandbox") # Required for some environments (e.g., Docker)
    # options.add_argument("--disable-dev-shm-usage") # Required for some environments

    context.driver = webdriver.Chrome(service=service)
    context.driver.implicitly_wait(10) # Implicit wait for elements to appear
    print("WebDriver setup complete.")

def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    print(f"Navigating to homepage: {HOMEPAGE_URL}")
    context.driver.get(HOMEPAGE_URL)


def after_all(context):
    """
    This function runs once after all scenarios.
    It quits the Selenium WebDriver.
    """
    print("Quitting WebDriver...")
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
        print("WebDriver quit.")

# You can also add `before_scenario` and `after_scenario` if you need
# to do specific setup/teardown for each scenario, e.g., clearing cookies.
# def before_scenario(context, scenario):
#     print(f"Starting scenario: {scenario.name}")

# def after_scenario(context, scenario):
#     print(f"Finished scenario: {scenario.name}")
