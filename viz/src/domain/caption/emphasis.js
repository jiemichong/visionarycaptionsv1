import { createCircle } from "../annotations/circle";
import { createRectangle } from "../annotations/rectangle";

export const Emphasis = class {
    constructor(phrase, shape) {
        this.phrase = phrase;
        this.shape = shape;
    }
};

export function createEmphasis(phrase, shape) {
    if (shape['type'] === "circle") {
        var shapeObject = createCircle(shape.x, shape.y, shape.r);
    } else if (shape['type'] === "rectangle") {
        var shapeObject = createRectangle(shape.x, shape.y, shape.w, shape.h);
    } else {
        var shapeObject = null;
    }
    return new Emphasis(phrase, shapeObject);
}