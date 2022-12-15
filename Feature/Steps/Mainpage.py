from selenium.webdriver.common.by import By
from behave import given, when, then
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC
#from time import sleep


@given("Open Cureskin Page")
def main_page (context):
    #context.driver.get("https://shop.cureskin.com/")
    context.App.main_page.open_main()


@when("Click on {category}")
def shop_by_category(context, category):
    context.App.main_page.shop_by_category()

@then("Verify {Header} is visible")
def header(context, Header):
    context.App.main_page.header()