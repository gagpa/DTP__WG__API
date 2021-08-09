from app.db import Base
import sqlalchemy as sql


class ShapeType(Base):
    """Модель типа """
    __tablename__ = 'shape_types'

    id = sql.Column(sql.SmallInteger, primary_key=True)

    name = sql.Column(sql.VARCHAR(), nullable=False)
