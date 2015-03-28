from flask import Flask
from flask import render_template
import random
import threading
import os
import json

import tweet_collector

app = Flask(__name__)

app.debug = True

positivity = []
global_average_positivity = 0


class ProcessingThread(threading.Thread):

    def __init__(self, search_term):
        self.search_term = search_term

    def run(self):
        global positivity
        c = tweet_collector.Collect()
        c.connect()
        for tweet in c.stream(self.search_term):
                blob = TextBlob(tweet["text"])

                average_positivity = []
                total_positivity = 0

                for sentence in blob.sentences:
                    average_positivity.append(sentence.sentiment.polarity)

                for value in average_positivity:
                    total_positivity += value

                ret_val = total_positivity/len(average_positivity)


                positivity.append(ret_val)




@app.route('/')
def hello(name=None):
    global positivity

    for value in positivity:
        global_average_positivity += value

    global_average_positivity = global_average_positivity/len(positivity)

    positivity_percentage = (global_average_positivity+1) * 50 #add one then its from 0-2 then multiple by 50 to get a percentage

    negativity_percentage = 100- positivity_percentage

    evalution_json = json.dumps([{'positive': positivity_percentage, 'negative': negativity_percentage}], separators=(','))





    return render_template('hello.html', name=random.randint(1,1000), evalution_json  )

if __name__ == '__main__':
    app.run()


if os.environ.get('WE_ARE_LIVE'):
    pt = ProcessingThread('transgender')
