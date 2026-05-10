import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.close()


def test_positive_login(get_driver):
    """
    Positive Test Case
    Verify successful login with valid credentials.
    """

    driver = get_driver

    driver.get("https://www.saucedemo.com/")

    # Verify homepage URL
    assert driver.current_url == "https://www.saucedemo.com/"

    # Verify title
    assert "Swag Labs" in driver.title

    # Enter valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login
    driver.find_element(By.ID, "login-button").click()

    time.sleep(5)

    # Take screenshot for positive test case
    driver.save_screenshot("reports/positive_login.png")

    # Verify dashboard URL
    assert "inventory.html" in driver.current_url


def test_negative_login(get_driver):
    """
    Negative Test Case
    Verify login failure with invalid credentials.
    """

    driver = get_driver



    # Enter invalid credentials
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")

    # Click login
    driver.find_element(By.ID, "login-button").click()

    time.sleep(5)

    # Fetch error message
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    # Take screenshot for negative test case
    driver.save_screenshot("reports/negative_login.png")

    # Verify error message
    assert "Username and password do not match" in error_message