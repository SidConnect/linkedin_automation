import os.path
import pytest
from selenium import webdriver
import logging
from pages.home_page import HomePage

logs_directory = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(logs_directory, exist_ok=True)

# Configure the logging settings
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=os.path.join(logs_directory, "automation.log"),
                    filemode='w')

# Logger instance
logger = logging.getLogger()


@pytest.fixture(scope="function")
def test_logger(request):
    test_name = request.node.name

    # create a logger for the specific test
    test_logger = logging.getLogger(test_name)

    yield test_logger

    test_logger.handlers.clear()


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
@pytest.fixture(scope='module')
def home_page(driver):
    return HomePage(driver)
