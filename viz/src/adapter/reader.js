// src/adapter/reader.js

import _ from 'lodash';
import { Caption } from '../domain/caption/caption.js';
import { createEmphasis } from '../domain/caption/emphasis.js';

export function jsonToCaptions(json) {
    var captions =  _.map(json["captions"], (d) => { 
        var emphases = _.map(d["properties"]["emphasis"], function (emph) {
            return createEmphasis(emph["phrase"], emph["shape"]);
        });

        return new Caption(d["index"], d["start"], d["end"], d["text"], emphases); 
    })
    return captions;
}