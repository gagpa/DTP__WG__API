from app.db import Base
import sqlalchemy as sql
from sqlalchemy import orm
from datetime import datetime


class Shape(Base):
    """Модель профиля рабочей группы"""
    __tablename__ = 'shapes'

    id = sql.Column(sql.Integer, primary_key=True)

    name = sql.Column(sql.VARCHAR(500), nullable=False)
    color = sql.Column(sql.VARCHAR(6), nullable=False)
    width = sql.Column(sql.Integer, nullable=False)
    border_color = sql.Column(sql.VARCHAR(6), nullable=False)
    border_width = sql.Column(sql.Integer, nullable=False)
    opacity = sql.Column(sql.Float, nullable=False)
    coordinates = sql.Column(sql.JSON(), nullable=False)
    shape_type_id = sql.Column(sql.SmallInteger, sql.ForeignKey('shape_types.id'), nullable=False)
    work_group_id = sql.Column(sql.Integer, sql.ForeignKey('work_groups.id', ondelete='CASCADE'), nullable=False)

    shape_type = orm.relationship('ShapeType')
    wg = orm.relationship('WorkGroup', back_populates='shapes')

    created_at = sql.Column(sql.DateTime, default=datetime.now(), nullable=False)
    updated_at = sql.Column(sql.DateTime, onupdate=datetime.now(), nullable=True)
