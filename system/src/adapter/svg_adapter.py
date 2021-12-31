from src.domain.viz.rectangle import Rectangle


def retrieve_rect(svg_doc):
    """
    :param svg_doc: return value of minidom.parse(svg_file)
    :return:
    """
    groups = svg_doc.getElementsByTagName('g')
    g_rect_containers = [g for g in groups if g.getAttribute('class') == 'g-rect-container']
    rectangles = []
    for g in g_rect_containers:
        transform = str(g.getAttribute('transform'))
        rect_element = g.getElementsByTagName('rect')[0]
        x = 0
        y = float(rect_element.getAttribute('y'))
        width = float(rect_element.getAttribute('width'))

        height = rect_element.getAttribute('height')
        if height == "":
            height = 0

        rectangles.append(Rectangle(x, y, width, height, transform))
    return rectangles
