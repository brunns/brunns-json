import datetime
import json

from brunns.matchers.data import json_matching
from hamcrest import assert_that, has_entries, calling, raises

from brunns.json.encoder import ExtendedEncoder


def test_encode_string():
    # Given
    somestring = "sausages"

    # When
    actual = json.dumps({"somestring": somestring}, cls=ExtendedEncoder)

    # Then
    assert_that(actual, json_matching(has_entries(somestring=somestring)))


def test_encode_int():
    # Given
    someint = 99

    # When
    actual = json.dumps({"someint": someint}, cls=ExtendedEncoder)

    # Then
    assert_that(actual, json_matching(has_entries(someint=99)))


def test_encode_date():
    # Given
    somedate = datetime.date(1968, 7, 21)

    # When
    actual = json.dumps({"somedate": somedate}, cls=ExtendedEncoder)

    # Then
    assert_that(actual, json_matching(has_entries(somedate="1968-07-21")))


def test_encode_datetime():
    # Given
    somedatetime = datetime.datetime(1968, 7, 21, 4, 4, 0)

    # When
    actual = json.dumps({"somedatetime": somedatetime}, cls=ExtendedEncoder)

    # Then
    assert_that(actual, json_matching(has_entries(somedatetime="1968-07-21T04:04:00")))


def test_unserialisable_type():
    # Given
    someobject = ExtendedEncoder()

    # Then
    assert_that(
        calling(json.dumps).with_args({"someobject": someobject}, cls=ExtendedEncoder),
        raises(TypeError, ".* is not JSON serializable"),
    )
