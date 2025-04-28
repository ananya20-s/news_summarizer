import requests
import json
import os
from newspaper import Article

from bert_summarizer import get_summary

def get_news_url(keyword):
    """
    This function takes a keyword as input and returns a news URL for that keyword.
    """
    NEWSDATA_API_KEY = "pub_82446613a83709c31e10383087f050a3e85c5"

    '''if 'NEWSDATA_API_KEY' not in os.environ:
        raise ValueError("API key not found. Please set the NEWSDATA_API_KEY environment variable.")'''

    #base_url = f"https://newsdata.io/api/1/latest?qInTitle={keyword}apikey={os.environ.get("NEWSDATA_API_KEY")}"
    base_url = f"https://newsdata.io/api/1/latest?qInTitle={keyword}&language=en&category=business,technology&apikey={NEWSDATA_API_KEY}"

    response = requests.get(base_url)

    if response.status_code != 200:
        #raise ValueError(f"Error fetching news data: {response.status_code}")
        print(f"Error fetching news data: {response.status_code}")
        return None, "Error fetching news data", None
    
    data = response.json()
    text = json.dumps(data, indent=4) 
    #print(text)
    if 'results' not in data:
        #raise ValueError("No results found in the response.")
        print(f"No results found in the response.")
        return None, "No articles found for the company", None
    
    articles = data['results']

    if not articles:    
        #raise ValueError("No articles found for the given keyword.")
        return None, "No articles found for the given keyword.", None
    
    url = articles[0]['link']
    print(url)
    title = articles[0]['title']
    print("Fetching content")
    content = get_content(url)
    
    summary = get_summary(content)
    print("Summarizing content")
    print(summary)


    return url,title,summary

def get_content(url):
    """
    This function takes a URL as input and returns the content of the page.
    """
    article = Article(url)
    article.download()
    article.parse()
    print("Parsing content")
    text = article.text
    print(text)
    
    return text