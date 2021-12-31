from src.domain.text.caption import Caption


class CaptionRepository(object):
    def __init__(self, captions: list[Caption]):
        self.captions = captions

    def list(self) -> list[Caption]:
        return self.captions

    def to_dict(self):
        return { "captions": self.captions }