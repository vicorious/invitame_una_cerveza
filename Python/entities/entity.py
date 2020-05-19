"""
Entity class
"""
from datetime import datetime
from sqlalchemy import  Column, String, Integer, DateTime
from typing import Any, List
class Entity():
    """
    Abstract class FOR ENTITY
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    def __init__(self, created_by):
        """
        Constructor
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.created_at, self.updated_at, self.last_updated_by))

    @staticmethod
    def serialize_many(items: List[Any] = None, is_me: bool = False):
        return [] if items is None else list(
            map(lambda item: item.serialize(is_me), items))
