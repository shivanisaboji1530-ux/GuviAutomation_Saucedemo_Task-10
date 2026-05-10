import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.close()

def test_login_saucedemo(get_driver):
   # driver = webdriver.Chrome()
   # driver.get("https://www.saucedemo.com/")
    driver = get_driver
    time.sleep(2)



    # Enter username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")


    # Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")


    # Click login button
    driver.find_element(By.ID, "login-button").click()


def test_webpage(get_driver):
    driver = get_driver

    # Fetch title
    page_title = driver.title
    print("Title of Webpage :", page_title)

    # Fetch current URL
    current_url = driver.current_url
    print("Current URL :", current_url)

    # Fetch entire page text
    page_content = driver.find_element(By.TAG_NAME, "body").text


    # Save content into text file
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_content)

    print("Webpage content saved successfully.")




