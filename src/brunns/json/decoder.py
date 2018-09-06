import json
import re

import pendulum


class ExtendedJSONDecoder(json.JSONDecoder):
    TYPES = [
        (r"^\d{4}-\d{2}-\d{2}$", lambda st: pendulum.parse(st, exact=True)),
        (r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$", lambda st: pendulum.parse(st, exact=True)),
    ]

    def __init__(self, *args, **kwargs):
        super(ExtendedJSONDecoder, self).__init__(*args, **kwargs)
        self.parse_string = self.custom_scan_string
        self.scan_once = json.scanner.py_make_scanner(self)

    @staticmethod
    def custom_scan_string(s, end, encoding=None, strict=True):
        s, end = json.decoder.scanstring(s, end)
        for pattern, transformer in ExtendedJSONDecoder.TYPES:
            if re.match(pattern, s):
                return transformer(s), end
        return s, end
