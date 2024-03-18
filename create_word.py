import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Word



def create_db(engine):
    words = (
        ('hello', 'привет'),
        ('goodbye', 'до свидания'),
        ('yes', 'да'),
        ('no', 'нет'),
        ('ok', 'хорошо'),
        ('Sun', 'солнце'),
        ('Moon', 'луна'),
        ('Star', 'звезда'),
        ('Tree', 'дерево'),
        ('House', 'дом'),
        ('Car', 'машина'),
        ('Book', 'книга'),
        ('Phone', 'телефон'),
        ('Computer', 'компьютер'),
        ('Keyboard', 'клавиатура'),
        ('Mouse', 'мышь'),
        ('Green', 'зеленый'),
        ('White', 'белый'),
        ('Red', 'красный'),
        ('Yellow', 'желтый'),
        ('Blue', 'синий')
    )
    
    create_tables(engine)
    for i in words:
        
        session.add(Word(word=i[0], translate=i[1]))
        
    session.commit()


    

DNS = 'postgresql://postgres:25022004HERSOSI1725@localhost:5432/tgbot'
engine = sqlalchemy.create_engine(DNS)
Session = sessionmaker(bind=engine)
session = Session()
create_db(engine)

session.close()

