from flask import Flask
from flask import render_template
# import twitter
import random
app = Flask(__name__)

app.debug = True

# api = twitter.Api(consumer_key='consumer_key',
#                   consumer_secret='consumer_secret',
#                   access_token_key='access_token',
#                   access_token_secret='access_token_secret')

@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=random.randint(1,1000))

if __name__ == '__main__':
    app.run()
