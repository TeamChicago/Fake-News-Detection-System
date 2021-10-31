from datetime import datetime
from flask import Flask, render_template, flash, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse
from flask_cors import CORS

from config import db, app
from predict import Predictor

predictors = Predictor()
CORS(app, resources={r'*': {'origins': '*'}})

count = 0


class News(db.Model):
    id = db.Column('news_id', db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.TEXT)
    writer = db.Column(db.String(255))
    writtentime = db.Column(db.DateTime, default=datetime.utcnow())
    reliability = db.Column(db.Integer)

    def __init__(self, counts, title, content, writer, reliability):
        self.id = counts
        self.title = title
        self.content = content
        self.writer = writer
        self.reliability = reliability

    def __repr__(self):
        return f"<News {self.text}>"


@app.route('/test', methods=['POST'])
def post_test():
    test = request.get_json()

    return jsonify(test)


@app.route('/connect')
def hello():
    news = News(
        "test title",
        "test content",
        "test writer",
        82,
    )
    db.session.add(news)
    db.session.commit()
    return 'Hello World'


@app.route('/api/newspost', methods=['POST'])
def news_post():
    global count
    count += 1
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('content', type=str)
        parser.add_argument('writer', type=str)
        args = parser.parse_args()

        _title = args['title']
        _content = args['content']
        _writer = args['writer']
        print(_content)
        _reliability = int(predictors.predictor(_content))

        news = News(
            count,
            _title,
            _content,
            _writer,
            _reliability
        )
        db.session.add(news)
        db.session.commit()
        return "success"
    except Exception as e:
        return {'error': str(e)}


@app.route('/model')
def predict_fake():
    test = "Democrats in the Texas Legislature staged a dramatic, late-night walkout on Sunday night to force the failure of a sweeping Republican overhaul of state election laws. The move, which deprived the session of the minimum number of lawmakers required for a vote before a midnight deadline, was a stunning setback for state Republicans who had made a new voting law one of their top priorities. The effort is not entirely dead, however. Gov. Greg Abbott, a Republican, indicated that he would call a special session of the Legislature, which could start as early as June 1, or Tuesday, to restart the process. The governor has said that he strongly supported an election bill, and in a statement he called the failure to reach one on Sunday “deeply disappointing.” He was widely expected to sign whatever measure Republicans passed. Election Integrity & Bail Reform were emergency items for this legislative session,” Mr. Abbott said on Twitter on Sunday night. “They will be added to the special session agenda.” He did not specify when the session would start. While Republicans would still be favored to pass a bill in a special session, the unexpected turn of events on Sunday presents a new hurdle in their push to enact a far-reaching election law that would install some of the most rigid voting restrictions in the country, and cement the state as one of the hardest in which to cast a ballot."
    ret = str(predictors.predictor(test))

    return ret


if __name__ == '__main__':
    db.create_all()
    app.run(Debug=True, host='0.0.0.0')
