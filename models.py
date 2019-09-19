"""SQLAlchemy models for Twittoff"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
# DB.create_all()

class User(DB.Model):
    """Twitter users that we pull and analyze tweets for."""
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    # def __repr__(self):
    #     return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets"""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    # user_id = DB.Column(DB.Integer, DB.ForeignKey('User.id'), nullable=False)
    # user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    #
    # def __repr__(self):
    #     return '<Tweet {}>.format(self.text)'
