from pages.sauceguineapigmain import SauceGuineaPig
from pages.sauceguineapig2 import SauceGuineaPig2

@given('we are looking at the guinea pig website')
def step_impl(context):
 context.page = SauceGuineaPig(context.browser)

@when('we click on the uncheck box')
def step_impl(context):
  context.page.find_unchecked_checkbox().click()

@then('it should be checked')
def step_impl(context):
  assert context.page.find_unchecked_checkbox().is_selected(), "Checkbox is not selected"

@when('I populate the email field')
def step_impl(context):
  context.page.find_email_input().send_keys('kevinmarkvi@gmail.com')

@then('it should contain the value I entered')
def step_impl(context):
  value = context.page.find_email_input().get_attribute('value')
  assert value == 'kevinmarkvi@gmail.com', "The value is incorrect"

@given('we are on the guinea pig website')
def step_impl(context):
  context.page = SauceGuineaPig(context.browser)

@when('I click on the link')
def step_impl(context):
  context.page.find_link().click

@then('I should see a new page')
def step_impl(context):
  context.page = SauceGuineaPig2(context.browser)
  assert 'another' in context.page.get_title()