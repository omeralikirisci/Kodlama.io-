from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date


class Test_SwagLabs:
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.WaitForElementVisibility((By.ID, "user-name"))
        self.WaitForElementVisibility((By.ID, "password"))

        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    # her testden sonra çağırılır
    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password", [("1", "1"), ("kullanıcı_1", "pass_1")])
    def test_denied_login(self, username, password):
        usernameinput = self.driver.find_element(By.ID, "user-name")
        passwordinput = self.driver.find_element(By.ID, "password")
        usernameinput.send_keys(username)
        passwordinput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errormessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(
            f"{self.folderPath}/test-invald-login-{username}-{password}.png")
        assert errormessage.text == 'Epic sadface: Username and password do not match any user in this service'

    def test_one_empty_login(self):
        uiInput = self.driver.find_element(By.ID, "user-name")
        uiInput.send_keys("standard_user")
        entry = self.driver.find_element(By.ID, "login-button")
        entry.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(
            f"{self.folderPath}/test-user-standard_user-error-mesage.png")
        assert errorMessage.text == 'Epic sadface: Password is required'

    def test_lockedOutUser(self):
        uiInput = self.driver.find_element(By.ID, "user-name")
        uiInput.send_keys("locked_out_user")
        uipInput = self.driver.find_element(By.ID, "password")
        uipInput.send_keys("secret_sauce")
        entry = self.driver.find_element(By.ID, "login-button")
        entry.click()
        locked_out_usermessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(
            f"{self.folderPath}/test-lockedOutUser.png")
        assert locked_out_usermessage.text == 'Epic sadface: Sorry, this user has been locked out.'

    def test_x_icon(self):
        ctrl = 0
        self.WaitForElementVisibility((By.ID, "login-button"))
        entry = self.driver.find_element(By.ID, "login-button")
        entry.click()
        self.WaitForElementVisibility(
            (By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg"))
        x_icon = self.driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        if x_icon.is_displayed():
            self.driver.save_screenshot(
                f"{self.folderPath}/test-x-icon-appeared.png")
            ctrl += 1
        error_message_for_x = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        error_message_for_x.click()

        try:

            x_icon.is_displayed()

        except:
            ctrl += 1

            self.driver.save_screenshot(
                f"{self.folderPath}/test-x-icon-disappeared.png")

        assert ctrl == 2

    def test_standard_user(self):
        uiInput = self.driver.find_element(By.ID, "user-name")
        uiInput.send_keys("standard_user")
        uipInput = self.driver.find_element(By.ID, "password")
        uipInput.send_keys("secret_sauce")
        entry = self.driver.find_element(By.ID, "login-button")
        entry.click()
        self.WaitForElementVisibility(
            (By.CLASS_NAME, "inventory_item_description"))
        self.driver.save_screenshot(
            f"{self.folderPath}/test-standard_user-entrance-successful.png")
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    def test_count_of_product(self):
        uiInput = self.driver.find_element(By.ID, "user-name")
        uiInput.send_keys("standard_user")
        uipInput = self.driver.find_element(By.ID, "password")
        uipInput.send_keys("secret_sauce")
        entrance = self.driver.find_element(By.ID, "login-button")
        entrance.click()
        self.WaitForElementVisibility(
            (By.CLASS_NAME, "inventory_item_description"))
        listofproducts = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_description")
        self.driver.save_screenshot(f"{self.folderPath}/test-ürün-listesi.png")
        assert len(listofproducts) == 6

    def test_shopping_basket(self):
        uiInput = self.driver.find_element(By.ID, "user-name")
        uiInput.send_keys("standard_user")
        uipInput = self.driver.find_element(By.ID, "password")
        uipInput.send_keys("secret_sauce")
        entry = self.driver.find_element(By.ID, "login-button")
        entry.click()
        self.WaitForElementVisibility(
            (By.ID, "add-to-cart-sauce-labs-backpack"))
        addToCart1 = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
        addToCart2 = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bike-light")
        addToCart3 = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        addToCart4 = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        addToCart5 = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")
        addToCart6 = self.driver.find_element(
            By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        basket = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        ActionChains(self.driver).click(addToCart1).click(addToCart2).click(addToCart3).click(
            addToCart4).click(addToCart5).click(addToCart6).click(basket).perform()
        self.WaitForElementVisibility((By.ID, "checkout"))
        countsofprd = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_name")
        self.driver.save_screenshot(
            f"{self.folderPath}/test-count.png")
        assert len(countsofprd) == 6

    # yeni 2
    @pytest.mark.parametrize("socialXPATH,socialLink,socialname", [("/html/body/div/div/footer/ul/li[1]/a", "https://twitter.com/saucelabs", "twitter"), ("/html/body/div/div/footer/ul/li[2]/a", "https://www.facebook.com/saucelabs", "facebook"), ("/html/body/div/div/footer/ul/li[3]/a", "https://www.linkedin.com/company/sauce-labs/?original_referer=", "lşnkedin")])
    def test_socialHub(self, socialXPATH, socialLink, socialname):
        uiInput = self.driver.find_element(By.ID, "user-name")
        uiInput.send_keys("standard_user")
        uipInput = self.driver.find_element(By.ID, "password")
        uipInput.send_keys("secret_sauce")
        entry = self.driver.find_element(By.ID, "login-button")
        entry.click()
        self.WaitForElementVisibility((By.XPATH, socialXPATH))
        socialMedia = self.driver.find_element(By.XPATH, socialXPATH)
        socialMedia.click()
        self.driver.switch_to.window(
            self.driver.window_handles[-1])
        self.driver.save_screenshot(
            f"{self.folderPath}/test-socialHub-{socialname}.png")
        assert self.driver.current_url == socialLink

    def test_priceLowToHigh(self):
        uiInput = self.driver.find_element(By.ID, "user-name")
        uiInput.send_keys("standard_user")
        uipInput = self.driver.find_element(By.ID, "password")
        uipInput.send_keys("secret_sauce")
        entry = self.driver.find_element(By.ID, "login-button")
        entry.click()
        self.WaitForElementVisibility(
            (By.ID, "add-to-cart-sauce-labs-backpack"))
        LtH = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
        LtH.click()
        self.driver.save_screenshot(
            f"{self.folderPath}/test-price-Low-To-High.png")

        fiyat = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_price")

        fiyatListe = [float(fiyat[i].text[1:]) for i in range(len(fiyat))]

        fiyatListe_copy_sort = fiyatListe.copy()
        fiyatListe_copy_sort.sort()
        assert fiyatListe == fiyatListe_copy_sort

    def WaitForElementVisibility(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))
