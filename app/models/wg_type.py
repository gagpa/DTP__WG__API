from app.db import Base
import sqlalchemy as sql


class WorkGroupType(Base):
    """Модель типа рабочей группы"""
    __tablename__ = 'wg_types'

    id = sql.Column(sql.Integer, primary_key=True)

    name = sql.Column(sql.VARCHAR(), nullable=False)
