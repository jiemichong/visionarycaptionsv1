from adapter.svg_adapter import retrieve_rect
from domain.viz.histogram import Histogram
from application.text_to_viz import TextToViz

from adapter.extract_emphasis import load_data
from application.new_captions import write_new_captions
import json     

from xml.dom import minidom


def main():
    #Part 1: NLP portion
    caption_data = load_data() 
    new_captions, phrases = write_new_captions(caption_data)
    d = { "captions": new_captions }
    captions_json = json.dumps(d, indent = 2)  

    print(captions_json)

    # #Part 2: System portion
    # svg_filename = "data/testchipotle.svg"
    # with open(svg_filename) as svg_file:
    #     svg_doc = minidom.parse(svg_file)
    #     rectangles = retrieve_rect(svg_doc)
    #     histogram = Histogram(rectangles)
    #     TextToViz(phrases, histogram).run()


#TODO:
# 1. How should the captions json object be stored?
# 2. TextToViz: Actual coordinates of the shapes


if __name__=="__main__":
    main()
