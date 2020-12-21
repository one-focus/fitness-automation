from behave import *

from pages import MainPage


@step('open {page_name} page')
def step_impl(context, page_name):
    if page_name.startswith(('http', 'www')):
        url = page_name
    else:
        url = context.config.get('websites', page_name)
    context.driver.get(url)
    context.current_page = MainPage(context.driver)


@when("go to {page_name} page")
def step_impl(context, page_name):
    if page_name == 'confirmation':
        context.execute_steps('''
                        When scroll down
                        And click on activate button
                        And click on email field
                        And type "random" in email field
                        When clear time
                        And click on next button
                        Then I am on confirmation page
                        ''')
    elif page_name == 'cloudpayments':
        context.execute_steps('''
                        Given click on confirm checkbox
                        When clear time
                        And click on continue button
                        Then I am on cloudpayments page
                        ''')
