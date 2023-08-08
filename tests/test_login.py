import time
import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def login_page(driver):
    return LoginPage(driver)

@pytest.mark.order(1)
def test_valid_login(login_page, test_logger):
    login_page.open()
    login_page.enter_username("rohanjain0781@gmail.com")
    login_page.enter_password("Townhall@12")
    login_page.click_login()

    time.sleep(5)
    test_logger.info("Login test - SUCCESS")
