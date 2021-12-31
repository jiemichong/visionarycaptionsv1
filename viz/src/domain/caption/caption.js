// src/domain/caption/caption.js
import _ from 'lodash';
export const Caption = class {
    constructor(index, start, end, text, emphases) {
        this.index = index;
        this.start = start;
        this.end = end;
        this.text = text;
        this.emphases = emphases;
    }

    _toSec (timeStr) {
        // "00:00:08,720"
        var _timeStr =  _.split(timeStr, ',')
        var _timeMsec = parseFloat(_timeStr[1]) / 1000;
        var _timeStr2 = _.split(_timeStr[0], ':');
        var _timeSec = parseInt(_timeStr2[2], 10);
        return _timeSec + _timeMsec;
    }

    duration () {
        "00:00:08,720"
        var start =  this._toSec(this.start)
        var end = this._toSec(this.end);

        return end - start;
    }

    emphasize () {
        // KH: I prefer to write a code in one of two ways: a method without a side-effect (query) or with a side-effect (command).   
        // See "What to Test? Origins and Types of Messages" in this tutorial: https://www.notion.so/smuhci/SE-Test-Driven-Development-f17c2b81e9174f02a1ee1751740fb089
        // The current implementation has a side-effect (it changes the state of `this.text` and then returns `this.text`. 
        // So I'll change it just return the updated text

        if (this.emphases.length != 0) {    
            const emphasis = this.emphases[0];
            return this.text.replace(emphasis.phrase, "<b style='color:#9E4B6C' id='test'>" + emphasis.phrase + "</b>");
        } else {
            return this.text;            
        }
    }
};