import os
import re
import json
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning,
module='gensim')
from gensim.summarization.summarizer import summarize
from collections import defaultdict
from twosum import sumari
# Function to preprocess text
def preprocess(text):
 # Convert to lowercase
 text = text.lower()
 # Remove non-alphanumeric characters
 text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
 # Split into words
 words = text.split()
 return words
# Function to build inverted index
def build_index(docs_dir):
 index = defaultdict(dict)
 # print(index)
 for filename in os.listdir(docs_dir):
  print(filename)
 if filename.endswith('.txt'):
  with open(os.path.join(docs_dir, filename),'r',encoding="utf-8",errors="ignore") as f:
   text = f.read()
 words = preprocess(text)
 for word in words:
  if filename not in index[word]:
   index[word][filename] = 0
 index[word][filename] += 1
 # print(index)
 return index

def query_index(index, query):
 keywords = preprocess(query)
 results = []
 for keyword in keywords:
  if keyword in index:
   results.extend(index[keyword])
 return list(set(results))
# Example usage
def jason(file_path,query):
 docs_dir = 'text_files'
 index = build_index(docs_dir)
 with open('index.json', 'w') as f:
  json.dump(index, f, indent=4)
 with open('index.json', 'r') as f:
  index = json.load(f)
 results = query_index(index, query)
 print(f"Results for query '{query}': {results}")
 print(len(results)," is the count of files for the query")
 summary =gap(results,docs_dir)
 return results
def gap(results,docs_dir):
 # define directory containing files


 for file in results:
  with open(os.path.join(docs_dir, file), 'r',encoding="utf8",errors="ignore") as f:
   contents = f.read()
 # print(f"Contents of {file}:")
 # print(contents)
 print("done contents")
 ds=sumari(contents)
 with open('summary.docx', 'w',encoding="utf8",errors="ignore") as f:
  f.write(str(ds))
 print("done")

 # summarize contents of all files
 # print(words)
 # summary = summarize(words)
 # print(summary)
 # return summary