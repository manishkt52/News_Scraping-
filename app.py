import streamlit as st  
import requests
from bs4 import BeautifulSoup
from llm import output

# Function to fetch news data
def get_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Fetching headlines
        headlines1 = soup.find_all('h2')  # Modify this based on the website's structure
        headlines2 = soup.find_all('p')  # Modify this based on the website's structure

        news_list = []
        for headline in headlines1:
            news_list.append(headline.text.strip())
        for headline in headlines2:
            news_list.append(headline.text.strip())

        return news_list
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the URL: {e}")
        return []

# Streamlit UI setup
st.title("News Scraping with Generative AI")

# Sidebar with suggested links
st.sidebar.title("Suggested Links")
suggested_links = [
    "https://www.indiatoday.in",
    "https://www.bbc.com/news",
    "https://news.yahoo.com/",
    "https://www.firstpost.com/",
    "https://www.nytimes.com"
]

selected_link = st.sidebar.radio("Click a link to copy it to the input box:", suggested_links)

if st.sidebar.button("Use Selected Link"):
    st.session_state['url'] = selected_link

# Explanation of how news scraping works
st.sidebar.title("How News Scraping Works")
st.sidebar.write(
    """
    - **Get the webpage content**: The app visits a webpage and collects its information.
    - **Understand the webpage**: The app uses a tool (called BeautifulSoup) to figure out the important parts of the webpage, like titles or headlines.
    - **Pick out the headlines**: It pulls out the main text, such as news headlines, from the webpage.
    - **Summarize the information**: A smart AI tool creates a short summary of the headlines to make it easier to read quickly.
    """
)

# Input URL from the user
url = st.text_input("Enter the URL of the news website", st.session_state.get('url', "https://www.indiatoday.in"))

if st.button("Fetch News"):
    with st.spinner("Fetching news data..."):
        news_data = get_news(url)

    if news_data:
        st.success("News fetched successfully!")

        # Summarizing headlines
        prompt = f"""Summarise the given input text:\ninput text: {news_data}"""
        with st.spinner("Summarizing the news..."):
            answer = output(prompt)

        st.subheader("Summarized News")
        st.write(answer)

           
