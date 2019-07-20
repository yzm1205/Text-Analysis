import pandas as pd
import numpy
import nltk
from nltk import *
import matplotlib.pyplot as plt
from nltk.stem.porter import PorterStemmer
from nltk.stem import *

from nltk.probability import FreqDist
nltk.download("punkt")
nltk.download('stopwords')
from nltk.corpus import stopwords


from nltk import word_tokenize
from string import *
import os
import unicodedata



base_path = "C:\Users\yash\Desktop\minorproject\FINAL_CODE\testing_files"  #location of file must be specified
filename = "xyz.txt"
path_to_file = os.path.join (base_path, filename)
fd = open(path_to_file ,'r+')
reed=fd.read()
#print reed



#REMOVING ALL THE PUNCTAUTION AND THE NUMERIC DIGITS FROM THE TEXT
def action():
   
    txt="".join(c for c in reed if not c.isdigit() ) #remove digits from the txt
    txt="".join(c for c in txt if c not in punctuation)     #remove punctaution 
    #print txt

#########################################

#REMOVING ALL THE STOPWORDS OT THE ARTICLES FROM THE TEXT
#AND CONVERTING TEXT INTO THE TOKENS FOR FREQUENCY DISTRIBUTION

stop_words = set(stopwords.words('english'))
stop_words.update(("would","a","i","so","may","also","stephen","hawking","Chapter","like","If","This","let","with","We","But","It","us","Let","To","His","In","For","The"))
word_tokens = word_tokenize(txt)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
     if w not in stop_words:
     filtered_sentence.append(w.lower())
 
#print(word_tokens)
#print(filtered_sentence)

#####################################################

#CALCULATING FREQUENCY DISTRIBUTION TO PLOT THE GRAPH

fdist=FreqDist(filtered_sentence)
count_frame = pd.DataFrame(fdist , index = [0]).T
count_frame.columns=['count']
#print count_frame

#######################################################

counts=count_frame.sort_values("count",ascending = False)

fig=plt.figure(figsize=(80,20))
ax=fig.gca()
counts['count'][:70].plot(kind='bar',ax=ax)
ax.set_title("Frequency of File" )
ax.set_ylabel('freq of words in hundreds')
ax.set_xlabel('word')
plt.show()
return


