// src/infra/visualization.js
import * as d3 from 'd3';
import { jsonToCaptions } from '../adapter/reader.js';
import { CaptionLoader } from '../application/captionLoader.js';
import { Circle } from '../domain/annotations/circle.js';
import { Rectangle } from '../domain/annotations/rectangle.js';


export const Visuzalization = class {
    constructor() {
        this.svg = d3.select("#canvas").select("svg");
        this.height = parseInt(this.svg.attr("height"), 10);
    }

    start(json) {

        // const data = await d3.json('/data/caption.emphasis.v2.json');
        const captions = jsonToCaptions(json);

        const captionLoader = new CaptionLoader(captions, this.show.bind(this));

        captionLoader.start();
    }

    show(caption) {
        var captionField = document.getElementById('caption-field');
        captionField.innerHTML = caption.emphasize();

        // KH: Let's move all the rendering related stuff in the infra layer.
        this.svg.selectAll("g.annotation").remove()

        var y = d3.scaleLinear().domain([0, this.height]).range([this.height, 0]);

        if (caption.emphases.length > 0) {
            const emphasis = caption.emphases[0];
            const shape = emphasis.shape;
            const el = document.getElementById("test");
            const rect = el.getBoundingClientRect();
            const lineTarget = {
                lineX: rect.right - rect.left,
                lineY: y(rect.top)
            };
            console.log(lineTarget);
            if (shape instanceof Circle) {
                this.svg.append("g")
                    .attr("class", "annotation")
                    .append("circle")
                    .attr("cx", shape.x)
                    .attr("cy", y(shape.y))
                    .attr("r", shape.r)
                    .style("fill", '#00000F')
                    .style("opacity", 0.3)
            } else if (shape instanceof Rectangle) {
                console.log(shape);
                this.svg.append("g")
                    .attr("class", "annotation")
                    .append("rect")
                    .attr("x", shape.x)
                    .attr("y", shape.y)
                    .attr("width", shape.width)
                    .attr("height", shape.height)
                    .style("fill", '#00000F')
                    .style("opacity", 0.3);
            }

            const line = d3.linkHorizontal()
                .x(d => d.lineX)
                .y(d => y(d.lineY))({
                    source: shape.lineSource,
                    target: lineTarget
                });

            this.svg.append("g")
                .append('path')
                .attr('d', line)
                .attr('marker-end', 'url(#arrow)')
                .attr('stroke', 'black')
                .attr("stroke-width", 4);
        }
    }
};