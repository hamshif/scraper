import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class OpenGraphNode(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), unique=True, nullable=True)
    type = db.Column(db.String(120), unique=False, nullable=True)
    title = db.Column(db.String(200), unique=False, nullable=True)
    update_time = db.Column(db.DateTime, unique=False, default=datetime.datetime.utcnow)

    def __init__(self, url, type=None, title=None):
        self.url = url
        self.type = type
        self.title = title

    def as_dict(self):

        return {
            "url": self.url,
            "type": self.type,
            "title": self.title,
            "image": {
                "url": "http://ogp.me/logo.png",
                "type": "image/png",
                "width": 300,
                "height": 300,
                "alt": "The Open Graph logo"
            },
            "scrape_status" : "done",
            "updated_time": "2018-02-18T03:41:09+0000",
            "id": self.id
        }


