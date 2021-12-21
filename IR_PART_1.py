import glob
import os
import string
import pandas as pd
import math
import numpy as np


os.chdir(r'C:\Users\youss\OneDrive\Desktop\DocumentCollectiion')
myFiles= glob.glob('*.txt')


def sort(f):
      return int(f.split(".")[0])

myFiles.sort(key=sort)


stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


final_words = []


for file in myFiles:
    
    
    print("\n\n")
    print(file)
    print("\n")
    text = open(file,encoding='utf-8').read()
    lower = text.lower()
    cleaned_text = lower.translate(str.maketrans('','',string.punctuation))
    tokens = cleaned_text.split()
    print(tokens)
    print("\n")
    print("======================================================================================================================================")
    print("\n")
    for word in tokens:
        
        if word not in stop_words:
        
            final_words.append(word)
            
    print(final_words)
    final_words.clear()
        
        
    
 
   