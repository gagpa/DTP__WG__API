from sqlalchemy import Column, VARCHAR, SmallInteger

from app.db import Base


class Department(Base):
    """ Модель отдела """
    __tablename__ = 'departments'
    id = Column(SmallInteger, primary_key=True)

    name = Column(VARCHAR(255), nullable=False, unique=True)

    def __repr__(self):
        return f'Department {self.name}'


__all__ = ['Department']
