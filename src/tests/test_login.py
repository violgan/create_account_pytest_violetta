from src.all_imports import *
import src.utilities as utils

data = utils.load_yaml((f"{utils.ROOT_DIR}/data/config.yaml"))
# data_neg = utils.load_yaml(f"{utils.ROOT_DIR}/data/login_scenarios/login_negative.yml")

@pytest.mark.login1
def test_login_case1(driver):
    print("This is it, I am doing my first framework!")
    utils.LOG.info("test_login_case1 started ...")
    utils.LOG.debug("Debug message....")
    utils.LOG.error("I am an exceptional case")
    utils.LOG.warning("Something does not seem to be right, but not an error")
    utils.LOG.critical("WOUUUW STOP NOW, CAN NOT RUN ANYTHING")

    # driver.get("http://automationpractice.com/index.php")
    # time.sleep(10)

    web_url = data['scenario1']['web_url']
    username = data['scenario1']['username']
    pswd = data['scenario1']['password']

    login_page = LoginPage(driver)

    driver.get(web_url)
    print(f"opened the browser and website : {web_url}")
    time.sleep(1)

    login_page.click_sign_in_link()
    login_page.enter_email(username)
    login_page.enter_password(pswd)
    login_page.click_sign_in_button()
    utils.LOG.info("We are able to sign in now")
    time.sleep(5)
    login_page.take_screenshot("HomePage")
    time.sleep(5)
    login_page.sign_out()
    utils.LOG.info("test_login_case1_completed")

# @pytest.mark.login
# @pytest.mark.loginNegative
# def test_login_case2(driver):
#     pass
#     web_url = data_neg['scenario1']['web_url']
#     username = data_neg['scenario1']['username']
#     pswd = data_neg['scenario1']['password']




