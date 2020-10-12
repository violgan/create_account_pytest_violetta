from src.all_imports import *
import src.utilities as utils
import time

class AccountPage (BasePage):
    #Locators
    sign_in_link = "//a[@class='login']"
    create_account = "//button[@id='SubmitCreate']"
    email_input = "//input[@id='email_create']"
    gender = "//div[@id='uniform-id_gender2']"
    first_name = "//input[@id='customer_firstname']"
    last_name = "//input[@id='customer_lastname']"
    password_create = "//input[@id='passwd']"
    day_of_birth = "//select[@id='days']"
    month_of_birth = "//select[@id='months']//option"
    year_of_birth = "//select[@id='years']//option"
    address = "//input[@id='address1']"
    city = "//input[@id='city']"
    state = "//select[@id='id_state']//option[1]"
    zip = "//input[@id='postcode']"
    phone = "//input[@id='phone_mobile']"
    register_button = "//button[@id='submitAccount']"

    #methods
    def click_sign_in_link(self):
        self.click_element_by_xpath(self.sign_in_link)
        time.sleep(2)

    def enter_email(self, email):
        self.enter_text_by_xpath(self.email_input, email)
        utils.LOG.info(f"email entered {email}")

    def click_create_account(self):
        self.click_element_by_xpath(self.create_account)
        time.sleep(2)

    def click_title(self):
        self.click_element_by_xpath(self.gender)
        time.sleep(2)


    def enter_name(self, firstname):
        self.enter_text_by_xpath(self.first_name, firstname)
        time.sleep(2)
        utils.LOG.info(f"First name entered {firstname}")

    def enter_lastname(self, lastname):
        self.enter_text_by_xpath(self.last_name, lastname)
        time.sleep(2)
        utils.LOG.info(f"Last name entered {lastname}")

    def create_password(self, password):
        self.enter_text_by_xpath(self.password_create, password)
        time.sleep(2)
        utils.LOG.info(f"Password entered {password}")

    def select_day(self, day):
        self.test_drop_down_list(self.day_of_birth, day)
        time.sleep(2)
        utils.LOG.info(f"Selected: {day}")

    def select_month(self, month):
        self.test_drop_down_list(self.month_of_birth, month)
        time.sleep(2)
        utils.LOG.info(f"Selected: {month}")

    def select_year(self, year):
        self.test_drop_down_list(self.year_of_birth, year)
        time.sleep(2)
        utils.LOG.info(f"Selected: {year}")

    def input_address(self, full_address):
        self.enter_text_by_xpath(self.address, full_address)
        time.sleep(2)
        utils.LOG.info(f"Address entered {full_address}")

    def input_city(self, city):
        self.enter_text_by_xpath(self.city, city)
        time.sleep(2)
        utils.LOG.info(f"City entered {city}")


    def click_state(self, value):
        self.test_drop_down_list(self.state, value)
        time.sleep(2)
        utils.LOG.info(f"Selected: {value} value")








    def enter_password(self, password):
        self.enter_text_by_xpath(self.password_input,password)
        time.sleep(2)
        utils.LOG.info(f"email entered {password}")

    def click_sign_in_button(self):
        self.click_element_by_xpath(self.sign_in_button)
        utils.LOG.info("Sign in button clicked.")
        time.sleep(1)

    def sign_out(self):
        self.click_element_by_xpath(self.sign_out_link)
        utils.LOG.info("Signed out from the website.")

    def get_app_message(self):
        return self.get_text_by_xpath(self.message_xpath)
