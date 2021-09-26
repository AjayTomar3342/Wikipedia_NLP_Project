import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
set(stopwords.words('english'))
import matplotlib.pyplot as plt
import re
from collections import Counter
import os
from os import path
from wordcloud import WordCloud

link='https://en.wikipedia.org/wiki/Homer'

vital_people_word_counts=[]

#String to store all wikipedia text
full_vital_text=""

# Set of stop words
stop_words = set(stopwords.words('english'))


#Original link to scrape
res = requests.get(link)

#Get html content from the scraped link
soup = bs(res.text, "html.parser")

#Get only article text from the url link
text=''
for paragraph in soup.find_all('p'):
    text += paragraph.text
    full_vital_text+=paragraph.text

vital_people_word_counts.append(str(len(text.split())))

print("Before",full_vital_text)

#Replace all stop words with blank in full_vital_text
big_regex = re.compile(' '.join(map(re.escape, stop_words)))
full_vital_text = big_regex.sub("", full_vital_text)
print("Full",full_vital_text)

#Create dictionary and count frequency of individual words
vital_text_dictionary=dict(Counter(full_vital_text.replace(',', '').replace('.', '').split()))


for key, value in sorted(vital_text_dictionary.items()):
    print("{} : {}".format(key, value))
#Convert list to pandas dataframe
vital_people_word_counts_df=pd.DataFrame(vital_people_word_counts, columns=['Counts'])


#Plotting vital people word cloud
text_word_cloud = " ".join([(k + " ") for k,v in vital_text_dictionary.items()])
# def convert(string):
#     li = list(string.split(" "))
#     return li
# text_word_cloud=convert(text_word_cloud)
#
# text_word_cloud=set(text_word_cloud)

print("Help",text_word_cloud)
# Generate a word cloud image
wordcloud = WordCloud().generate(text_word_cloud)

plt.imshow(wordcloud, interpolation='none')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text_word_cloud)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

