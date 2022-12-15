from behave import given, when, then
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC

#from time import sleep


@given("Open search Results Page")
def search_page(context):
    context.App.searchresults_page.search_page()

@when("Select sort by price, low to high")
def sort_price(context):
    context.App.searchresults_page.sort_price()

@then("Verify filter applied")
def filter(context):
    context.App.searchresults_page.filter()


