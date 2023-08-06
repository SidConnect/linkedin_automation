from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://in.linkedin.com/")
        self.driver.maximize_window()

    def enter_username(self, username):
        username_field = self.driver.find_element(By.XPATH, "//*[@id=\"session_key\"]")
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, "//*[@id=\"session_password\"]")
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, "//*[@id=\"main-content\"]/section[1]/div/div/form[1]/div[2]/button")
        login_button.click()

