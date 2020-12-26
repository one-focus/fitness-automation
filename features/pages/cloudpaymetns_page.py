from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CloudPayments(BasePage):

    @property
    def _elements_map(self):
        return {
            'iframe': (By.TAG_NAME, 'iframe'),

            'cardnumber field': (By.ID, 'cardNumber'),
            'cardnumber label': (By.XPATH, '//label[@for="cardNumber"]'),
            'month field': (By.ID, 'inputMonth'),
            'year field': (By.ID, 'inputYear'),
            'cardholder field': (By.ID, 'cardHolder'),
            'cvc field': (By.ID, 'cardCvv'),
            'pay button': (By.XPATH, '//*[@id="sizingContainer"]//button'),

            '3d secure widget': (By.ID, 'pwdInputVisible'),
            'repeat button': (By.XPATH, '//*[@id="statusContainer"]//button[1]'),
            'cancel button': (By.XPATH, '//*[@id="statusContainer"]//button[2]'),
        }

    def _verify_page(self):
        self.on_this_page('iframe')
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
