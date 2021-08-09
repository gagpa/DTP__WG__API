from sqlalchemy import Column, VARCHAR, SmallInteger

from app.db import Base


class Role(Base):
    """ Модель ролей """
    __tablename__ = 'roles'
    id = Column(SmallInteger, primary_key=True)

    name = Column(VARCHAR(25), nullable=False, unique=True)

    def __repr__(self):
        return f'Role {self.name}'


__all__ = ['Role']
