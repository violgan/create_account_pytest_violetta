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
    # day = data['scenario1']['day']
    month = data['scenario1']['mon']
    year = data['scenario1']['year']
    full_address = data['scenario1']['address']
    city = data['scenario1']['city']

    account_page = AccountPage(driver)

    driver.get(web_url)
    print(f"opened the browser and website : {web_url}")
    time.sleep(1)

    account_page.click_sign_in_link()
    account_page.enter_email(username)
    account_page.click_create_account()
    account_page.click_title()
    account_page.enter_name(name)
    account_page.enter_lastname(lastname)
    account_page.create_password(pswd)
    account_page.select_day("2")
    account_page.select_month(month)
    account_page.select_year(year)
    account_page.input_address(full_address)
    account_page.input_city(city)
    account_page.click_state("32")






