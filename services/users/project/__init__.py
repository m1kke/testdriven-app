# services/users/project/__init__.py

import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# init app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTIGNS')
app.config.from_object(app_settings)

#import sys
#print(app.config, file=sys.stderr)

# init db
db = SQLAlchemy(app)

# model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(128), nullable = False)
    active = db.Column(db.Boolean(), default = True, nullable = False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


# routes
@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        "status": "success",
        "message": "pong!"
    })
