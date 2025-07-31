from seleniumbase import SB
from behave import when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

GOOGLE_EMAIL_INPUT_LOCATOR = (By.ID, "identifierId")

@when('I select the Google login option')
def step_impl_select_google_login(context):
    """
    Finds the Google login option and clicks it.
    """
    print("Selecting Google login option...")
    try:
        google_login_button = context.driver.find_element(By.XPATH, "/html/body/code/div/main/section/div/div/div/div[4]/form[1]/button")
        google_login_button.click()
        print("Google login button clicked.")
        time.sleep(2)
    except Exception as e:
        raise Exception(f"Could not find or click Google login button: {e}")


@when('I enter Google credentials')
def step_impl_enter_google_credentials(context):

    try:
        email_input = context.driver.find_element(*GOOGLE_EMAIL_INPUT_LOCATOR)
        email_input.send_keys("jbantock95@gmail.com")
        print("Email entered.")
        time.sleep(1)
        next_button = context.driver.find_element(By.CLASS_NAME, "VfPpkd-*")
        next_button.click()
        print("next button clicked.")
    except Exception as e:
        raise Exception(f"Could not find or interact with email input using {GOOGLE_EMAIL_INPUT_LOCATOR}: {e}")

#   Cypress.Commands.add("googleOneTapSignIn", () => {
#   cy.log("Sign-In");
#   cy.log(Cypress.env("GOOGLE_REGISTER_CLIENT_ID"));
#   cy.log(Cypress.env("GOOGLE_REGISTER_CLIENT_SECRET"));
#   cy.log(Cypress.env("GOOGLE_REGISTER_REFRESH_TOKEN"));
#   cy.request({
#     method: "POST",
#     url: "https://www.googleapis.com/oauth2/v4/token",
#     body: {
#       grant_type: "refresh_token",
#       client_id: Cypress.env("GOOGLE_REGISTER_CLIENT_ID"),
#       client_secret: Cypress.env("GOOGLE_REGISTER_CLIENT_SECRET"),
#       refresh_token: Cypress.env("GOOGLE_REGISTER_REFRESH_TOKEN"),
#     },
#   }).then(({ body }) => {
#     const { id_token } = body;
#     cy.wait(10000);
#     cy.window().then((window) => {
#       cy.log("Passing credential in to Google");
#       window.handleCredentialResponse({
#         credential: id_token,
#       });
#     });
#   });
# });