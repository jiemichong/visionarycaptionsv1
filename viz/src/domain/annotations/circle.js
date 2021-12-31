// src/domain/annotation/circle.js
import * as d3 from 'd3';

export const Circle = class {
    constructor(x, y, r) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.svg = d3.select("#canvas").select("svg");
        this.lineSource = {
            lineX: this.x + this.r,
            lineY: this.y
        };
    }

    // display () {
    //     this.svg.append("g")
    //         .append("circle")
    //         .attr("x", this.cx)
    //         .attr("y", this.cy)
    //         .attr("r", this.r)
    //         .style("fill", '#00000F')
    //         .style("opacity", 0.3);
    // }
};

export function createCircle(x, y, r) {
    return new Circle(x, y, r);
}