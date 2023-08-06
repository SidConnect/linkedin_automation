from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    def get_followers_count(self):
        try:
            followers_element = self.driver.find_element(By.XPATH, "//a[@class='ember-view link-without-visited-state']//span[@class='t-bold']")
            followers_count = followers_element.text
            return followers_count
        except NoSuchElementException:
            return 0

    def get_connections_count(self):
        try:
            connections_element = self.driver.find_element(By.XPATH, "//span[@class='link-without-visited-state']//span[@class='t-bold']")
            connections_count = connections_element.text
            return connections_count
        except NoSuchElementException:
            return 0


    def navigate_to_homepage(self):
        try:
            homepage_element = self.driver.find_element(By.XPATH, "//*[@id=\"global-nav\"]/div/nav/ul/li[1]")
            homepage_element.click()
        except NoSuchElementException:
            print("Could not navigate to Home Page")





