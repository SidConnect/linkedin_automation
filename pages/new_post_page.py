import time

from selenium.webdriver.common.by import By
import pyautogui


class NewPostPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_post_content(self, post_content):
        post_textbox = self.driver.find_element(By.XPATH, "//div[@class='editor-content ql-container']//div[@class='ql-editor ql-blank']")
        post_textbox.send_keys(post_content)
        time.sleep(2)

    def enter_attachment(self, attachment_path, post_idea):

        add_image_button = self.driver.find_element(By.XPATH,
                                                    "//span[@class='share-promoted-detour-button__icon-container']")
        add_image_button.click()
        time.sleep(5)

        pyautogui.typewrite(attachment_path)
        pyautogui.press("enter")
        time.sleep(3)

        done_button = self.driver.find_element(By.XPATH, "//button[@class='share-box-footer__primary-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
        done_button.click()

    def create_post(self):

        done_button = self.driver.find_element(By.XPATH, "//button[@class='share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
        done_button.click()
