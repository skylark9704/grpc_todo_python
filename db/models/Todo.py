from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP, SMALLINT
from db.db import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Todo(Base):

    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(256), nullable=False)
    description = Column(VARCHAR(256), nullable=True)
    status = Column(SMALLINT, default=0, nullable=True)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated = Column(
        TIMESTAMP, server_default=func.now(),
        onupdate=func.now(), nullable=False
    )

    def __repr__(self):
        return (
            "<Todo(id='{}', title='{}',description='{}')>".format(
                self.id, self.title, self.description
            )
        )
