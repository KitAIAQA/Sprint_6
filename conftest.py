import pytest
from selenium import webdriver
from urls import URLs


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLs.scooter_address)
    yield driver
    driver.quit()