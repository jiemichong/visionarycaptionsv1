import json

from src.domain.text.caption import Caption
from src.adapter.serializer.caption_encoder import CaptionJsonEncoder


def test_serialize_caption():
    with open("../../../data/caption.emphasis.v3.json") as f:
        data = json.load(f)
    caption_data = data['captions'][1]
    caption = Caption.from_dict(caption_data)

    expected_json = """
    {
        "index": 2,
        "start": "00:00:08,720",
        "end": "00:00:14,480",
        "text": "The spike around 1000 calories represents standard burrito orders",
        "properties": {
          "emphasis": [
              {
                  "phrase": "The spike around 1000 calories",
                  "shape": {
                      "type": "circle",
                      "x": 339,
                      "y": 460,
                      "r": 45
                  }
              }
          ]
        }
      }
    """

    json_caption = json.dumps(caption, cls=CaptionJsonEncoder)
    assert json.loads(json_caption) == json.loads(expected_json)
