import time

from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Searchpage(Page):

    Sort_Selection= (By.CSS_SELECTOR, "select[id='SortBy']")
    results = (By.CSS_SELECTOR, "div[class='card-information__wrapper']")
    Products_Prices = (By.CSS_SELECTOR, "span[class*= 'sale price-item--last']")

    def search_page(self):
        self.driver.get('https://shop.cureskin.com/search?q=cure')

    def sort_price(self):
        select = Select(self.driver.find_element(*self.Sort_Selection))
        select.select_by_value('price-ascending')
        time.sleep(2)
        select.select_by_value('price-descending')
        time.sleep(2)
        pass
        #self.driver.wait.until(EC.)

    def filter(self):

        all_products=self.driver.find_elements(*self.results)
        print(all_products)

        prices_list = []
        for prices in all_products:
            Price = prices.find_element(*self.Products_Prices).text
            prices_list.append(float(Price.split(" ")[1]))
        print(prices_list)
        #assert sorted(Prices) == Prices, f'The prices are not sorted in ascending order'




