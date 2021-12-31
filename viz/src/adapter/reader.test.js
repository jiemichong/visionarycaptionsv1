import { jsonToCaptions } from './reader.js';


test("reader should be able to convert caption data into Caption object", () => {
    var data = {
        "captions": [
            {
                "index": 1,
                "start": "00:00:01,920",
                "end": "00:00:08,720",
                "text": "The histogram above shows the distribution of calories for all orders."
            },
            {
                "index": 2,
                "start": "00:00:08,720",
                "end": "00:00:14,480",
                "text": "The spike around 1000 calories represents standard burrito orders"
            }
        ]
    };

    var captions = jsonToCaptions(data)
    expect(captions[0].start).toBe("00:00:01,920");    
});