from src.all_imports import *
import src.utilities as utils

data = utils.load_yaml((f"{utils.ROOT_DIR}/data/config.yaml"))

@pytest.mark.account1
def test_createaccount_case1(driver):
    print("This is it, I am doing my first framework!")
    utils.LOG.info("test_createaccount started ...")
    utils.LOG.debug("Debug message....")
    utils.LOG.error("I am an exceptional case")
    utils.LOG.warning("Something does not seem to be right, but not an error")
    utils.LOG.critical("WOUUUW STOP NOW, CAN NOT RUN ANYTHING")

    web_url = data['scenario1']['web_url']
    username = data['scenario1']['username']
    pswd = data['scenario1']['password']
    name = data['scenario1']['firstname']
    lastname = data['scenario1']['lastname']


    account_page = AccountPage(driver)

    driver.get(web_url)
    print(f"opened the browser and website : {web_url}")
    time.sleep(1)

    account_page.click_sign_in_link()
    account_page.take_screenshot("Home page")
    account_page.enter_email(username)
    account_page.take_screenshot("Create account link")
    account_page.click_create_account()
    account_page.click_title()
    account_page.enter_name(name)
    account_page.enter_lastname(lastname)
    account_page.create_password(pswd)
    account_page.select_day("15")
    account_page.select_month("2")
    account_page.select_year("1988")
    account_page.input_address("1111 86th St")
    account_page.input_city("Brooklyn")
    account_page.click_state("32")
    account_page.take_screenshot("Account info part 1")
    account_page.enter_zip("11214")
    account_page.enter_phone("9999999999")
    account_page.take_screenshot("Account info part 2")
    account_page.click_register()
    account_page.take_screenshot("My account page")
    account_page.checking_if_account_opened()








