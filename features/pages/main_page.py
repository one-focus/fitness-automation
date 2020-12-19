from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def _elements_map(self):
        return {
            "activate button": (By.XPATH, '//*[@data-id="email"]'),
            "email field": (By.NAME, 'email'),
            "next button": (By.NAME, 'external'),

            "policy link": (By.XPATH, '//a[@href="https://zhiry-net.ru/about/privacy/"]'),
            "oferta link": (By.XPATH, '//a[@href="https://zhiry-net.ru/about/oferta/"]')
        }

    def _verify_page(self):
        self.on_this_page('oferta link', "policy link")
