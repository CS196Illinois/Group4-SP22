from msilib import Table
from unicodedata import name
from keywords import extractors
import pandas as pd
import random
import csv

class whytry:
    def __init__(self, script):
        self.script = script
    def keyword_extract(self):
       extractor = extractors.KeyBertExtractor(self.script)
       return extractor.get_n_best(5)



def guess_word(script):
    first_words = whytry(script)
    guess_word = first_words.keyword_extract()
    final_word = {}
    for x in guess_word:
        for y in x[0].split(" "):
            if y in final_word:
                final_word[y] += guess_word[1] 
            else:
                final_word[y] = guess_word[1]
    sorted_keys = sorted(final_word)
    return sorted_keys[0:3]



# three word function 

data = []
filename = 'file_name.csv'
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)
    i = 0
    for row in datareader:
        print("processing file " + str(i) + " out of 1161")
        try:
            script_file = open("cs124dataset/" +row[2], 'r', encoding='utf-8')
            movie_text = script_file.read()
            words = movie_text.split()
            randomwords = [random.choice(words) for i in range(300)]
            threewords = guess_word(" ".join(randomwords))
            data.append([row[0], row[1], threewords])
        except:
            print("file " + str(i) + " didn't work")
        i += 1
df = pd.DataFrame(data, columns = ["Movie_Title", "Year", "ThreeWords"])
df.to_csv("threewords.csv")