# build selenium scraper

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
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

# extract html body

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# clean html body

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # look inside parser content for script or style and remove them

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # get all text and separate with new line    

    cleaned_content = soup.get_text(separator="\n")

    # remove empty text strings

    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

# split between max token limit batches for llm

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]