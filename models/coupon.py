from datetime import datetime

from sqlalchemy import Column, TEXT, INT, BIGINT, VARCHAR, CHAR, DATE, DATETIME
from sqlalchemy.orm import declarative_base

# +-------+--------------+------+-----+---------+----------------+
# | Field | Type         | Null | Key | Default | Extra          |
# +-------+--------------+------+-----+---------+----------------+
# | id    | int(11)      | NO   | PRI | NULL    | auto_increment |
# | no    | varchar(100) | NO   |     | NULL    |                |
# | use   | char(1)      | NO   |     | N       |                |
# | month | char(6)      | NO   |     | NULL    |                |
# | exp   | date         | NO   |     | NULL    |                |
# | img   | varchar(100) | NO   |     | NULL    |                |
# | reg   | datetime     | NO   |     | NULL    |                |
# +-------+--------------+------+-----+---------+----------------+

Base = declarative_base()


class Coupon(Base):
    __tablename__ = "coupon"
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    no = Column(VARCHAR, nullable=False)
    use = Column(CHAR, nullable=False)
    month = Column(CHAR, nullable=False)
    exp = Column(DATE, nullable=False)
    img = Column(VARCHAR, nullable=False)
    reg = Column(DATETIME, nullable=False, default=datetime.now)
