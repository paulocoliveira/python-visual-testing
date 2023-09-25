from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config/config.ini')

@pytest.fixture()
def driver(request):
    username = os.getenv("LT_USERNAME")
    accessKey = os.getenv("LT_ACCESS_KEY")

    gridUrl = config.get('CLOUDGRID', 'grid_url')

    web_driver = webdriver.ChromeOptions()
    platform = config.get('ENV', 'platform')
    browser_name = config.get('ENV', 'browser_name')

    box1 = {
        "left": 100,
        "top": 500,
        "right": 800,
        "bottom": 300
    }

    box2 = {
        "left": 800,
        "top": 50,
        "right": 20,
        "bottom": 700
    }

    lt_options = {
        "user": config.get('LOGIN', 'username'),
        "accessKey": config.get('LOGIN', 'access_key'),
        "build": config.get('CLOUDGRID', 'build_name'),
        "name": config.get('CLOUDGRID', 'test_name'),
        "platformName": platform,
        "w3c": config.get('CLOUDGRID', 'w3c'),
        "browserName": browser_name,
        "browserVersion": config.get('CLOUDGRID', 'browser_version'),
        "selenium_version": config.get('CLOUDGRID', 'selenium_version'),
        "smartUI.project": "official_testing", 
        "smartUI.build": "build_4", 
        "smartUI.baseline": False,
        "boundingBoxes" : [box1, box2] # Your bounding box configuration
    }

    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = f"https://{username}:{accessKey}@{gridUrl}"
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    driver.quit

def test_visual_using_lambdatest(driver):
    driver.get(config.get('WEBSITE', 'url'))
    
    driver.execute_script("smartui.takeScreenshot=screenshots/screenshot_initial.jpg")

    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys("This is a visual testing text!")

    # # Find an element by its ID and click on it
    element = driver.find_element(By.ID, "showInput")
    element.click()

    # # Find an element by its ID and extract its text
    element = driver.find_element(By.ID, "message")

    driver.execute_script("smartui.takeScreenshot=screenshots/screenshot_final.jpg")

    assert element.text == "This is a visual testing text!"

    result = driver.execute_script("smartui.fetchScreenshotStatus")
    print(result)