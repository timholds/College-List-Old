#from app import db
from sqlalchemy import Column, Integer, String
from database import Base, init_db, User

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), index=True, unique=True)
    college = Column(String(140), index=True, unique=False)

    def __init__(self, email=None, college=None):
        self.email = email
        self.college = college

    def __repr__(self):
        return '<User %r>' % (self.email)

u = User('admin', 'admin@localhost')
db_session.add(u)
db_session.commit()
User.query.all()

"""
class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CollegeName = db.Column(db.String(150), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)

class Votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fun = db.Column(db.Integer, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)
"""