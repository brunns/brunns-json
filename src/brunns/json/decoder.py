import json
import re

import pendulum


class ExtendedJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(ExtendedJSONDecoder, self).__init__(*args, **kwargs)
        self.parse_string = self.custom_scan_string
        self.scan_once = json.scanner.py_make_scanner(self)

    @staticmethod
    def custom_scan_string(s, end, encoding=None, strict=True):
        s, end = json.decoder.scanstring(s, end)
        if re.match(r"\d{4}-\d{2}-\d{2}", s):
            return pendulum.parse(s, exact=True), end
        return s, end
