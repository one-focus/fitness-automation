import configparser

import allure
import telebot
from allure_commons.types import AttachmentType
from selenium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

# TODO check all context attributes on https://behave.readthedocs.io/en/latest/context_attributes.html#user-attributes
from utils.google_sheets import GoogleSheets


def before_all(context):
    caps = {
        # -- Chrome Selenoid options
        'browserName': 'chrome',
        'version': '87.0',
        'selenoid:options':
            {
                'enableVNC': True,
                'enableVideo': False
            },
        # -- Chrome browser mobile emulation and headless options
        'goog:chromeOptions': {
            'mobileEmulation': {'deviceName': 'iPhone X'},
            # 'args': ['headless']
        }
    }
    '''
        -- Android browser Selenoid options
        "browserName": "android",
        "version": "9.0",
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    
        -- Android native app Selenoid options
        'deviceName': 'android',  # not browserName
        'version': '9.0',
        'app': 'path/to/instagram.apk',
        'appActivity': 'com.instagram.mainactivity.LauncherActivity',
        'appPackage': 'com.instagram.android',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': False
        }
    '''

    # -- Local driver
    context.driver = webdriver.Chrome(desired_capabilities=caps)

    # -- Remote driver
    # context.driver = webdriver.Remote(command_executor='http://0.0.0.0:4444/wd/hub', desired_capabilities=caps)
    # context.driver = webdriver.Remote(command_executor='http://159.65.195.102:4444/wd/hub', desired_capabilities=caps)

    context.driver.implicitly_wait(1)

    # read config
    parser = configparser.ConfigParser()
    parser.read('behave.ini')
    context.config = parser

    context.data_worksheet = GoogleSheets().authorize('Data')


# def before_feature(context, feature):
#     # retry failures
#     for scenario in feature.scenarios:
#         # if "flaky" in scenario.effective_tags:
#         patch_scenario_with_autoretry(scenario, max_attempts=2)


# def before_scenario(context, scenario):
#     context.driver.delete_all_cookies()


def after_step(context, step) -> None:
    if step.status == 'failed':
        bot = telebot.TeleBot("1461082086:AAGUnZJyEcDwkW1LPHLmezbrXEDzIu6nD8k")
        bot.send_photo(chat_id=-447406725, photo=context.driver.get_screenshot_as_png(), caption=step.name)
        allure.attach('screenshot', context.driver.get_screenshot_as_png(), type=AttachmentType.PNG)


def after_all(context):
    context.driver.quit()
