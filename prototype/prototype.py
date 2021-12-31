from collections import Counter
import spacy
nlp = spacy.load('en_core_web_sm')
from num2words import num2words
from word2number import w2n

srt = []
with open('./prototype.srt') as reader: 
    srt = reader.readlines()

# extract text by timestamp
allText = {}
key = 0
gotTimestamp = False
timestamp = ""
text = ""
for line in srt:
    if line == "\n": 
        allText[key] = [timestamp, text]
        key = 0
        text = ""
        timestamp = ""
        gotTimestamp = False
    elif key == 0: 
        key = int(line)
    elif not gotTimestamp:
        timestamp = line
        gotTimestamp = True
    else: 
        line = line.replace("--", "")
        text += line

wholeDoc = {}
index = 0
for key,value in allText.items():
    text = value[1]
    words = ""
    for word in text.split(" "): 
        if word.isdigit():
            words += num2words(word) +" "
        else:
            words += word + " "
    
    docs = nlp(words)
    for token in docs: 
        wholeDoc[index] = token
        index += 1
    allText[key] = [value[0], words, docs]

totalWords = index

maxWords = ["spike"]
complementWords = ["around", "than"]
minWords = ["fewer"]
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "fifty"]

copyOfDoc = {}
for index, token in wholeDoc.items():
    copyOfDoc[index] = token

for index, token in wholeDoc.items(): 
    wordPosition = index
    if token.lemma_ in maxWords or token.lemma_ in minWords: 
        if (wholeDoc[wordPosition + 1].lemma_ in complementWords): 
            comp = wholeDoc[wordPosition + 1].lemma_
            copyOfDoc[wordPosition + 1] = text.replace(comp, "\\bold" + comp + "\\bold")
            comp = wholeDoc[wordPosition].lemma_
            copyOfDoc[wordPosition] = text.replace(comp, "\\bold" + comp + "\\bold")
            phrase = ""
            for i in range(2): 
                phrase += wholeDoc[wordPosition + i + 2].lemma_ + " "
            
            print("phrase " + phrase)
            if(str(w2n.word_to_num(phrase)).isdigit()):
                for i in range(2): 
                    comp = wholeDoc[wordPosition + i + 2].lemma_
                    copyOfDoc[wordPosition + i + 2] = text.replace(comp, "\\bold" + comp + "\\bold")
    if token.lemma_ == "in": 
        if(wholeDoc[wordPosition - 1].lemma_ in digits and wholeDoc[wordPosition + 1].lemma_ in digits):
            for i in range(3): 
                comp = wholeDoc[wordPosition + i - 1].lemma_
                print("comp " + comp)
                copyOfDoc[wordPosition + i - 1] = text.replace(comp, "\\bold" + comp + "\\bold")


afterProcess = "" 
for key,value in copyOfDoc.items():
    print("value ") 
    print(value)
    if(isinstance(value,str)):
        afterProcess += value +" "
    else: 
        afterProcess += value.lemma_  +" "


# print("after process: " + afterProcess)

