# from src.all_imports import *
#
#
# WIN_HANDLE_MAIN = None
#
# def launch_website(url):
#     driver.get(url)
#     print(f"opened the browser and google website : {url}")
#     time.sleep(3) #thread.sleep() in java
#
# def click_element_by_xpath(xpath):
#     """
#        this method finds the element by xpath and clicks it
#        :param xpath: correct unique xpath of single element
#        """
#     try:
#         print(f"xpath provided: {xpath}")
#         element = driver.find_element_by_xpath(xpath)
#         print("clicking the element")
#         element.click()
#     except NoSuchElementException as err:
#         print(f"Check element by following xpath")
#         print(err)
#
#
#
# def enter_text_by_xpath(xpath, some_text):
#     """
#        this method finds the element by xpath and clicks it
#        :param xpath: correct unique xpath of single element
#        """
#     try:
#         print(f"xpath provided: {xpath}")
#         element = driver.find_element_by_xpath(xpath)
#         print(f"entering thje following text: {some_text}")
#         element.send_keys(some_text)
#     except NoSuchElementException as err:
#         print(f"Entering Text failed by following xpath")
#         print(err)
#
# def wed_driver_properties():
#     '''3. using WebDriver class properties'''
#     print('Current url: ', driver.current_url)
#     print('Current title: ', driver.title)
#     print('Current win_handle: ', driver.current_window_handle)
#     print('Current name: ', driver.name)
#
#
# def close_browser():
#     wed_driver_properties()
#     driver.quit()
#     print("browser is closed")
#
#
# def login_to_automation_practice(url, email, password):
#     '''
#     # ********** Scenario to login ********
#     # Create an account
#     # username: itsme@gmail.com, password: $Password001
#     # identify all locators by inspecting on browser (xpath, optional: id, css selectors)
#     # sign_in_link "//a[@class='login']" incorrect XPATH , to see Try except
#     '''
#
#     sign_in_link = "//a[@class='login']"
#     email_input = "//input[@id='email']"
#     password_input = "//input[@id='passwd']"
#     sign_in_button = "//button[@id='SubmitLogin']"
#     sign_out_link = "//a[@class='logout']"
#
#
#     #Steps:
#     launch_website(url)
#     click_element_by_xpath(sign_in_link)
#     # time.sleep(2)
#     enter_text_by_xpath(email_input, email)
#     enter_text_by_xpath(password_input, password)
#     click_element_by_xpath(sign_in_button)
#     time.sleep(10)
#     take_screenshot('signin')
#     utils.LOG.info("Successfully signed in")
#     utils.LOG.info("Signing out now...")
#     click_element_by_xpath(sign_out_link)
#     close_browser()
#
# def take_screenshot(message=""):
#     timestmp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
#     #ROOT_DIR = dirname(dirname(abspath(__file__)))
#     file_location = f"{ROOT_DIR}/screenshots/"
#     file_name = message + timestmp + ".png"
#     full_file_path = file_location + file_name
#     driver.save_screenshot(full_file_path)
#     #driver.get_screenshot_as_png(message + timestmp)