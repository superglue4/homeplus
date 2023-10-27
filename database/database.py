from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class engineconn:
    def __init__(self, db_str):
        self._engine = create_engine(db_str, pool_recycle=500)

    def sessionmaker(self):
        Sesstion = sessionmaker(bind=self._engine)
        return Sesstion()

    def connection(self):
        return self._engine.connect()
