import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    
    __tablename__ = 'Follower'
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('Users.ID'))
    user_to_id = Column(Integer, ForeignKey('Users.ID'))

class User(Base):
    __tablename__ = 'Users'
    ID = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    posts = relationship("Post")
    comments = relationship("Comment")

class Media(Base):
    __tablename__ = 'Media'
    ID = Column(Integer, primary_key=True)
    type = Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.ID'))
    post = relationship("Post")

class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.ID'))
    user = relationship("User")
    comments = relationship("Comment")
    media = relationship("Media")

class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('Users.ID'))
    post_id = Column(Integer, ForeignKey('Post.ID'))
    author = relationship("User")
    post = relationship("Post")

def to_dict(self):
    return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
