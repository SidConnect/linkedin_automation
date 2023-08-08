from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_profile_dashboard(self):
        '''To click on the profile and navigate to Profile page'''
        profile_element = self.driver.find_element(By.XPATH,
                                                   "//div[@class='share-box-feed-entry__avatar']//img[@alt='Visit profile for Rohan Jain']")
        profile_element.click()

    def get_notifications_count(self):
        '''To get the number of notifications if any'''
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


