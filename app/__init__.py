from flask import Flask
import logging

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
logging.basicConfig(filename='example.log', level=logging.DEBUG)
from app import views, groups, fields, database, creator, parse, scenarios

# helpful logging script edited slightly from what is found on Miguel Grinberg's fantastic flask tutorial
# at http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
