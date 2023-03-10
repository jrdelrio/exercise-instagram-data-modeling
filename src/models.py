import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=True)
    post = relationship('post')
    comment = relationship('comment.author_id')
    follower_to = relationship('follower.user_to_id')
    follower_from = relationship('follower.user_from_id')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String)
    post_id = Column(ForeignKey('post.id'))
    post = relationship('post')

class Comment (Base):
    __tablename__ = 'comment'
    comment_text = Column(String)
    author_id = Column(ForeignKey('person.id'))
    post_id = Column(ForeignKey('post.id'))

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(ForeignKey('person.id'))
    user_to_id = Column(ForeignKey('person.id'))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
