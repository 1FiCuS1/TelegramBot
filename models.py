import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = sq.Column(sq.Integer, primary_key=True)
    cid = sq.Column(sq.BigInteger, nullable=False)

    def __str__(self):
        return self.name
    
class UserWord(Base):
    __tablename__ = "user_word"
    id = sq.Column(sq.Integer, primary_key=True)
    word = sq.Column(sq.String(length=50), unique=True)
    translate = sq.Column(sq.String(length=50), nullable=False)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="user_words")

    def __str__(self):
        return self.word
    
class Word(Base):
    __tablename__ = "word"
    id = sq.Column(sq.Integer, primary_key=True)
    word = sq.Column(sq.String(length=50), unique=True)
    translate = sq.Column(sq.String(length=50), nullable=False)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="words")
   
    def __str__(self):
        return self.word

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
