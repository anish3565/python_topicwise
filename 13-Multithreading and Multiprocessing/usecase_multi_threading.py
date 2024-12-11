"""
Scenario: Web Scraping:
- Web scraping involves making numerous network requests to fetch web pages.
- They're I/O-bound because they spend a lot of time waiting for responses from server.
- Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.
"""
'''
https://python.langchain.com/v0.1/docs/langsmith/
https://python.langchain.com/v0.1/docs/langsmith/walkthrough/
https://docs.smith.langchain.com/old/monitoring/concepts
'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
    "https://python.langchain.com/v0.1/docs/langsmith/",
    "https://python.langchain.com/v0.1/docs/langsmith/walkthrough/",
    "https://docs.smith.langchain.com/old/monitoring/concepts/"
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched.")