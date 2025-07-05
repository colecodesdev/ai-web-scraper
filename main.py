# build StreamLit UI

import streamlit as st

# website title

st.title("AI Web Scraper")

# create text input box

url = st.text_input("Enter a website URL: ")

# create button

if st.button("Scrape Site"):
    st.write("Scraping the wesite")