from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    sbc = (By.ID, "Details-HeaderMenu-3")
    Body = (By.CSS_SELECTOR, "a[href='/collections/body'][class*='t caption-large']")

    def open_main(self):
        self.driver.get('https://shop.cureskin.com/')

    def shop_by_category(self):
        self.click(*self.sbc)

    def header(self):
        expected_result = "Body"
        actual_result = self.driver.find_elements_by_(*self.Body).text
        assert expected_result == actual_result, f' Error! expected {expected_result} but got {actual_result}'




