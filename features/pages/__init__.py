from .main_page import MainPage
from .confirmation_page import ConfirmationPage

page_map = {
    "main": MainPage,
    "confirmation": ConfirmationPage
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
