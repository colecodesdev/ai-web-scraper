# build selenium scraper

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

# grab content from site

def scrape_website(website):
    print("Launching chrome browser...")

    # specify chrome driver

    chrome_driver_path = "./chromedriver.exe"

    # specify how driver should operate (headless, ignore images, etc.)

    options = webdriver.ChromeOptions()

    # setup driver, specify service, pass options

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    # use webdriver to go to website
    
    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()