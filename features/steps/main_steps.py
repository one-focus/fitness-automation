from behave import *

from pages import MainPage


@step('I open {page_name} page')
def step_impl(context, page_name):
    base_url = context.config.get('settings', 'base_url')
    if page_name == "home":
        context.driver.get(f'{base_url}')
        context.current_page = MainPage(context.driver)
