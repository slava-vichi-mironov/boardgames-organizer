from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import db
from sqlalchemy.orm.collections import attribute_mapped_collection


class BoardGameModel(db.Model):
    __tablename__ = 'boardgames'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    key_words = db.Column(db.String(500))
    game_type = db.Column(db.String(80))
    author = db.Column(db.String(80))

    def __init__(self, name, key_words, game_type, author):
        self.name = name
        self.key_words = key_words
        self.game_type = game_type
        self.author = author

    def json(self):
        return {'name': self.name, 'game_type': self.game_type, 'author': self.author,
                'keywords': self.key_words.split('#')}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


