from collections import Counter
import spacy
nlp = spacy.load('en_core_web_sm')

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
    
wholeDoc = []
for key,value in allText.items():
    # print("key: " + str(key) + ", value: " + str(value))
    text = value[1]
    # tokenise words and give it its POS tag
    docs = nlp(text)
    for token in docs:
        if not token.is_stop and not token.is_punct and not token.text=="-" and not token.text == "\n":
            wholeDoc.append(token.lemma_.strip().lower())
    # put it back in allText dictionary
    allText[key] = [value[0], value[1], docs]

# word_freq = Counter(wholeDoc)
# common_words = word_freq.most_common(5)

for key, value in allText.items():
    for token in value[2]:
        print("token: " + token.text)
        # if(token.pos_=="DET") :
            # print("key: " + str(key) + ", value: " + str(value[2]))
            # print("ancestors: " + str(list(token.ancestors)) )
        print("subtree: " + str(list(token.subtree)))
            # if len(list(token.ancestors)) > 0: 
            # if len(list(token.subtree)) > 1:
            #     print("ancestors: " + str(list(token.ancestors))) 
            # text = value[1]
            # toReplace = ""
            # temp = token
            
            # for item in token.ancestors:
            #     # print("items " + str(item.text) + ", pos: " + str(item.pos_))
            #     if item.text == "\n" or item.is_punct or item.text == "." or item.text==" " or len(item.text) == 1:
            #         continue
            #     text = text.replace(item.text, "\\bold" + item.text + "\\bold")
            #     # print("text after replace child: " + str(text))
            # if len(token.text) > 1: 
            #     text = text.replace(token.text, "\\bold" + token.text + "\\bold")
            # #can use regex
            # text = text.replace("\\bold\\bold", "\\bold")
            # print("text after replace child and token: " + str(text))
        
            # for token in value[2]:
            #     print("token text: " + token.text + ", pos tag: " + token.pos_)
