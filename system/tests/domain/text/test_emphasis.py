from src.domain.viz.circle import Circle
from src.domain.text.emphasis import Emphasis


def test_emphasis():
    phrase = "test phrase"
    shape = Circle(100, 100, 10)
    emphasis = Emphasis(phrase, shape)

    assert emphasis.phrase == phrase
    assert emphasis.shape.type == "circle"
    assert emphasis.shape.x == 100
    assert emphasis.shape.y == 100
    assert emphasis.shape.r == 10


circle_dict = {
                  "phrase": "The spike around 1000 calories",
                  "shape": {
                      "type": "circle",
                      "x": 339,
                      "y": 460,
                      "r": 45
                  }
              }

rect_dict = {
                "phrase": "fewer than 650 calories such as a cheese-free burrito bowl",
                "shape": {
                    "type": "rectangle",
                    "x": 2,
                    "y": 0,
                    "w": 220,
                    "h": 500
                }
              }


def test_emphasis_from_dict():
    circle_emph = Emphasis.from_dict(circle_dict)

    assert circle_emph.phrase == circle_dict["phrase"]
    assert circle_emph.shape.x == circle_dict["shape"]["x"]
    assert circle_emph.shape.y == circle_dict["shape"]["y"]
    assert circle_emph.shape.r == circle_dict["shape"]["r"]

    rect_emph = Emphasis.from_dict(rect_dict)

    assert rect_emph.phrase == rect_dict["phrase"]
    assert rect_emph.shape.x == rect_dict["shape"]["x"]
    assert rect_emph.shape.y == rect_dict["shape"]["y"]
    assert rect_emph.shape.width == rect_dict["shape"]["w"]
    assert rect_emph.shape.height == rect_dict["shape"]["h"]
