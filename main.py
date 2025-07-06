import streamlit as st
from scrape import scrape_website

# website title

st.title("AI Web Scraper")

# create text input box

url = st.text_input("Enter a website URL: ")

# create button

if st.button("Scrape Website"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    print(result)