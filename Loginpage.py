from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginData:
    # Test Data
    url = "https://www.guvi.in/"
    username = "nandhinibalu72@gmail.com"
    password = "Nivan@10"

class Loginpage:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'login-btn').click()

    def fetchurl(self):
        return self.url

    def fetchsigninurl(self):
        self.start()
        return self.driver.current_url

    def validate_username_input_box(self):
        try:
            username_input_box = self.driver.find_element(By.ID, 'email')
            return username_input_box.is_displayed() and username_input_box.is_enabled()
        except:
            return False

    def validate_password_input_box(self):
        try:
            password_input_box = self.driver.find_element(By.ID, 'password')
            return password_input_box.is_displayed() and password_input_box.is_enabled()
        except:
            return False

    def validate_login_button(self):
        try:
            login_button = self.driver.find_element(By.ID, 'login-btn')
            return login_button.is_displayed() and login_button.is_enabled()
        except:
            return False

    def validate_login(self):
        try:
            self.start()
            self.driver.find_element(By.ID, 'email').send_keys(LoginData.username)
            sleep(2)
            self.driver.find_element(By.ID, 'password').send_keys(LoginData.password)
            sleep(2)
            self.driver.find_element(By.ID, 'login-btn').click()
            sleep(4)
            return True
        except:
            print("login failed")
            return False
    def shutdown(self):
        self.driver.quit()
