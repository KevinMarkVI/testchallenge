import os
import time
from selenium import webdriver
from sauceclient import SauceClient

# username = os.environ.get('SAUCE_USERNAME')
# access_key = os.environ.get('SAUCE_ACCESS_KEY')
username = "KevinMarkVI"
access_key = "105a063b-8837-4c2d-b323-d6a86c71ff97"
assert username, "Unable to pull username from environment variables"
assert access_key, "Unable to pull access_key from environment variables"

desired_cap = {
  'platform': "Mac OS X 10.9",
  'browserName': "chrome",
  'version': "31",
  'build': int(time.time())
}

def before_scenario(context, scenario):
  desired_cap['name'] = scenario.name
  context.browser = webdriver.Remote(
  command_executor ='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key),
  desired_capabilities = desired_cap)

def after_scenario(context, scenario):
  context.browser.quit()
  sauce_client = SauceClient(username, access_key)
  passed = scenario.status == 'passed'
  sauce_client.jobs.update_job(context.browser.session_id, passed = passed)

