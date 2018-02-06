from __future__ import print_function
import praw
import os
import datetime as dt
import time
import csv
import re

SCR_CLIENT_ID = os.environ["SCR_CLIENT_ID"]
SCR_CLIENT_SECRET = os.environ["SCR_CLIENT_SECRET"]
SCR_PASSWORD = os.environ["SCR_PASSWORD"]
SCR_USERAGENT = os.environ["SCR_USERAGENT"]
SCR_USERNAME = os.environ["SCR_USERNAME"]


class RedditScraper():
    def __init__(self, subreddit):
        self.post_list = []
        self.api = praw.Reddit(client_id = SCR_CLIENT_ID,
                client_secret = SCR_CLIENT_SECRET, password = SCR_PASSWORD,
                user_agent = SCR_USERAGENT, username = SCR_USERNAME)
        self.sr = self.api.subreddit(subreddit)

    def get_posts_in_date_range(self, start_date, end_date, posts_per_day):
        """
        start_date (YYYY-MM-DD)
        end_date (YYYY-MM-DD)
        """
        start_date_ts = time.mktime(dt.datetime.strptime(start_date, '%Y-%m-%d').timetuple())
        end_date_ts = time.mktime(dt.datetime.strptime(end_date, '%Y-%m-%d').timetuple())
        loop_ts = start_date_ts
        while loop_ts <= end_date_ts:
            self.get_top_posts_from_date(loop_ts, posts_per_day)
            loop_ts = int(loop_ts + dt.timedelta(days=1).total_seconds())

    def get_top_posts_from_date(self, start_date_ts, posts_per_day):
        """
        Get top post of the day
        """

        end_date_ts = int(start_date_ts + dt.timedelta(days=1).total_seconds())
        query = 'timestamp:{}..{}'.format(start_date_ts, end_date_ts)
        results = self.sr.search(query, limit=posts_per_day, params={}, sort='top', syntax='cloudsearch')
        for result in results:
            self.post_list.append(result)

    def make_csv(self, children):
        """
        Generates CSV file from the list of Reddit Submission objects
        """

        OUTPUT_FILE = '../data/reddit.csv'
        csv_file_handle = open(OUTPUT_FILE, 'w')
        out_csv = csv.writer(csv_file_handle, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        out_csv.writerow(['date', 'subreddit', 'title', 'upvotes'])
        regex = re.compile('[^a-zA-Z1-9\s]')

        def clean_data(text):
            intermediate_text = re.sub('\n', '\n', text)
            return regex.sub('', intermediate_text)

        counter = 0
        for child in children:
            counter += 1
            # if (len(children) % 100 == 0):
            print (str(counter) + " items processed")
            title = child.title
            upvotes = child.ups
            time_from_epoch = child.created_utc
            date = dt.datetime.utcfromtimestamp(time_from_epoch).strftime('%Y-%m-%d')
            cleaned_data = clean_data(title)
            subreddit = child.subreddit
            out_csv.writerow([date, subreddit, cleaned_data, upvotes])


rs = RedditScraper('bitcoin')
rs.get_posts_in_date_range('2007-01-16', '2018-01-30', 1)
rs.make_csv(rs.post_list)
