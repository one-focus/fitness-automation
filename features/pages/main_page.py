from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def _elements_map(self):
        return {
            "activate button": (By.XPATH,
                                '(//*[@data-id="email"]|//section[@id="prise_3"]//div[@class="prise_one silver"]//a[@data-product-id="5010"])'),
            "email field": (By.NAME, 'email'),
            "next button": (
            By.XPATH, '//button[@type="submit"]'),

            "policy link": (By.XPATH, '//a[@href="https://zhiry-net.ru/about/privacy/"]'),
            "oferta link": (By.XPATH, '//a[@href="https://zhiry-net.ru/about/oferta/"]')
        }

    def _verify_page(self):
        pass
        # self.on_this_page('oferta link', "policy link")
