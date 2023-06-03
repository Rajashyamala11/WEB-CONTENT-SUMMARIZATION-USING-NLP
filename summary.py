import openpyxl
from ctypes import alignment
import tkinter as tk
from tkinter import ANCHOR, CENTER, Canvas, ttk
import requests
from bs4 import BeautifulSoup
from q7 import ser
import re
import warnings
from rsa import verify
import summarizer
from preprocessing import prepro
import csv
from selenium import webdriver
import pandas as pd
import nltk
from urllib.request import urlopen
from googlesearch import search
warnings.filterwarnings(action='ignore', category=UserWarning,
module='gensim')
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import xlwt
from xlwt import Workbook
from docx import Document
from docx.shared import Inches,Pt
from pptx import Presentation
root = tk.Tk()
root.geometry("400x200")
root.minsize(300, 100)
root.configure(bg="#4da4ea")
root.title('Report Generator')
#photo = PhotoImage(file = "Any image file")
root.iconbitmap("./PIRG.ico")
canvas = Canvas(root, bg = "#4da4ea", height = 300, width = 100)
canvas.place(relx = 0.2, rely = 0.3)
companyName = tk.StringVar()
def submit():
 # def tagVisible(element):
 # if element.parent.name in ['style', 'script', 'head','title', 'meta', '[document]']:
 # return False
 # if isinstance(element, Comment):
 # return False
 # return True
 def textFromHtml(body):
   soup = BeautifulSoup(body, 'html.parser')
 # paragraphs = soup.find_all('p')
 # # print(paragraphs)
 # text = '\n'.join([p.get_text() for p in paragraphs])
 # print(text)
 sentences = []
 for p_tag in soup.find_all('p'):
   sentences += p_tag.get_text().split('.')
 # print(sentences)
 return sentences

 name = companyName.get()
 wb = openpyxl.Workbook()
 sheet = wb.active
 row_num = 1
 list_url = search(name, tld="co.in", num=10, stop=10, pause=2)
 res = []
 for link in list_url:
   res.append(link)
 print(link)
 sheet.cell(row=row_num, column=1, value=link)
 row_num += 1


 query = name
 # def cosine(query):
 # sentencefilename = query+'_sentence.csv'
 # skg=name+'_sentence.csv'
 # with open(sentencefilename, 'w', newline='', encoding='utf8') as csvfile:
 # writer = csv.writer(csvfile)
 # for i in res:
 # print(i)
 # page = requests.get(i)
 # # print(page)
 # html = page.content
 # sentences = textFromHtml(html)
 # for sentence in sentences:
 # writer.writerow([sentence])
 # print("done")
 # prepro(skg)
 # return skg
 filename = name
 wb.save(filename + '.csv')
 results = ser(query)
 # cosine(query)

companyName.set("")
nameLabel = tk.Label(canvas, text = 'Name', font=('calibre',10,'bold'))
nameValue = tk.Entry(canvas, textvariable =
companyName,font=('calibre',10,'normal'))
submitBtn = tk.Button(canvas, text = 'Submit', command = submit, bg =
"#73c2fb")
nameLabel.grid(row = 0, column = 0)
nameValue.grid(row = 0, column = 2)
submitBtn.grid(row = 2, column = 2)
root.mainloop()
