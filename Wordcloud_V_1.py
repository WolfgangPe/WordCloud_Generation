#Import of relevant packages
import csv
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Load the *data*.csv for the WordCloud
data = pd.read_csv(r"C:\Users\Paul\Desktop\Code\WordCloud_Generation\kicker_bl_li_tweets.csv")

# Load a List of Stopwords for filtering
Ignore = open(r"C:\Users\Paul\Desktop\Code\WordCloud_Generation\Stopwords.txt",'r').read().split()

#Set and update Stopwords
STOPWORDS.update(Ignore)
stopwords = set(STOPWORDS)

# Generation of a WordCloud image with a set of customization
wordcloud = WordCloud(
    background_color='white',
    stopwords=stopwords,
    max_words=5000,
    width=1920,
    height=1080,
    max_font_size=1000

                      ).generate(str(data))
#Plotter

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
