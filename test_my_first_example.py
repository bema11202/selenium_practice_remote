import selenium as se
import pytest
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
    return login


def test_add_to_cart(goto_page, login):
    """This test will add an item to the cart"""
    # goto_page.find_element(By.XPATH, "//a[@href='/cart']").click()
    assert goto_page.current_url == "https://www.saucedemo.com/inventory.html"
    # goto_page.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    goto_page.find_element(By.CLASS_NAME, "btn_primary").click() # btn btn_primary btn_small btn_inventory
    # assert goto_page.find_element(By.NAME, "remove-sauce-labs-backpack").is_displayed()
    wait = WebDriverWait(goto_page, 10)
    wait.until(lambda x: x.find_element(By.NAME, "remove-sauce-labs-backpack").is_displayed())
    for i in goto_page.find_elements(By.CLASS_NAME, "inventory_item_name"):
        print(i.text)
    print(goto_page.current_url)
    goto_page.close()
