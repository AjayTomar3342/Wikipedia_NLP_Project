from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

def links_scraping():
    #Original link to scrape
    res = requests.get("https://en.wikipedia.org/wiki/Wikipedia:Vital_people")
    #Get html content from the scraped link
    soup = bs(res.text, "html.parser")

    #Create an empty dataframe to fill links
    vital_scraped_links_df = pd.DataFrame(['Links'])

    #Get all urls inside the scraped link and store them in an dataframe
    for link in soup.find_all("a"):
        url = link.get("href", "")
        url=pd.Series(url)
        vital_scraped_links_df=vital_scraped_links_df.append(url,ignore_index=True)

    #Filter out unwanted links
    vital_scraped_links_df=vital_scraped_links_df[~vital_scraped_links_df[0].str.contains(':')]
    vital_scraped_links_df=vital_scraped_links_df[~vital_scraped_links_df[0].str.contains('#')]
    vital_scraped_links_df=vital_scraped_links_df[~vital_scraped_links_df[0].str.contains('//')]
    vital_scraped_links_df=vital_scraped_links_df[~vital_scraped_links_df[0].str.contains('Main_Page')]
    vital_scraped_links_df=vital_scraped_links_df[~vital_scraped_links_df[0].str.contains('en.wikipedia.org')]

    #Append initial link to convert relative links to absolute links
    vital_scraped_links_df[0] = 'https://en.wikipedia.org' + vital_scraped_links_df[0].astype(str)

    #Remove unwanted base links
    vital_scraped_links_df = vital_scraped_links_df.iloc[4: , :]
    vital_scraped_links_df = vital_scraped_links_df.iloc[:-1]

    #Rename column name of the dataframe
    vital_scraped_links_df=vital_scraped_links_df.set_axis(['Links'], axis=1)

    #Second Column Categories
    writers=['Writer']*60
    musicians_and_composers=['Musicians and composers']*36
    visual_artists=['Visual Artist']*41
    directors=['Director']*9
    entertainers=['Entertainers']*11
    philosophers_and_social_scientists=['Philosophers and Social Scientists']*56
    scientists_mathematicians_and_inventors=['Scientists, Mathematicians and Inventors']*92
    explorers=['Explorer']*19
    business_people=['Business People']*9
    political_leaders=['Political Leader']*108
    military_leaders_and_theorists=['Military Leaders and Theorists']*10
    rebels_revolutionaries_and_activitis=['Rebels,Revolutionaries and Activitis']*15
    religious_figures=['Religious Figure']*25
    sport_figures=['Sport Figure']*9

    #Append all categroies in one list
    category_list=writers+musicians_and_composers+visual_artists+directors+entertainers+philosophers_and_social_scientists+scientists_mathematicians_and_inventors+\
                explorers+business_people+political_leaders+military_leaders_and_theorists+rebels_revolutionaries_and_activitis+religious_figures+sport_figures

    #Add second column(Category) to dataframe
    vital_scraped_links_df['Category']=category_list

    #Store dataframe as an excel file
    vital_scraped_links_df.to_excel(r'C:\Users\Ajay\PycharmProjects\Wikipedia_NLP_Project\Data\vital_people_links.xlsx',index=False, header=True)

    #Read in serial killers url file
    serial_killer_df = pd.read_excel('Data\serial_killer_people_links.xlsx')

    #Append initial link to convert relative links to absolute links
    serial_killer_df['Links'] = 'https://en.wikipedia.org' + serial_killer_df['Links'].astype(str)

    #Store dataframe as an excel file
    serial_killer_df.to_excel(r'C:\Users\Ajay\PycharmProjects\Wikipedia_NLP_Project\Data\serial_killer_people_links.xlsx',index=False, header=True)

