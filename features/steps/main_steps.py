import random
import string
from datetime import datetime, timezone, timedelta

from behave import *

import pages
import steps
from pages import MainPage


@step('open {page_name} page')
def step_impl(context, page_name):
    if page_name.startswith(('http', 'www')):
        url = page_name
    else:
        url = context.config.get('websites', page_name)
    context.landing = page_name
    context.driver.get(url)
    context.current_page = MainPage(context.driver)


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


@when("go to {page_name} page")
def step_impl(context, page_name):
    if page_name == 'confirmation':
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        context.current_page.click_on('activate button')
        context.current_page.click_on('email field')
        context.current_page.type_in('email field', f"{random_char(7)}@{random_char(7)}.com")
        context.time = datetime.now(timezone.utc) + timedelta(hours=3)
        context.current_page.click_on('next button')
    elif page_name in ('alfabank', 'cloudpayments'):
        context.current_page.click_on('confirm checkbox')
        context.time = datetime.now(timezone.utc) + timedelta(hours=3)
        context.current_page.click_on('continue button')
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)
