from collections import Counter
import re
import os

StopWords = set(["the","and","or","but","to","of","a","an","in","on","for","with","as","by","at"])

file_name = 'paragraphs.txt'
directory = 'F:\\UNI\\semester 4\\Cloud Computing'
file_path = os.path.join(directory, file_name)

with open(file_path,'r') as file:
    
    words = re.findall(r'\b\w+\b', file.read())

words = [word for word in words if word.lower()not in StopWords]

word_freq = Counter(words)

for word,freq in word_freq.items():
    print(word+": "+str(freq))