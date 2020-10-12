from telnetlib import EC

from selenium.webdriver.support.select import Select

from src.all_imports import *
import src.utilities as utils
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wwait = WebDriverWait(driver, 10)

    def click_element_by_xpath(self, xpath):
        """
           this method finds the element by xpath and clicks it
           :param xpath: correct unique xpath of single element
           """
        try:
            print(f"xpath provided: {xpath}")
            #element = driver.find_element_by_xpath(xpath)
            element = self.wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            utils.LOG.info("clicking the element")
            element.click()
        except NoSuchElementException as err:
            utils.LOG.error(f"Check element by following xpath")
            utils.LOG.error(err)
            self.take_screenshot('ErrorClickElement')

    def enter_text_by_xpath(self, xpath, some_text):
        """
           this method finds the element by xpath and clicks it
           :param xpath: correct unique xpath of single element
           """
        try:
            print(f"xpath provided: {xpath}")
            element = self.wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

            utils.LOG.info(f"entering thje following text: {some_text}")
            element.send_keys(some_text)
        except NoSuchElementException as err:
            utils.LOG.warning(f"Entering Text failed by following xpath: {xpath}")
            utils.LOG.error(err)
            self.take_screenshot('ErrorEnterText_')

    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element, "color: green; border: 2px solid green;")
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element, "")
        utils.LOG.info("Element highlighted")

    def take_screenshot(self, message=""):
        timestmp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        # ROOT_DIR = dirname(dirname(abspath(__file__)))
        file_location = f"{utils.ROOT_DIR}/screenshots/"
        file_name = message + timestmp + ".png"
        full_file_path = file_location + file_name
        self.driver.save_screenshot(full_file_path)
        # driver.get_screenshot_as_png(message + timestmp)
        utils.LOG.info("screenshot was taken and completed.")

    def get_text_by_xpath(self, xpath: str) -> str:
        try:
            print(f"xpath provided: {xpath}")
            #element = driver.find_element_by_xpath(xpath)
            element = self.wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            utils.LOG.info("getting the element text")
            return element.text
        except NoSuchElementException as err:
            utils.LOG.warnings(f"Check element by following xpath: {xpath}")
            utils.LOG.error(err)
            self.take_screenshot('ErrorGetText_')

    def test_drop_down_list(self, xpath, value):
        # # try:
        #
        #     # dd_list_xpath = "//select[@id='carselect']"  # real ddown that selenium can handle
            element = self.wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))


        #     utils.LOG.info("clicking the dd_list")
            element.click()
            select = Select(element)  # !!!!!!!!!!
            # text_options = [option.text for option in day_selection.options]
            # print("Options available in the list: ", text_options)

            select.select_by_value(value)
            # text_selected_ones = [option.text for option in day_selection.all_selected_options]
            # utils.LOG.info("Options selected: ", text_selected_ones)

        # except NoSuchElementException as err:
        #     utils.LOG.error(f"Check element by following xpath")
        #     utils.LOG.error(err)
        #     self.take_screenshot('ErrorClickElement')




