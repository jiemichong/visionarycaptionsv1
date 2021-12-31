import './style.css';
import * as d3 from 'd3';

import { Visuzalization } from './infra/visualization.v2.js';

// KH: I think the implementation of `Visualization` becomes cleaner if I read a json file like
d3.json('/data/caption.emphasis.v3.json')
    .then(function (data) {
        var viz = new Visuzalization();
        viz.start(data);
    })



