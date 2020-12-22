from .main_page import MainPage
from .alfabank_page import AlfaBank
from .cloudpaymetns_page import CloudPayments
from .confirmation_page import ConfirmationPage

page_map = {
    "main": MainPage,
    "alfabank": AlfaBank,
    "confirmation": ConfirmationPage,
    "cloudpayments": CloudPayments
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
