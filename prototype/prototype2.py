from collections import Counter
import spacy
nlp = spacy.load('en_core_web_sm')
from num2words import num2words
from word2number import w2n

srt = []
with open('./prototype.srt') as reader: 
    srt = reader.readlines()

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

for key,value in allText.items(): 
    words = "" 
    text = value[1]
    text = text.replace("1 in 10 meals", "\\bold" + "1 in 10 meals" + "\\bold")
    text = text.replace("fewer than", "\\bold" + "fewer than" + "\\bold")
    text = text.replace("650 calories", "\\bold" + "650 calories" + "\\bold")
    text = text.replace("The spike around 1000 calories", "\\bold" + "The spike around 1000 calories" + "\\bold")
    splitWords = text.split(" ")
    for word in splitWords: 
        words += word + " "
    print("words " + words)
    allText[key] = [value[0], words]

with open('./output.srt', "w") as srt:
    for key, value in allText.items():
        srt.writelines(str(key) + "\n")
        srt.writelines(value[0])
        srt.writelines(value[1])
        srt.writelines("\n")

with open('./output.txt', "w") as phrases:
    phrases.writelines("1 in 10 meals\n")
    phrases.writelines("fewer than")
    phrases.writelines(" 650 calories\n")
    phrases.writelines("The spike around 1000 calories")

# print(words)