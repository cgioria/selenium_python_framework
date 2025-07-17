from behave import given, when, then
from pages.login_page import LoginPage
from utilities.driver_manager import DriverManager

@given('I am on the login page')
def step_impl(context):
    context.driver = DriverManager.get_chrome_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to_login()

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@when('I click the login button')
def step_impl(context):
    # La acción ya está incluida en el método login()
    pass

@when('I click the login button without entering credentials')
def step_impl(context):
    context.login_page.click(context.login_page.LOGIN_BUTTON)

@then('I should be redirected to the secure area')
def step_impl(context):
    assert context.login_page.is_login_successful(), "Login failed"

@then('I should see an error message "{message}"')
def step_impl(context, message):
    assert message in context.login_page.get_flash_message(), \
        f"Expected '{message}' not found in flash message"

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()