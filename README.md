# Redditcoin

Redditcoin combines the data from Reddit and Bitcoin price to derive relevant information and analize

---

## Features


This project is built to accommodate needs of ***.

Users can

1)
2)
3)


---

## Production Screen Shots



### 1


### 2


### 3


---

## Behind the scenes


### Data

The Reddit data was optained using the Python script that uses PRAW. Check the requirements.txt to see the dependancies.

The initial data coming in from Reddit is formatted as follows.

```
[
  {
    "kind": "Listing",
    "data": {
      "after": null,
      "whitelist_status": "all_ads",
      "modhash": "",
      "dist": 1,
      "children": [
        {
          "kind": "t3",
          "data": {
            "domain": "self.BitcoinMarkets",
            "approved_at_utc": null,
            "mod_reason_by": null,
            "banned_by": null,
            "media_embed": {},
            "subreddit": "BitcoinMarkets",
            "selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\"md\"&gt;&lt;p&gt;I am interested in historic data for certain currency pairs and crypto exchanges for backtesting of strategies and profit calculations. \nTradingview provides provides charts and technical analysis for quite a few pairs and exchanges. I therefore would be interested to extract the historic data per candle (Open, High, Low, Close) on minute time frame.&lt;/p&gt;\n\n&lt;p&gt;Has anyone already found a way to do this?\nAny python script available to get started?&lt;/p&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;",
            "selftext": "I am interested in historic data for certain currency pairs and crypto exchanges for backtesting of strategies and profit calculations. \nTradingview provides provides charts and technical analysis for quite a few pairs and exchanges. I therefore would be interested to extract the historic data per candle (Open, High, Low, Close) on minute time frame.\n\nHas anyone already found a way to do this?\nAny python script available to get started?",
            "likes": null,
            "suggested_sort": null,
            "mod_note": null,
            "user_reports": [],
            "secure_media": null,
            "is_reddit_media_domain": false,
            "saved": false,
            "id": "7tzvom",
            "banned_at_utc": null,
            "mod_reason_title": null,
            "view_count": null,
            "archived": false,
            "clicked": false,
            "report_reasons": null,
            "author": "windoak",
            "num_crossposts": 0,
            "link_flair_text": null,
            "can_mod_post": false,
            "is_crosspostable": false,
            "pinned": false,
            "score": 6,
            "approved_by": null,
            "over_18": false,
            "hidden": false,
            "num_comments": 1,
            "thumbnail": "",
            "subreddit_id": "t5_2wwh3",
            "hide_score": false,
            "author_cakeday": true,
            "edited": false,
            "link_flair_css_class": null,
            "author_flair_css_class": null,
            "contest_mode": false,
            "gilded": 0,
            "locked": false,
            "downs": 0,
            "brand_safe": true,
            "secure_media_embed": {},
            "removal_reason": null,
            "can_gild": false,
            "is_self": true,
            "parent_whitelist_status": "all_ads",
            "name": "t3_7tzvom",
            "spoiler": false,
            "permalink": "/r/BitcoinMarkets/comments/7tzvom/how_to_extract_historic_data_from_tradingview/",
            "subreddit_type": "public",
            "whitelist_status": "all_ads",
            "stickied": false,
            "created": 1517333362,
            "url": "https://www.reddit.com/r/BitcoinMarkets/comments/7tzvom/how_to_extract_historic_data_from_tradingview/",
            "author_flair_text": null,
            "quarantine": false,
            "title": "How to extract historic data from tradingview?",
            "created_utc": 1517304562,
            "subreddit_name_prefixed": "r/BitcoinMarkets",
            "distinguished": null,
            "media": null,
            "upvote_ratio": 0.87,
            "mod_reports": [],
            "visited": false,
            "num_reports": null,
            "is_video": false,
            "ups": 6
          }
        }
      ],
      "before": null
    }
  },
  {
    "kind": "Listing",
    "data": {
      "after": null,
      "whitelist_status": "all_ads",
      "modhash": "",
      "dist": null,
      "children": [
        {
          "kind": "t1",
          "data": {
            "subreddit_id": "t5_2wwh3",
            "approved_at_utc": null,
            "mod_reason_by": null,
            "banned_by": null,
            "removal_reason": null,
            "link_id": "t3_7tzvom",
            "likes": null,
            "replies": "",
            "user_reports": [],
            "saved": false,
            "id": "dthu6m3",
            "banned_at_utc": null,
            "mod_reason_title": null,
            "gilded": 0,
            "archived": false,
            "report_reasons": null,
            "author": "flyingunicorn222",
            "can_mod_post": false,
            "ups": 1,
            "parent_id": "t3_7tzvom",
            "score": 1,
            "approved_by": null,
            "downs": 0,
            "body": "You can write your own strategies on TradingView using their own script language called \"pine script\" and that will allow you to do some pretty basic but still very revealing backtests!\n\ni don't think downloading their data is \"easily available\" and dumping their data is probably against their terms of service...\nWorth mentioning if your browser is rendering the data you already received the data somehow and should be able to read it somehow either via javascript on your browser or with some sort of http proxy such as https://mitmproxy.org",
            "edited": false,
            "author_flair_css_class": null,
            "collapsed": false,
            "is_submitter": false,
            "collapsed_reason": null,
            "body_html": "&lt;div class=\"md\"&gt;&lt;p&gt;You can write your own strategies on TradingView using their own script language called &amp;quot;pine script&amp;quot; and that will allow you to do some pretty basic but still very revealing backtests!&lt;/p&gt;\n\n&lt;p&gt;i don&amp;#39;t think downloading their data is &amp;quot;easily available&amp;quot; and dumping their data is probably against their terms of service...\nWorth mentioning if your browser is rendering the data you already received the data somehow and should be able to read it somehow either via javascript on your browser or with some sort of http proxy such as &lt;a href=\"https://mitmproxy.org\"&gt;https://mitmproxy.org&lt;/a&gt;&lt;/p&gt;\n&lt;/div&gt;",
            "stickied": false,
            "subreddit_type": "public",
            "can_gild": true,
            "subreddit": "BitcoinMarkets",
            "score_hidden": false,
            "permalink": "/r/BitcoinMarkets/comments/7tzvom/how_to_extract_historic_data_from_tradingview/dthu6m3/",
            "num_reports": null,
            "name": "t1_dthu6m3",
            "created": 1517389955,
            "author_flair_text": null,
            "created_utc": 1517361155,
            "subreddit_name_prefixed": "r/BitcoinMarkets",
            "controversiality": 0,
            "depth": 0,
            "mod_reports": [],
            "mod_note": null,
            "distinguished": null
          }
        }
      ],
      "before": null
    }
  }
]
```


### Languages
Python, JavaScript, HTML, CSS

### Technologies
Flask, React, Bootstrap

---

## How to see a test run






### Use bash script given


In terminal window in the folder downloaded, run the following command

source roster_bash.sh


### Shortcut


Copy the entire paragraph of the following inside the forked folder to run the web app

virtualenv env; source env/bin/activate; dropdb intranet; createdb intranet; pip install -r requirements.txt; echo export secret_key='abc' > secret.sh; source secret.sh; open 'http://localhost:5000'; python server.py;


---

## License

The MIT License (MIT) Copyright (c) 2017 Soo Park

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
