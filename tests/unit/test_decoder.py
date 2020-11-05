import json
from datetime import date, datetime

from hamcrest import assert_that, has_entries

from brunns.json.decoder import ExtendedJSONDecoder


def test_decode_date():
    # Given
    given = """{"somedate": "1968-07-21", "foo": 99, "bar": "sausages"}"""

    # When
    actual = json.loads(given, cls=ExtendedJSONDecoder)

    # Then
    assert_that(actual, has_entries(somedate=date(1968, 7, 21), foo=99, bar="sausages"))


def test_decode_not_a_date():
    # Given
    given = """{"not_a_date": "1111-22-33"}"""

    # When
    actual = json.loads(given, cls=ExtendedJSONDecoder)

    # Then
    assert_that(actual, has_entries(not_a_date="1111-22-33"))


def test_decode_datetime():
    # Given
    given = """{"somedate": "1968-07-21T04:04:00", "foo": 99, "bar": "sausages"}"""

    # When
    actual = json.loads(given, cls=ExtendedJSONDecoder)

    # Then
    assert_that(
        actual,
        has_entries(somedate=datetime(1968, 7, 21, 4, 4, 0), foo=99, bar="sausages"),
    )
