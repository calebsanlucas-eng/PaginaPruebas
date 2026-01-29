import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestBusquedaAvanzada(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://calebsanlucas-eng.github.io/PaginaPruebas/")

    def test_busquedas(self):
        self.driver.find_element(By.LINK_TEXT, "Link Principal")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Parcial")
        self.driver.find_element(By.CSS_SELECTOR, ".titulo")
        self.driver.find_element(By.TAG_NAME, "table")
        self.driver.find_element(By.XPATH, "//input[@id='busqueda']")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
