from app.db import Base
import sqlalchemy as sql


class Responsible(Base):
    """Модель типа """
    __tablename__ = 'responsible'

    id = sql.Column(sql.SmallInteger, primary_key=True)

    name = sql.Column(sql.VARCHAR(), nullable=False)
