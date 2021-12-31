import json

from flask import Flask, Response
from src.adapter.serializer.caption_encoder import CaptionJsonEncoder
from src.domain.text.caption import Caption
from src.infra.repository.caption_repository import CaptionRepository

# To-Do. The applicaiton should be instantiated in infrastructure (`infra/server/`)
app = Flask(__name__)

# To-Do. The REST API should be designed in infrastructure (`infra/server/`)
@app.route("/")
def get_captions():
    # To-Do. It should not read the v3 file, but instead it should process the original caption file.
    with open("./data/caption.emphasis.v3.json") as f:
        data = json.load(f)
    captions = [Caption.from_dict(d) for d in data['captions']]
    caption_repo = CaptionRepository(captions)

    # To-Do. Emphasize the caption and extract the visualization information.
    ###

    captions = caption_repo.list()
    json_caption = json.dumps(captions, cls=CaptionJsonEncoder)

    response = Response(json_caption, mimetype='application/json')

    return response
