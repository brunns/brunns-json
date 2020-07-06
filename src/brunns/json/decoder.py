import json
import re

from dateutil import parser


class ExtendedJSONDecoder(json.JSONDecoder):
    TYPES = [
        (r"^\d{4}-\d{2}-\d{2}$", lambda st: parser.parse(st).date()),
        (r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$", parser.parse),
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
                try:
                    return transformer(s), end
                except Exception:  # nosec
                    pass  # Try something else
        return s, end
