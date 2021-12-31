import json

from src.domain.text.caption import Caption
from src.infra.repository.caption_repository import CaptionRepository

def test_caption_repository():
    with open("../../../data/caption.emphasis.v3.json") as f:
        data = json.load(f)
    captions = [Caption.from_dict(d) for d in data['captions']]
    caption_repo = CaptionRepository(captions)
    assert caption_repo.list() == captions
