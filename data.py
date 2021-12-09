import datetime

from sqlalchemy import create_engine, Integer, String, Column, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import os

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'statistic.db'))
session = Session(bind=engine)
Base = declarative_base()


class UserResults(Base):
    __tablename__ = 'session_result'
    id = Column(Integer(), primary_key=True)
    date = Column(Date())
    CPM = Column(Integer())
    WPM = Column(Integer())
    Errors = Column(Integer())
    Count = Column(Integer())


Base.metadata.create_all(engine)


def save_results(date, new_wpm, new_cpm, new_errors):
    result = session.query(UserResults).filter(UserResults.date == date).first()
    if result:
        result.CPM += new_cpm
        result.WPM += new_wpm
        result.Errors += new_errors
        result.Count += 1
        session.commit()
    else:
        to_save = UserResults(
            date=date,
            CPM=new_cpm,
            WPM=new_wpm,
            Errors=new_errors,
            Count=1
        )
        session.add(to_save)
        session.commit()

    take_results()


def take_results():
    results = []
    query = session.query(UserResults)
    for result in query:
        new_result = [result.date, result.WPM // result.Count, result.CPM // result.Count, result.Errors]
        results.append(new_result)

    return results
