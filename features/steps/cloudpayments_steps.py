from behave import *

from pages import MainPage


@step('I enter card details')
def step_impl(context):
    context.current_page.type_in('cardnumber field', '5555555555554444')
    context.current_page.type_in('month field', '10')
    context.current_page.type_in('year field', '22')
    context.current_page.type_in('cardholder field', 'ANDREY KARDASH')
    context.current_page.type_in('cvc field', '222')
    context.current_page.click_on('pay button')
