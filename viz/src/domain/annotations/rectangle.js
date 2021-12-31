// src/domain/annotation/rectangle.js
import * as d3 from 'd3';

export const Rectangle = class {
    constructor(x, y, width, height) {
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
        this.svg = d3.select("#canvas").select("svg");
        this.lineSource = {
            lineX: this.x + this.width / 2,
            lineY: this.height / 2
        };
    }

    display () {
        this.svg.append("g")
            .append("rect")
            .attr("x", this.x)
            .attr("y", this.y)
            .attr("width", this.width)
            .attr("height", this.height)
            .style("fill", '#00000F')
            .style("opacity", 0.3);
    }
};

export function createRectangle (x, y, w, h) {
    return new Rectangle(x, y, w, h);
}