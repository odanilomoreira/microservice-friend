from sql_alchemy import db
from flask import Flask

class FriendModel(db.Model):
    __tablename__ = 'friends'

    id = db.Column(db.Integer, primary_key=True)
    friend_name = db.Column(db.String(80))
    entity_id = db.Column(db.Integer)

    def __init__(self, id, friend_name, entity_id):
        self.id = id
        self.friend_name = friend_name
        self.entity_id = entity_id

    def json(self):
        return {
            'id': self.id,
            'friend_name': self.friend_name,
            'entity_id': self.entity_id
        }

    @classmethod
    def find_by_entity_id(cls, id):
        friends = cls.query.filter_by(entity_id=id)
        if friends:
            return friends
        return None

    @classmethod
    def find_by_id(cls, id):
        friend = cls.query.filter_by(id=id)
        if friend:
            return friend
        return None
    
    @classmethod
    def find(cls, friend_name):
        friend = cls.query.filter_by(friend_name=friend_name).first()
        if friend:
            return friend
        return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
