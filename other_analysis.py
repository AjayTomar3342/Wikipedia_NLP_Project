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

def other_visualizations():
    #Read in vital people url file
    vital_people_df = pd.read_excel('Data\\vital_people_links.xlsx')

    #List to store word count of all the vital people articles
    vital_people_word_counts=[]

    #String to store all wikipedia text
    full_vital_text=""

    # Set of stop words
    stop_words = set(stopwords.words('english'))

    #Iterate through all vital people links
    for i in vital_people_df['Links']:

        #Original link to scrape
        res = requests.get(i)

        #Get html content from the scraped link
        soup = bs(res.text, "html.parser")

        #Get only article text from the url link
        text=''
        for paragraph in soup.find_all('p'):
            text += paragraph.text
            full_vital_text+=paragraph.text

        vital_people_word_counts.append(str(len(text.split())))

    #Replace all stop words with blank in full_vital_text
    big_regex = re.compile(' '.join(map(re.escape, stop_words)))
    full_vital_text = big_regex.sub(" ", full_vital_text)

    #Create dictionary and count frequency of individual words
    vital_text_dictionary=dict(Counter(full_vital_text.replace(',', '').replace('.', '').split()))

    #Convert list to pandas dataframe
    vital_people_word_counts_df=pd.DataFrame(vital_people_word_counts, columns=['Counts'])

    #Store dataframe as an excel file
    vital_people_word_counts_df.to_excel(r'C:\Users\Ajay\PycharmProjects\Wikipedia_NLP_Project\Data\vital_people_word_counts.xlsx',index=False, header=True)

    #Read in serial killers url file
    serial_people_df = pd.read_excel('Data\\serial_killer_people_links.xlsx')

    #List to store word count of all the serial killer articles
    serial_killer_word_counts=[]

    #String to store all wikipedia text
    full_serial_killer_text=""

    #Iterate through all serial killer links
    for i in serial_people_df['Links']:

        #Original link to scrape
        res = requests.get(i)

        #Get html content from the scraped link
        soup = bs(res.text, "html.parser")

        #Get only article text from the url link
        text=''
        for paragraph in soup.find_all('p'):
            text += paragraph.text
            full_serial_killer_text += paragraph.text

        serial_killer_word_counts.append(str(len(text.split())))

    #Replace all stop words with blank in full_vital_text
    big_regex = re.compile(' '.join(map(re.escape, stop_words)))
    full_serial_killer_text = big_regex.sub(" ", full_serial_killer_text)

    #Create dictionary and count frequency of individual words
    serial_killer_text_dictionary=dict(Counter(full_serial_killer_text.replace(',', '').replace('.', '').split()))

    #Convert list to pandas dataframe
    serial_killer_word_counts_df=pd.DataFrame(serial_killer_word_counts, columns=['Counts'])

    #Store dataframe as an excel file
    serial_killer_word_counts_df.to_excel(r'C:\Users\Ajay\PycharmProjects\Wikipedia_NLP_Project\Data\serial_people_word_counts.xlsx',index=False, header=True)

    #Creating box plot
    vital_people_word_counts = pd.read_excel('Data\\vital_people_word_counts.xlsx')
    serial_killer_word_counts = pd.read_excel('Data\\serial_people_word_counts.xlsx')

    data=[vital_people_word_counts['Counts'],serial_killer_word_counts['Counts']]

    labels = ['Vital People Word Count', 'Serial Killer Word Count',]

    fig = plt.figure(figsize =(10, 7))

    # Creating plot
    bp = plt.boxplot(data,meanline=True, showmeans=True, showcaps=True, showbox=True, showfliers=True, vert=True, patch_artist=True, labels=labels)

    colors = ['green', 'red']

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # show plot
    plt.show()

    #Plotting vital people word cloud
    text_word_cloud = " ".join([(k + " ") for k,v in vital_text_dictionary.items()])

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text_word_cloud)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    print(serial_killer_text_dictionary)
    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text_word_cloud)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    #Store vital people word count dictionary as excel file
    vital_people_frequency_df = pd.DataFrame(data=vital_text_dictionary, index=[0])
    vital_people_frequency_df.to_excel('vital_people_frequency_df.xlsx')

    #Store serial killers word count dictionary as excel file
    serial_killer_frequency_df = pd.DataFrame(data=serial_killer_text_dictionary, index=[0])
    serial_killer_frequency_df.to_excel('serial_killer_frequency_df.xlsx')

    #Plotting vital people word cloud
    text_word_cloud = " ".join([(k + " ") for k,v in serial_killer_text_dictionary.items()])

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text_word_cloud)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text_word_cloud)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()