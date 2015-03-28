from flask import Flask
from flask import render_template
import random
import threading
import os

import tweet_collector

app = Flask(__name__)

app.debug = True


class ProcessingThread(threading.Thread):

    def __init__(self, search_term):
        self.search_term = search_term

    def run(self):
        c = tweet_collector.Collect()
        c.connect()
        for tweet in c.stream(self.search_term):
            pass


@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=random.randint(1,1000))

if __name__ == '__main__':
    app.run()


if os.environ['WE_ARE_LIVE']:
    pt = ProcessingThread('transgender')
