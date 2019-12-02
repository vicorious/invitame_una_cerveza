"""
Encoder module
"""
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):
    """
    AlchemyJsonEncoder
    """
    def default(self, obj):
        """
        Default method
        """
        fields = {}
        if isinstance(obj.__class__, DeclarativeMeta):            
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        return fields
