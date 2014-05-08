import os
import json
import time

from bottle import get, post, redirect, request, run

FOLDER = 'bottle_guests'


def generate_homepage():
    l = []
    for filename in sorted(os.listdir(FOLDER), key=lambda x: float(x[:-4])):
        with open(os.path.join(FOLDER, filename)) as f:
            review = f.read()
        l.append(render_review(json.loads(review)))
    return '<h1>Guests reviews</h1>' + '{}\n'.format('=' * 20).join(l) + \
           '<br ><a href="/add">Send us your feedback</a>'


def render_review(review):
    return '''<h3>Review by {}</h3>
              <p>{}</p>'''.format(review['name'].title(), review['review'])


@get('/')
def index():
    return generate_homepage()


@get('/add')
def form():
    return '''<h1>Guests reviews are always welcom</h1>
              <form method="POST">
                <label>Your name</label><br >
                <input type="text" name="name"><br >
                <label>Your email</label><br >
                <input type="email" name="email"><br >
                <label>Review</label><br >
                <textarea cols="40" rows="10" name="review"></textarea><br >
                <input type="submit">
              </form>'''


@post('/add')
def add():
    d = {
        'name': request.forms.get('name'),
        'email': request.forms.get('email'),
        'review': request.forms.get('review'),
    }
    save_review(d)
    redirect('/thanks')

def save_review(review):
    now = time.time()
    path = os.path.join(FOLDER, '{}.txt'.format(now))
    with open(path, 'w') as f:
        f.write(json.dumps(review))


@get('/thanks')
def thanks():
    return '<h1>Thanks!</h1><a href="/">Back to homepage</a>'

run(host='localhost', port=8080)
