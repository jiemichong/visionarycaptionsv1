import json

from src.domain.text.caption import Caption
from src.domain.text.emphasis import Emphasis
from src.domain.text.properties import Properties


def test_caption_initializes():
    caption = Caption(1, "start", "end", "test text", None)
    assert caption.index == 1
    assert caption.start == "start"
    assert caption.end == "end"
    assert caption.text == "test text"


def test_load_from_json():
    with open("../../../data/caption.emphasis.v3.json") as f:
        data = json.load(f)
    caption_data = data['captions'][1]
    properties = Properties([Emphasis.from_dict(emph)for emph in caption_data["properties"]["emphasis"]])

    caption = Caption.from_dict(caption_data)

    assert caption.index == 2
    assert caption.start == "00:00:08,720"
    assert caption.end == "00:00:14,480"
    assert caption.text == "The spike around 1000 calories represents standard burrito orders"

    assert caption.properties == properties
