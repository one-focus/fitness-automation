import datetime

from behave import *

from pages import MainPage


@step('enter {card_type} details')
def step_impl(context, card_type):
    if card_type == 'fake card':
        context.current_page.type_in('cardnumber field', '5555555555554444')
        context.current_page.type_in('month field', '10')
        context.current_page.type_in('year field', '22')
        context.current_page.type_in('cardholder field', 'USERNAME USERNAME')
        context.current_page.type_in('cvc field', '222')
        context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
        context.current_page.click_on('pay button')
    elif card_type == 'real card':
        context.current_page.type_in('cardnumber field', '4214870006156277')
        context.current_page.type_in('month field', '12')
        context.current_page.type_in('year field', '24')
        context.current_page.type_in('cardholder field', 'USERNAME USERNAME')
        context.current_page.type_in('cvc field', '000')
        context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
        context.current_page.click_on('pay button')