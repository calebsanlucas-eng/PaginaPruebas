import unittest
from selenium import webdriver

def test_busquedas(self):
    self.driver.find_element(By.ID, "linkPrincipal")
    self.driver.find_element(By.PARTIAL_LINK_TEXT, "Parcial")
    self.driver.find_element(By.CSS_SELECTOR, ".titulo")
    self.driver.find_element(By.TAG_NAME, "table")
    self.driver.find_element(By.XPATH, "//input[@id='busqueda']")


if __name__ == "__main__":
    unittest.main()
