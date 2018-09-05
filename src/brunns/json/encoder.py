import datetime
import json

from brunns.util.method_dispatch import methoddispatch


class ExtendedEncoder(json.JSONEncoder):
    @methoddispatch
    def default(self, o):
        return super(ExtendedEncoder, self).default(o)

    @default.register(datetime.date)
    def default_date(self, date):
        return date.isoformat()

    @default.register(datetime.datetime)
    def default_datetime(self, datetime):
        return datetime.isoformat()
