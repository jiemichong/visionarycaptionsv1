import json

from src.domain.text.caption import Caption


class CaptionJsonEncoder(json.JSONEncoder):
    """
    https://stackoverflow.com/questions/5160077/encoding-nested-python-object-in-json
    """
    def default(self, o: Caption):
        return o.to_dict()