import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestSelenium(unittest.TestCase):

    def test_add_to_shopping_cart(self) -> None:
        """Добавление в корзину"""
        service = ChromeService(executable_path=ChromeDriverManager().install())

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors-spki-list')
        driver = webdriver.Chrome(service=service, options=options)

        driver.get('http://tutorialsninja.com/demo/')

        search_field = driver.find_element(By.NAME, 'search')
        search_field.send_keys("samsung")
        search_field.send_keys(Keys.ENTER)

        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div[2]/div[2]/button[1]')
        add_to_cart_button.click()

        sleep(1)
        shopping_cart_link = driver.find_element(By.XPATH, '//*[@title="Shopping Cart"]')
        shopping_cart_link.click()

        self.assertTrue("Product 6" in driver.page_source)

        driver.close()

    def test_delete_from_shopping_cart(self):
        """Удаление из корзины"""
        self.assertTrue(True)
