from pages.main_page import MainPage
from pages.searchresults_page import Searchpage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.searchresults_page = Searchpage(self.driver)


