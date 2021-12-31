import { isEmpty } from "lodash";

// src/application/captionLoader.js
export const CaptionLoader = class {
    constructor(captions, show) {
        this.captions = captions;
        this.show = show;
    }

    start() {
        this._showNext();
    }

    _showNext () {
        var that = this;

        if (that.captions.length > 0) {
            var caption = this.captions.shift();
            caption.emphasize();
            this.show(caption);

            var sec = caption.duration();
            setTimeout(this._showNext.bind(this), sec * 1000);
        }
    }
};