# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:23:39 2020

@author: reena
"""

#!pip install pyttsx3  #pyttsx3 use for the speaking part
#!pip install PyPDF2

import pyttsx3
import PyPDF2

book = open('D:\interview-question-data-science--master\Data.pdf','rb')
bookReader = PyPDF2.PdfFileReader(book)
print(bookReader.getNumPages())
#pagenumber=bookReader.getNumPages()
page=''
for pages in range(bookReader.getNumPages()):
    page = bookReader.getPage(pages) #bookReader.getPage(14) 
    text = page.extractText()
    print(text)
    output = pyttsx3.init()
    output.say(text)
    output.runAndWait()
