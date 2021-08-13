from app.db import Base
import sqlalchemy as sql
from sqlalchemy import orm
from datetime import datetime


class WorkGroup(Base):
    """Модель рабочей группы"""
    __tablename__ = 'work_groups'

    id = sql.Column(sql.Integer, primary_key=True)

    description = sql.Column(sql.VARCHAR(1000), nullable=False)
    protocol = sql.Column(sql.DateTime, nullable=False)
    start_realization = sql.Column(sql.DateTime, nullable=False)
    end_realization = sql.Column(sql.DateTime, nullable=False)

    type_id = sql.Column(sql.SmallInteger, sql.ForeignKey('wg_types.id'), nullable=False)
    status_id = sql.Column(sql.SmallInteger, sql.ForeignKey('wg_statuses.id'), nullable=False)
    responsible_id = sql.Column(sql.Integer, sql.ForeignKey('responsible.id'), nullable=False)

    type = orm.relationship('WorkGroupType', backref='work_groups')
    status = orm.relationship('WorkGroupStatus', backref='work_groups')
    responsible = orm.relationship('Responsible', backref='work_groups')
    shapes = orm.relationship('Shape', back_populates='wg', cascade="all, delete", passive_deletes=True)

    created_at = sql.Column(sql.DateTime, default=datetime.now(), nullable=False)
    updated_at = sql.Column(sql.DateTime, onupdate=datetime.now(), nullable=True)
