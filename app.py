import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.debug = True

if not os.environ.get('trail_testing'):
    app.config['MONGODB_SETTINGS'] = {'DB': "trail"}
    # signed cookie secret
    app.config["SECRET_KEY"] = "KeepThisS3cR3t"
else:
    app.config["SECRET_KEY"] = "TestSecret"
    app.config["MONGODB_SETTINGS"] = {'DB': "test_trail"}
    app.config['TESTING'] = True

db = MongoEngine(app)
import login

import handlers.auth_handlers
import handlers.home_handlers
