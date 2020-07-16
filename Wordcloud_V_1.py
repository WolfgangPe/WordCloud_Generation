# History

#Import of relevant packages
import csv
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

#Loading of a .txt as csv_file

#with open('Test.txt') as csv_file:
    #csv_reader = csv.reader(csv_file)
    #line_count = 0
    #your_list = '\t'.join([i[0] for i in csv_reader])

data = pd.read_csv("kicker_bl_li_tweets.csv")

# Set Words to Ignore in WordCloud
Ignore="Er Sie Es Und Wie Der Die Das Wieso Weshalb Warum"
ListOfWordsIgnore = Ignore.split()

#Set STOPWORDS
STOPWORDS.update(ListOfWordsIgnore)
stopwords = set(STOPWORDS)

# Generation of a wordcloud image
wordcloud = WordCloud(
    background_color='white',
    stopwords=stopwords,
    max_words=1000,
    max_font_size=40,
     random_state=42

                      ).generate(str(data))

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
