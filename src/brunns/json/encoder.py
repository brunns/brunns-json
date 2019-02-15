import datetime
import json
from enum import Enum

from brunns.util.method_dispatch import methoddispatch


class ExtendedJSONEncoder(json.JSONEncoder):
    @methoddispatch
    def default(self, o):
        return super(ExtendedJSONEncoder, self).default(o)

    @default.register(datetime.date)
    def default_date(self, date):
        return date.isoformat()

    @default.register(datetime.datetime)
    def default_datetime(self, datetime):
        return datetime.isoformat()

    @default.register(Enum)
    def default_enum(self, enum):
        return str(enum)

    @default.register(bytes)
    def default_binary(self, binary):
        return binary.decode("utf-8")
