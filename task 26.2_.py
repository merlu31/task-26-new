import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    paths = r"C:\Users\Merlin Archana\chromedriver-win64\chromedriver-win64"
    os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

