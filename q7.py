import requests
from bs4 import BeautifulSoup
from googlesearch import search
from q777 import jason
import os
import re
from gensim.summarization.summarizer import summarize
def ser(query):
# Perform Google search and get list of URLs
 urls = list(search(query, tld="co.in", num=10, stop=10, pause=2))
# Create directory for text files
 if not os.path.exists('text_files'):
   os.mkdir('text_files')
# Scrape text from each URL and save as separate file
 for url in urls:
   response = requests.get(url)

 # Parse HTML content using BeautifulSoup
 soup = BeautifulSoup(response.content, 'html.parser')
 # Find all paragraphs in the HTML content
 paragraphs = soup.find_all('p')

 # Join paragraphs into a single string
 text = '\n'.join([p.get_text() for p in paragraphs])

 # Create file path based on URL
 filename = 'the'+url.split('/')[-1]
 filename =re.sub(r'[^a-zA-Z0-9\s]', '', filename) + '.txt'
 file_path = os.path.join('text_files', filename)
 print(file_path)

 # Write text to file
 with open(file_path, 'w',encoding="utf-8",errors="ignore") as f:f.write(text)
print('Text files saved in "text_files" directory.')
result = jason('text_files',query)