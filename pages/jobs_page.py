import time
import pdb
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class JobsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_job_details(self):
        """To get the job description into a list"""
        time.sleep(5)
        job_cards = []
        job_details_list = []

        for i in range(25):
            job_cards_container = self.driver.find_element(By.XPATH,
                                                           "//ul[@class='scaffold-layout__list-container']")
            job_cards = job_cards_container.find_elements(By.XPATH,
                                                          "//div[@class='job-card-list__entity-lockup "
                                                          "artdeco-entity-lockup artdeco-entity-lockup--size-4 "
                                                          "ember-view']")

            # Scroll the last element into view to load more job cards
            if job_cards:
                last_job_card = job_cards[-1]
                self.driver.execute_script("arguments[0].scrollIntoView()", last_job_card)

                # Wait for new job cards to be visible
                try:
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                                "//div[@class='job-card-list__entity-lockup artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view']")))
                except TimeoutException:
                    break

        for i in range(len(job_cards)):
            job_card = job_cards[i]

            job_title_element = job_card.find_element(By.XPATH,
                                                      ".//div[@class='full-width artdeco-entity-lockup__title ember-view']")
            company_name_element = job_card.find_element(By.XPATH,
                                                         ".//div[@class='artdeco-entity-lockup__subtitle ember-view']")
            job_location_element = job_card.find_element(By.XPATH,
                                                         ".//div[@class='artdeco-entity-lockup__caption ember-view']")

            job_title = job_title_element.text
            company_name = company_name_element.text
            job_location = job_location_element.text

            clickable_element = job_card.find_element(By.XPATH,
                                                      ".//a[@class='disabled ember-view job-card-container__link job-card-list__title']")

            clickable_element.click()
            time.sleep(4)

            job_description_element = self.driver.find_element(By.XPATH, "//*[@id=\"job-details\"]/span")
            job_description = job_description_element.text

            job_details = {
                "Job Title": job_title,
                "Company Name": company_name,
                "Job Location": job_location,
                "Job Description": job_description
            }

            job_details_list.append(job_details)

            # print("Job Title:", job_title)
            # print("Company Name:", company_name)
            # print("Job Location:", job_location)
            # print("Job Description: ", job_description)

        job_details_df = pd.DataFrame(job_details_list)

        return job_details_df

        # write_to_excel(job_details_df, "data/post_data.xlsx", "Job Details")

    def search(self, search_tag):
        '''To search for a search prompt on the search bar in jobs page.'''
        self.driver.get("https://www.linkedin.com/jobs/")

        input_field = self.driver.find_element(By.XPATH,
                                               "//input[@class='jobs-search-box__text-input jobs-search-box__keyboard-text-input']")
        input_field.click()
        input_field.send_keys(search_tag)
        time.sleep(2)
        input_field.send_keys(Keys.ENTER)

    def go_to_page(self, to_page):
        try:
            next_page = self.driver.find_element(By.XPATH, f".//button[@aria-label='Page {to_page}']")
            next_page.click()
            time.sleep(5)
        except:
            print("No more pages found")

