# flake8: noqa
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP, SMALLINT
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Todo(Base):

    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    description = Column(VARCHAR(256))
    status = Column(SMALLINT, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(
        TIMESTAMP, server_default=func.now(),
        onupdate=func.now(), nullable=False
    )

    def __repr__(self):
        return (
            "<Todo(id='{}', title='{}')>".format(
                self.id, self.title
            )
        )
