import spacy
nlp = spacy.load("en_core_web_sm")

def write_new_captions(caption_data):
    sentences = [caption['text'] for caption in caption_data['captions']]
    new_captions = []
    phrases = []
    for idx, sentence in enumerate(sentences, 1):
        doc = nlp(sentence)
        nummods = [token for token in doc if token.dep_ == "nummod"]
        emphasis_texts = []
        for nummod in nummods:    
            for token in doc:
                if nummod in token.lefts:
                    emph = ''.join([t.text_with_ws for t in token.subtree]).strip()
                    print(emph)
                    emphasis_texts.append(emph)
                    phrases.append(emph)
                    
        _caption = next(filter(lambda cap: cap['index'] == idx, caption_data['captions']))
        _caption['properties'] = {}
        _caption['properties']['emphasis'] = emphasis_texts
        new_captions.append(_caption)
    return new_captions, phrases

