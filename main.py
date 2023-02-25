import web

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = 'mysql+pymysql://user:my-cool-secret@db/test'
engine = create_engine(DB_URI)
session = sessionmaker(bind=engine)
Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'

    test_id = Column(Integer, primary_key=True)
    test = Column(String)


urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        s = session()
        records = s.query(Test).all()
        return "\n".join([record.test for record in records])


if __name__ == "__main__":
    app.run()
