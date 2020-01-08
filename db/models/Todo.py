from sqlalchemy import Column, Integer, String, DateTime, SMALLINT, Boolean
from db.db import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Todo(Base):

    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created = Column(DateTime(timezone=True),
                     server_default=func.now(), nullable=True)
    status = Column(SMALLINT, default=0, nullable=False)

    def __repr__(self):
        return (
            "<Todo(id='%s', title='%s',description='%s')>" % (
                self.id, self.title, self.description,
            )
        )
