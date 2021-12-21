import glob
import os
import string
import pandas as pd
import math
import numpy as np
from collections import Counter 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


os.chdir(r'C:\Users\youss\OneDrive\Desktop\DocumentCollectiion')
myFiles= glob.glob('*.txt')

def sort(f):
      return int(f.split(".")[0])

myFiles.sort(key=sort)

DFdict=[]


def word_count(filename):
        text = open(filename).read()
        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
        tokenized_words = cleaned_text.split()
        c = Counter()
        c.update(tokenized_words)
    
        return c


for files in myFiles:
    
    print("\n\n")
    print(files)
    print("\n")
    text = open(files).read()
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
    tokenized_words = cleaned_text.split()
    
    

    
    
    print("\n=========================TERM_FREQUENCY=================================\n")
    
            
    TF = dict(Counter(tokenized_words))

    print(TF)     
    
        

    
    
    print("\n=========================WEIGHT _ TERM_FREQUENCY=================================\n")
    
    W_TF = 0
    W_TF = {}
    
    for word in TF:
        W_TF[word] = 1 + math.log10(TF[word])
    print(W_TF)     
    
    
    
    
    print("\n=========================DOCUMENT_FREQUENCY=================================\n")

    
    counters = [word_count(files) for files in myFiles]

    total = dict(sum(counters, Counter()))

    print(total)
    
    
    
        
    print("\n\n=============================INVERSE DOCUMENT FREQUENCY=============================\n\n")  
    
    
    IDFDict=0
    
    IDFDict = {}
    
    for word in total:
        IDFDict[word] = math.log10((len(myFiles)) / total[word])
        
    print(IDFDict)


    print("\n\n=============================TERM FREQUENCY _ INVERSE DOCUMENT FREQUENCY=============================\n\n")  
    
    TF_IDFDict=0
        
    TF_IDFDict = {}
    
    
    for word in TF:
        TF_IDFDict[word] = (TF[word] * IDFDict[word])
        
    print(TF_IDFDict)
    




    print("\n\n=============================DOCUMENT LENGTH=============================\n\n")  
    
    length = 0.0
    length1 = 0.0
    
    for word in TF_IDFDict:
        length += math.pow((TF_IDFDict[word]) , 2)
        length1 = math.sqrt(length)
        
    print("Document Length of " , files , " is : " ,  length1)
    
        
   
    
    
    
    print("\n\n=============================NORMALIZED TF _ IDF=============================\n\n")  
    
    NormTF_IDFDict=0
        
    NormTF_IDFDict = {}
    
    
    for word in TF_IDFDict:
        NormTF_IDFDict[word] = (TF_IDFDict[word] / length1)
        
    print(NormTF_IDFDict)
    
    
    
    
   
        
   
    