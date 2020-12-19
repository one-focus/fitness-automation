from .main_page import MainPage
from .cloudpaymetns_page import CloudPayments
from .confirmation_page import ConfirmationPage

page_map = {
    "main": MainPage,
    "confirmation": ConfirmationPage,
    "cloudpayments": CloudPayments
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
