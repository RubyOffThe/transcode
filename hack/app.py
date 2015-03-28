from flask import Flask
from flask import render_template
import os
import json
import logging
import sys

from tweet_collector import (
    global_average_positivity,
    positivity,
    ProcessingThread
)

logger = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)


app = Flask(__name__)

app.debug = True


@app.route('/')
def hello(name=None):
    global positivity
    global global_average_positivity


    for value in positivity:
        global_average_positivity += value

    if len(positivity):
        global_average_positivity = global_average_positivity/len(positivity)

    positivity_percentage = (global_average_positivity+1) * 50 #add one then its from 0-2 then multiple by 50 to get a percentage

    negativity_percentage = 100- positivity_percentage

    evalution_json = json.dumps(
        [
          [ 'positive', positivity_percentage ],
          [ 'negative', negativity_percentage ]
        ]
    )


    return render_template(
        'hello.html', positive=positivity_percentage, sentiment=evalution_json)


if __name__ == '__main__':
    app.run()


if os.environ.get('WE_ARE_LIVE'):
    pt = ProcessingThread('transgender OR tranny OR transexual')
    pt.start()
