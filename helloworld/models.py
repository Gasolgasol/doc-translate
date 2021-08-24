from datetime import datetime
import secrets

from sqlalchemy import (
    Column, Unicode, Integer, DateTime, Boolean, ForeignKey, Float
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Tester(Base):
    """Tasks for the To Do list."""
    __tablename__ = 'Tester'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)

class File(Base):
    """Tasks for the To Do list."""
    __tablename__ = 'File'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    server_name = Column(Unicode, nullable=False)
    size = Column(Unicode, nullable=False)
    original = Column(Unicode, nullable=False)
    translated = Column(Unicode, nullable=False)
    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
       
        
   