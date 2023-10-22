from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn_string = "mysql+pymysql://homeplus:homeplus1234@3.34.220.143:59475/homeplus?autocommit=true"

class engineconn:
    def __init__(self):
        self._engine = create_engine(conn_string, pool_recycle=500)

    def sessionmaker(self):
        Sesstion = sessionmaker(bind=self._engine)
        return Sesstion()

    def connection(self):
        return self._engine.connect()
