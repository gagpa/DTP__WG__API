from app.db import Base
import sqlalchemy as sql


class WorkGroupStatus(Base):
    """Модель статуса рабочей группы"""
    __tablename__ = 'wg_statuses'

    id = sql.Column(sql.Integer, primary_key=True)

    name = sql.Column(sql.VARCHAR(), nullable=False)
