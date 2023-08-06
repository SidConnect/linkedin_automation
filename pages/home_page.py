from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_profile_dashboard(self):
        profile_element = self.driver.find_element(By.XPATH,
                                                   "//div[@class='share-box-feed-entry__avatar']//img[@alt='Visit profile for Rohan Jain']")
        profile_element.click()

    def get_notifications_count(self):
        try:
            notification_element = self.driver.find_element(By.XPATH,
                                                            "//span[@class='notification-badge notification-badge--show ']//span[@class='a11y-text']")
            notifications_count = notification_element.text
            return notifications_count
        except NoSuchElementException:
            return 0

    def start_a_new_post(self):
        try:
            new_post_element = self.driver.find_element(By.XPATH,
                                                        "//button[@class='artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger']//span")
            new_post_element.click()
        except NoSuchElementException as e:
            return 0

    def search(self, search_tag):

        self.driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/div/nav/ul/li[3]").click()
        input_field = self.driver.find_element(By.XPATH,
                                               "//input[@class='jobs-search-box__text-input jobs-search-box__keyboard-text-input']")
        input_field.click()
        input_field.send_keys(search_tag)
        input_field.send_keys(Keys.ENTER)

    def get_job_cards(self):


        job_cards = self.driver.find_elements(By.XPATH, "//ul[@class='scaffold-layout__list-container']//li")
        print(job_cards)
