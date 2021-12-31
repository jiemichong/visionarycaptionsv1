from collections import Counter
import spacy
nlp = spacy.load('en_core_web_sm')
from num2words import num2words
from word2number import w2n

srt = []
with open('./prototypeV2.srt') as reader: 
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

allText[key] = [timestamp, text]

wholeDoc = {}
index = 0
for key,value in allText.items():
    text = value[1]

    docs = nlp(text)
    for token in docs: 
        wholeDoc[index] = [token,token.text]
        index += 1
    allText[key] = [value[0], docs, index, text]

totalWords = index
lastPos = 0

maxWords = ["spike", "maximum", "highest"]
minWords = ["minimum", "fewest"]
comparativeWords = ["more", "less", "fewer", "lesser", "higher", "lower", "bigger", "smaller"]
complementaryWords = ["than"]
for key,value in allText.items(): 
    end = int(value[2])
    text = value[3]

    for i in range (lastPos, end):
        word = wholeDoc[i][0]
        # print(word.lemma_ + " pos " + str(word.pos_))
        # print(list(word.subtree))
        # print(list(word.ancestors))
        if word.pos_ == "NUM": 
            case1 = True
            #case 1: not comparative like 1 in 10 
            for token in word.subtree: 
                if token.pos_ == "NUM" and token.text != word.text:
                    case1 = False
            if case1 and len(list(word.subtree)) > 1:
                for token in word.subtree:
                    text = text.replace(token.text, "\\bold" + token.text +"\\bold")
        elif word.lemma_ in maxWords or word.lemma_ in minWords or word.text in comparativeWords: 
            start = i
            lastWord = ""
            stop = -1
            for token in word.subtree:
                if token.text != word.text:
                    start = start - 1
            for token in word.ancestors: 
                if token.pos_ != "VERB":
                    lastWord = token.text
            
            for j in range(i, end):
                curr = wholeDoc[j][1] 
                if lastWord == curr:
                    stop = j
            
            if stop == -1:
                continue

            for k in range(start, stop + 1): 
                text = text.replace(wholeDoc[k][1], "\\bold" + wholeDoc[k][1]+"\\bold")
            
        elif word.lemma_ == "in":
            inPos = i
            firstNum = inPos - 1
            if firstNum < 0:
                continue
                
            if wholeDoc[inPos+1][0].pos_ != "NUM":
                continue

            text = wholeDoc[lastPos][1] 
            for j in range(lastPos+1, firstNum): 
                text += " " + wholeDoc[j][1]
            
            text += " " + "\\bold" + wholeDoc[firstNum][1]+"\\bold"
            text += " " + "\\bold" + wholeDoc[inPos][1]+"\\bold"
            text += " " + "\\bold" + wholeDoc[inPos+1][1]+"\\bold"

            for k in range(inPos+2, end):
                text += " " + wholeDoc[k][1]

            for token in word.subtree:
                if token.pos_ != "NUM": 
                    text = text.replace(token.text, "\\bold" + token.text+"\\bold")            

    #clean up over bold: 
    text = text.replace("\\bold\\bold", "\\bold")
    print("final text : " + text)
    allText[key] = [value[0], value[1], value[2], text]
    lastPos = end

with open("./output.txt", "w") as writer:
    for key, value in allText.items():
        text = value[3]
        splitWords = text.split(" ")
        toWrite = ""
        for word in splitWords:
            if "\\bold" in word:
                word = word.replace("\\bold", "")
                toWrite += word + " "
                
        if toWrite:
            toWrite = toWrite[:-1] + "\n"
            writer.writelines(toWrite)


with open("./output.srt", "w") as writer2:
    for key, value in allText.items():
        writer2.writelines(str(key) + "\n")
        writer2.writelines(value[0])
        writer2.writelines(value[3])
        writer2.writelines("\n")



