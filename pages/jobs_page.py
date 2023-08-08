from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys


class JobsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_job_cards(self):
        """To get the job description into a list"""

        pytest.set_trace()

        job_cards_container = self.driver.find_element(By.XPATH, "//ul[@class='scaffold-layout__list-container']")

        job_cards = job_cards_container.find_elements(By.TAG_NAME, "li")

        for job_card in job_cards:
            company_name = job_card.find_element(By.XPATH, "//div[@class='artdeco-entity-lockup__subtitle ember-view']//span[@class='job-card-container__primary-description ']").text
            print(company_name)

        job_details = self.driver.find_element(By.XPATH, "//*[@id=\"job-details\"]/span").text
        print(job_details)
    def search(self, search_tag):
        '''To search for a search prompt on the search bar in jobs page.'''
        self.driver.get("https://www.linkedin.com/jobs/")

        input_field = self.driver.find_element(By.XPATH, "//input[@class='jobs-search-box__text-input jobs-search-box__keyboard-text-input']")

        self.driver.execute_script("arguments[0].value = arguments[1]", input_field, search_tag)

        input_field.send_keys(Keys.ENTER)