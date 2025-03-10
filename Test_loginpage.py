from Loginpage import Loginpage, LoginData

class Testloginautomation:
    def setup_method(self):
        self.login = Loginpage(LoginData.url)

    def teardown_method(self):
        self.login.shutdown()

    def test_positive_validateurl(self):
        actualurl = self.login.fetchurl()
        expected_url = "https://www.guvi.in/"
        assert expected_url == actualurl
        print("Test case Pass: Valid URL is launched")
    def test_negative_validateurl(self):
        actualurl = self.login.fetchurl()
        expected_url = "https://www.amazon.in/"
        assert expected_url != actualurl
        print("Test case Pass: URL is not matched")

    def test_positive_validatesigninurl(self):
        homeurl = self.login.fetchsigninurl()
        expectedhome_url = "https://www.guvi.in/sign-in/"
        assert expectedhome_url == homeurl
        print("Test case Pass: Home Page URL is matched")

    def test_negative_validatesigninurl(self):
        homeurl = self.login.fetchsigninurl()
        expectedhome_url = "https://saucedemo.com/"
        assert expectedhome_url != homeurl
        print("Test case Pass: Home Page URL is not matched")

    def test_loginform(self):
        self.login.validate_login()
        self.login.validate_username_input_box()
        self.login.validate_password_input_box()
        self.login.validate_login_button()
        print("Test case Pass: Login Done")
        