// src/infra/visualization.js
import * as d3 from 'd3';
import { jsonToCaptions } from '../adapter/reader.js';
import { CaptionLoader } from '../application/captionLoader.js';


export const Visuzalization = class {
    constructor() {

    }

    async start () {

        const data = await d3.json('/data/caption.json');
        const captions = jsonToCaptions(data);
        
        const captionLoader = new CaptionLoader(captions, this.show);

        captionLoader.start();
    }

    show (caption) {
        console.log(caption);
        var elem = document.getElementById('caption-field');
        console.log(elem);

        elem.textContent = caption.text;
    }
};