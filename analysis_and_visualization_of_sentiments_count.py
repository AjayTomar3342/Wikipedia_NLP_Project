import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp

def visualization_sentiments():
    #Read in vital people file
    vital_people_df=pd.read_excel('Data\\vital_people_with_sentiments.xlsx')

    #Filter out only writers from all vital people
    vital_people_writers_df=vital_people_df[vital_people_df['Category']=='Writer']

    #Get individual sentiments average
    writers_positive=vital_people_writers_df['Positive_Words_%'].mean()
    writers_negative=vital_people_writers_df['Negative_Words_%'].mean()
    writers_neutral=vital_people_writers_df['Neutral_Words_%'].mean()

    #Filter out only musicians and composers from all vital people
    vital_people_musicians_and_composers_df=vital_people_df[vital_people_df['Category']=='Musicians and composers']

    #Get individual sentiments average
    musicians_and_composers_positive=vital_people_musicians_and_composers_df['Positive_Words_%'].mean()
    musicians_and_composers_negative=vital_people_musicians_and_composers_df['Negative_Words_%'].mean()
    musicians_and_composers_neutral=vital_people_musicians_and_composers_df['Neutral_Words_%'].mean()

    #Filter out only visual artist from all vital people
    vital_people_visual_artist_df=vital_people_df[vital_people_df['Category']=='Visual Artist']

    #Get individual sentiments average
    visual_artist_positive=vital_people_visual_artist_df['Positive_Words_%'].mean()
    visual_artist_negative=vital_people_visual_artist_df['Negative_Words_%'].mean()
    visual_artist_neutral=vital_people_visual_artist_df['Neutral_Words_%'].mean()

    #Filter out only director from all vital people
    vital_people_directors_df=vital_people_df[vital_people_df['Category']=='Director']

    #Get individual sentiments average
    directors_positive=vital_people_directors_df['Positive_Words_%'].mean()
    directors_negative=vital_people_directors_df['Negative_Words_%'].mean()
    directors_neutral=vital_people_directors_df['Neutral_Words_%'].mean()

    #Filter out only entertainers from all vital people
    vital_people_entertainers_df=vital_people_df[vital_people_df['Category']=='Entertainers']

    #Get individual sentiments average
    entertainers_positive=vital_people_entertainers_df['Positive_Words_%'].mean()
    entertainers_negative=vital_people_entertainers_df['Negative_Words_%'].mean()
    entertainers_neutral=vital_people_entertainers_df['Neutral_Words_%'].mean()

    #Filter out only philosophers from all vital people
    vital_people_philosophers_df=vital_people_df[vital_people_df['Category']=='Philosophers and Social Scientists']

    #Get individual sentiments average
    philosophers_positive=vital_people_philosophers_df['Positive_Words_%'].mean()
    philosophers_negative=vital_people_philosophers_df['Negative_Words_%'].mean()
    philosophers_neutral=vital_people_philosophers_df['Neutral_Words_%'].mean()

    #Filter out only scientists and mathematicians from all vital people
    vital_people_scientists_and_mathematicians_df=vital_people_df[vital_people_df['Category']=='Scientists, Mathematicians and Inventors']

    #Get individual sentiments average
    scientists_and_mathematicians_positive=vital_people_scientists_and_mathematicians_df['Positive_Words_%'].mean()
    scientists_and_mathematicians_negative=vital_people_scientists_and_mathematicians_df['Negative_Words_%'].mean()
    scientists_and_mathematicians_neutral=vital_people_scientists_and_mathematicians_df['Neutral_Words_%'].mean()

    #Filter out only explorers from all vital people
    vital_people_explorers_df=vital_people_df[vital_people_df['Category']=='Explorer']

    #Get individual sentiments average
    explorers_positive=vital_people_explorers_df['Positive_Words_%'].mean()
    explorers_negative=vital_people_explorers_df['Negative_Words_%'].mean()
    explorers_neutral=vital_people_explorers_df['Neutral_Words_%'].mean()

    #Filter out only business people from all vital people
    vital_people_business_people_df=vital_people_df[vital_people_df['Category']=='Business People']

    #Get individual sentiments average
    business_people_positive=vital_people_business_people_df['Positive_Words_%'].mean()
    business_people_negative=vital_people_business_people_df['Negative_Words_%'].mean()
    business_people_neutral=vital_people_business_people_df['Neutral_Words_%'].mean()

    #Filter out only politicians from all vital people
    vital_people_politicians_df=vital_people_df[vital_people_df['Category']=='Political Leader']

    #Get individual sentiments average
    politicians_positive=vital_people_politicians_df['Positive_Words_%'].mean()
    politicians_negative=vital_people_politicians_df['Negative_Words_%'].mean()
    politicians_neutral=vital_people_politicians_df['Neutral_Words_%'].mean()

    #Filter out only military leaders from all vital people
    vital_people_military_leaders_df=vital_people_df[vital_people_df['Category']=='Military Leaders and Theorists']

    #Get individual sentiments average
    military_leaders_positive=vital_people_military_leaders_df['Positive_Words_%'].mean()
    military_leaders_negative=vital_people_military_leaders_df['Negative_Words_%'].mean()
    military_leaders_neutral=vital_people_military_leaders_df['Neutral_Words_%'].mean()

    #Filter out only revolutionaries and activists from all vital people
    vital_people_revolutionaries_and_activists_df=vital_people_df[vital_people_df['Category']=='Rebels,Revolutionaries and Activitis']

    #Get individual sentiments average
    revolutionaries_and_activists_positive=vital_people_revolutionaries_and_activists_df['Positive_Words_%'].mean()
    revolutionaries_and_activists_negative=vital_people_revolutionaries_and_activists_df['Negative_Words_%'].mean()
    revolutionaries_and_activists_neutral=vital_people_revolutionaries_and_activists_df['Neutral_Words_%'].mean()

    #Filter out only religious figure from all vital people
    vital_people_religious_figures_df=vital_people_df[vital_people_df['Category']=='Religious Figure']

    #Get individual sentiments average
    religious_figures_positive=vital_people_religious_figures_df['Positive_Words_%'].mean()
    religious_figures_negative=vital_people_religious_figures_df['Negative_Words_%'].mean()
    religious_figures_neutral=vital_people_religious_figures_df['Neutral_Words_%'].mean()

    #Filter out only sport figure from all vital people
    vital_people_sport_figures_df=vital_people_df[vital_people_df['Category']=='Sport Figure']

    #Get individual sentiments average
    sport_figures_positive=vital_people_sport_figures_df['Positive_Words_%'].mean()
    sport_figures_negative=vital_people_sport_figures_df['Negative_Words_%'].mean()
    sport_figures_neutral=vital_people_sport_figures_df['Neutral_Words_%'].mean()

    #Setting up matplotlib
    N = 14
    ind = np.arange(N)
    width = 0.25

    #Setting up positive sentiments average for all categories
    xvals=[writers_positive,musicians_and_composers_positive,visual_artist_positive,directors_positive,entertainers_positive,philosophers_positive,scientists_and_mathematicians_positive,explorers_positive,business_people_positive,politicians_positive,military_leaders_positive,revolutionaries_and_activists_positive,religious_figures_positive,sport_figures_positive]
    bar1 = plt.bar(ind, xvals, width, color = 'r')

    #Setting up neutral sentiments average for all categories
    # yvals=[writers_neutral,musicians_and_composers_neutral,visual_artist_neutral,directors_neutral,entertainers_neutral,philosophers_neutral,scientists_and_mathematicians_neutral,explorers_neutral,business_people_neutral,politicians_neutral,military_leaders_neutral,revolutionaries_and_activists_neutral,religious_figures_neutral,sport_figures_neutral]
    # bar2 = plt.bar(ind+width, yvals, width, color='g')

    #Setting up negative sentiments average for all categories
    zvals=[writers_negative,musicians_and_composers_negative,visual_artist_negative,directors_negative,entertainers_negative,philosophers_negative,scientists_and_mathematicians_negative,explorers_negative,business_people_negative,politicians_negative,military_leaders_negative,revolutionaries_and_activists_negative,religious_figures_negative,sport_figures_negative]
    bar3 = plt.bar(ind+width, zvals, width, color = 'b')

    plt.xlabel("Categories")
    plt.ylabel('Proportion(in %)')
    plt.title("Category Wise Sentiments Proportion")

    plt.xticks(ind+width,['Writer','Musicians','Visual Artist','Director',
      'Entertainers','Philosophers',
      'Scientists','Explorer','Business People',
      'Political Leader','Military Leaders',
      'Revolutionaries','Religious Figure','Sport Figure'],rotation=30)
    plt.legend( (bar1, bar3), ('Positive Sentiments', 'Negative Sentiments') )

    plt.show()

    #Read in serial killer file
    serial_killer_df=pd.read_excel('Data\\serial_killer_people_with_sentiments.xlsx')

    #Plot positive and negative sentiments proportion with comparison between vital people and serial killers

    #Positive Words Proportion

    #Create x axis labels
    label=np.arange(490)

    #Labels for x axis
    x1=label
    x2=label

    #Vital People positive words proportions
    y1=vital_people_df['Positive_Words_%'][:490]

    #Serial killers positive words proportions
    y2=serial_killer_df['Positive_Words_%']

    #Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Vital People Vs. Serial Killer Positive words proportion')

    ax1.plot(x1, y1, 'o-')
    ax1.set_ylabel('Vital People Positive Words Proportion')

    ax2.plot(x2, y2, '.-')
    ax2.set_xlabel('Wikipedia Article Count')
    ax2.set_ylabel('Serial Killer Positive Words Proportion')

    plt.show()


    #Negative Words Proportion

    #Create x axis labels
    label=np.arange(490)

    #Labels for x axis
    x1=label
    x2=label
    #
    #Vital People positive words proportions
    y1=vital_people_df['Negative_Words_%'][:490]

    #Serial killers positive words proportions
    y2=serial_killer_df['Negative_Words_%']

    #Plotting
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Vital People Vs. Serial Killer Negative words proportion')

    ax1.plot(x1, y1, 'o-')
    ax1.set_ylabel('Vital People Negative Words Proportion')

    ax2.plot(x2, y2, '.-')
    ax2.set_xlabel('Wikipedia Article Count')
    ax2.set_ylabel('Serial Killer Negative Words Proportion')

    plt.show()


    #Creating box plot

    data=[vital_people_df['Positive_Words_%'][:490],serial_killer_df['Positive_Words_%'],vital_people_df['Negative_Words_%'][:490],serial_killer_df['Negative_Words_%']]

    fig = plt.figure(figsize =(10, 7))

    labels = ['Vital People Positive', 'Serial Killer Positive', 'Vital People Negative', 'Serial Killer Negative']

    # Creating plot
    bp = plt.boxplot(data,meanline=True, showmeans=True, showcaps=True, showbox=True, showfliers=True, vert=True, patch_artist=True, labels=labels)

    colors = ['blue', 'green', 'blue', 'green']

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # show plot
    plt.show()

    #Kolmogorov Smirnov test for testing positive words proportion between vital people and serial killer

    print("Kolmogorov Smirnov test result for difference between vital people and serial killer for positive words", ks_2samp(vital_people_df['Positive_Words_%'],serial_killer_df['Positive_Words_%']))

    print("Kolmogorov Smirnov test result for difference between vital people and serial killer for negative words", ks_2samp(vital_people_df['Negative_Words_%'],serial_killer_df['Negative_Words_%']))






