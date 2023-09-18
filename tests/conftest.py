import os
import pytest

from selene import browser
from selenium import webdriver

from template_tests.utils import attach

options = webdriver.ChromeOptions()


@pytest.fixture(scope='function', autouse=True)
def browser_opt():
    browser.config.base_url = 'https://innoseti.ru/'
    options.add_argument('window-size=1920,1080')

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }

    # browser.config.driver_options = options

    options.capabilities.update(selenoid_capabilities)

    browser.config.driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
