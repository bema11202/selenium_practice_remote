import os
import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture(name="goto_page", scope="session")
def goto_page():
    """This fixture will open the browser and go to the page"""
    driver = webdriver.ChromiumEdge()
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    return driver

@pytest.fixture(name="login", scope="session", autouse=True)
def login(goto_page):
    """This fixture will login to the page"""
    goto_page.find_element(By.ID, "user-name").send_keys("standard_user")
    goto_page.find_element(By.ID, "password").send_keys("secret_sauce")
    goto_page.find_element(By.ID, "login-button").click()
    assert "Swag Labs" in goto_page.title
    time.sleep(1)
    return login



def test_add_to_cart(goto_page, login):
    """This test will add an item to the cart"""
    # goto_page.find_element(By.XPATH, "//a[@href='/cart']").click()
    assert goto_page.current_url == "https://www.saucedemo.com/inventory.html"
    # goto_page.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    goto_page.find_element(By.CLASS_NAME, "btn_primary").click() # btn btn_primary btn_small btn_inventory
    assert goto_page.find_element(By.NAME, "remove-sauce-labs-backpack").is_displayed()
    print(goto_page.current_url)
    print("The session id is:" + goto_page.session_id)
    print(os.path.abspath(__file__))
    print(os.getcwd())

def test_remove_from_cart(goto_page):
    """This test will remove an item from the cart"""
    goto_page.find_element(By.CLASS_NAME, "btn_primary").click()  # btn btn_primary btn_small btn_inventory
    goto_page.find_element(By.NAME, "remove-sauce-labs-backpack").click()
    assert goto_page.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").is_displayed()
    print("The other session id is:" + goto_page.session_id)


def test_checkout(goto_page, login):
    """This test will checkout the cart"""
    goto_page.find_element(By.ID, "shopping_cart_container").click()  # btn btn_primary btn_small btn_inventory
    time.sleep(3)
    assert goto_page.find_element(By.NAME, "checkout").is_displayed()
    assert goto_page.find_element(By.NAME, "checkout").text == "Checkout"
    print("The other session id is:" + goto_page.session_id)
    goto_page.find_element(By.NAME, "continue-shopping").click()
    assert goto_page.current_url == "https://www.saucedemo.com/inventory.html"

def test_add_multiple_to_cart(goto_page, login):
    """This test will add multiple items to the cart"""
    goto_page.find_element(By.ID, "shopping_cart_container").click()  # btn btn_primary btn_small btn_inventory
    time.sleep(3)
    assert goto_page.find_element(By.NAME, "checkout").is_displayed()
    assert goto_page.find_element(By.NAME, "checkout").text == "Checkout"
    print("The other session id is:" + goto_page.session_id)
    goto_page.find_element(By.NAME, "continue-shopping").click()
    assert goto_page.current_url == "https://www.saucedemo.com/inventory.html"
    goto_page.close()
