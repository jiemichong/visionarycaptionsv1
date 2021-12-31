import spacy
import json

def load_data():
    spacy.prefer_gpu()

    with open('data/caption.json') as f:
        data = json.load(f)
        return data

