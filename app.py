import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
st.set_page_config(
    page_title="Web Page Link Scraper",
    page_icon="📰",
    layout="wide",
)



class Scraper:
    """
    A class to scrape a website for specific links based on their text.
    """
    def __init__(self, site):
        self.site = site

    def scrape(self, keyword):
        """
        Fetches a website's HTML and finds links where the visible text
        contains the specified keyword.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            r = requests.get(self.site, headers=headers, timeout=10)
            r.raise_for_status()
            html = r.content
        except requests.exceptions.RequestException as e:
            return f"Error: Could not retrieve the URL. Details: {e}"
            
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        
        found_links = {} # Using a dictionary to avoid duplicate URLs
        for tag in sp.find_all("a"):
            url = tag.get("href")
            link_text = tag.get_text() # Get the visible text of the link
            
            # Ensure both the URL and the link text exist
            if url and link_text:
                # *** KEY CHANGE IS HERE ***
                # Check if the keyword is in the link's text (case-insensitive)
                if keyword.lower() in link_text.lower():
                    full_url = urljoin(self.site, url)
                    # Add the text and URL to the dictionary to prevent duplicates
                    found_links[full_url] = link_text.strip()
                    
        return found_links

# --- Streamlit App Interface ---





st.title("📰 Web Page Link Scraper")
st.write("Enter a URL and a keyword. The app will find all links on the page where the **visible text** contains your keyword.")

# Reordered the input fields as per the logic
keyword = st.text_input("1. Enter a keyword to find in the link text", "news")
news_site = st.text_input("2. Enter the URL to scrape", "https://www.bbc.com")


if st.button("Scrape for Links"):
    if news_site and keyword:
        with st.spinner(f"Searching for links with text '{keyword}' on {news_site}..."):
            scraper_instance = Scraper(news_site)
            results = scraper_instance.scrape(keyword)

        st.success("Scraping complete!")

        if isinstance(results, dict):
            if results:
                st.subheader(f"Found {len(results)} matching links:")
                with st.expander("View Links", expanded=True):
                    # Display the link text and the URL
                    for url, text in results.items():
                        st.markdown(f"**Text:** `{text}`\n\n**URL:** [{url}]({url})")
                        st.divider() # Adds a small line between results
            else:
                st.warning(f"No links containing the text '{keyword}' were found.")
        else:
            st.error(results)
    else:
        st.warning("Please enter both a URL and a keyword.")