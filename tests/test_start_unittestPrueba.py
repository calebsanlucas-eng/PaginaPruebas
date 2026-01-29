import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPagina(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://calebsanlucas-eng.github.io/PaginaPruebas/")

    def test_titulo_pagina(self):
        wait = WebDriverWait(self.driver, 10)
        titulo = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "titulo"))
        ).text

        self.assertEqual(titulo, "Página de Pruebas")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
