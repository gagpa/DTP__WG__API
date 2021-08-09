from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Integer, VARCHAR, SmallInteger, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    """ Модель пользователя """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    uuid = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid4)
    username = Column(VARCHAR(50), unique=True, nullable=False)
    fullname = Column(VARCHAR(255), nullable=False)
    birthday = Column(DateTime, nullable=False)
    offer_date = Column(DateTime, nullable=False)

    boss_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    role_id = Column(SmallInteger, ForeignKey('roles.id'), nullable=False)
    position_id = Column(SmallInteger, ForeignKey('positions.id'), nullable=False)

    boss = relationship('User', backref='staff', remote_side=id)
    department = relationship('Department', backref='users')
    role = relationship('Role', backref='users')
    position = relationship('Position', backref='users')

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.now(), nullable=True)

    def __repr__(self):
        return f'User: {self.username} {self.fullname}'


__all__ = ['User']
