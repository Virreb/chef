

# def init_session():
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

with open('credentials.json', 'r') as f:
    creds = json.load(f)['database']

engine = create_engine(f'mysql+mysqldb://{creds["user"]}:{creds["password"]}@{creds["host"]}/{creds["db"]}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
#     return sessionmaker(bind=engine)

# def declare_tables():
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Area(Base):
    __tablename__ = 'areas'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(200))

    def __repr__(self):
        return f'<User(id={self.id}, title={self.title}, description={self.description})>'

# print(Areas.__table__)
# Base.metadata.create_all(engine)

test_area = Area(title='Krishantering', description='Stöd för svåra samtal angående medarbetare – samt försvar vad gäller din funktion och dig själv.')
# print(test_area.title)
# session.add(test_area)
test = session.query(Area).first()
print(test)
