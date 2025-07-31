# features/environment.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

HOMEPAGE_URL = "https://www.hudl.com"

def before_all(context):
    # Sets up the WebDriver for the tests
    print("\nSetting up WebDriver...")

    # Installing ChromeDriver using webdriver-manager
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())

    # Configuring Chrome options
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    # chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources on some systems
    # chrome_options.add_argument("--window-size=1920x1080")
    context.driver = webdriver.Chrome(service=service)
    context.driver.implicitly_wait(2) # Implicit wait for elements to appear
    print("WebDriver setup complete.")

def before_scenario(context, scenario):
    # Navigates to the homepage before each scenario
    print(f"Starting scenario: {scenario.name}")
    print(f"Navigating to homepage: {HOMEPAGE_URL}")
    context.driver.get(HOMEPAGE_URL)


def after_all(context):
    #  Quits the WebDriver after all tests are done
    print("Quitting WebDriver...")
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
        print("WebDriver quit.")
