from eve.io.base import BaseJSONEncoder
from datetime import timedelta


class SQLAJSONEncoder(BaseJSONEncoder):
    def default(self, obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return super(SQLAJSONEncoder, self).default(obj)
