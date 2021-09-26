from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
set(stopwords.words('english'))
nltk.download('punkt')
from nltk.sentiment import SentimentIntensityAnalyzer

def words_sentiment():
    #Read in vital people url file
    vital_people_df = pd.read_excel('Data\\vital_people_links.xlsx')

    #Lists to append different sentiment percentages
    vital_negative_percentages=[]
    vital_neutral_percentages=[]
    vital_positive_percentages=[]

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

        #Set of stop words
        stop_words=set(stopwords.words('english'))

        #tokens of words of our text
        word_tokens = nltk.word_tokenize(text)

        #Take only words which aren't stop words
        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)

        # print("\n\nOriginal Sentence \n\n")
        # print(" ".join(word_tokens))
        #
        # print("\n\nFiltered Sentence \n\n")
        # print(" ".join(filtered_sentence))
        #
        # print("Filtered", filtered_sentence)

        sia = SentimentIntensityAnalyzer()

        #Variables to track count of different sentiments
        neg = 0
        neu = 0
        pos = 0
        total=0

        #Get sentiment scores of each word in text and increase count for different sentiment words
        for i in filtered_sentence:
           for key, value in sia.polarity_scores(i).items():
               if key=='neg' and value==1:
                   neg=neg+1
               elif key== 'neu' and value==1:
                   neu=neu+1
               elif key== 'pos' and value ==1:
                   pos=pos+1
               else:
                   continue
        total=neg+neu+pos

        vital_negative_percentages.append((neg/total)*100)
        vital_neutral_percentages.append((neu/total)*100)
        vital_positive_percentages.append((pos/total)*100)

    print(vital_neutral_percentages)
    print(vital_negative_percentages)
    print(vital_positive_percentages)

    vital_people_df['Positive_Words_%']=vital_positive_percentages
    vital_people_df['Neutral_Words_%']=vital_neutral_percentages
    vital_people_df['Negative_Words_%']=vital_negative_percentages

    #Store dataframe as an excel file
    vital_people_df.to_excel(r'C:\Users\Ajay\PycharmProjects\Wikipedia_NLP_Project\Data\vital_people_with_sentiments.xlsx',index=False, header=True)


    #Read in serial killers url file
    serial_people_df = pd.read_excel('Data\\serial_killer_people_links.xlsx')

    #Lists to append different sentiment percentages
    serial_negative_percentages=[]
    serial_neutral_percentages=[]
    serial_positive_percentages=[]

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

        #Set of stop words
        stop_words=set(stopwords.words('english'))

        #tokens of words of our text
        word_tokens = nltk.word_tokenize(text)

        #Take only words which aren't stop words
        filtered_sentence = []

        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)

        # print("\n\nOriginal Sentence \n\n")
        # print(" ".join(word_tokens))
        #
        # print("\n\nFiltered Sentence \n\n")
        # print(" ".join(filtered_sentence))
        #
        # print("Filtered", filtered_sentence)

        sia = SentimentIntensityAnalyzer()

        #Variables to track count of different sentiments
        neg = 0
        neu = 0
        pos = 0
        total=0

        #Get sentiment scores of each word in text and increase count for different sentiment words
        for i in filtered_sentence:
           for key, value in sia.polarity_scores(i).items():
               if key=='neg' and value==1:
                   neg=neg+1
               elif key== 'neu' and value==1:
                   neu=neu+1
               elif key== 'pos' and value ==1:
                   pos=pos+1
               else:
                   continue
        total=neg+neu+pos

        serial_negative_percentages.append((neg/total)*100)
        serial_neutral_percentages.append((neu/total)*100)
        serial_positive_percentages.append((pos/total)*100)


    serial_people_df['Positive_Words_%']=serial_positive_percentages
    serial_people_df['Neutral_Words_%']=serial_neutral_percentages
    serial_people_df['Negative_Words_%']=serial_negative_percentages

    #Store dataframe as an excel file
    serial_people_df.to_excel(r'C:\Users\Ajay\PycharmProjects\Wikipedia_NLP_Project\Data\serial_killer_people_with_sentiments.xlsx',index=False, header=True)