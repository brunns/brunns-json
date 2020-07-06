import datetime
import json
from enum import Enum

from hamcrest import assert_that, calling, has_entries, raises

from brunns.json.encoder import ExtendedJSONEncoder
from brunns.matchers.data import json_matching


def test_encode_date_and_builtins():
    # Given
    somestring = "sausages"
    someint = 99
    somedate = datetime.date(1968, 7, 21)

    # When
    actual = json.dumps(
        {"somedate": somedate, "somestring": somestring, "someint": someint},
        cls=ExtendedJSONEncoder,
    )

    # Then
    assert_that(
        actual,
        json_matching(has_entries(somestring=somestring, someint=someint, somedate="1968-07-21")),
    )


def test_encode_datetime():
    # Given
    somedatetime = datetime.datetime(1968, 7, 21, 4, 4, 0)

    # When
    actual = json.dumps({"somedatetime": somedatetime}, cls=ExtendedJSONEncoder)

    # Then
    assert_that(actual, json_matching(has_entries(somedatetime="1968-07-21T04:04:00")))


def test_encode_binary():
    # Given
    somebin = b"dfgddzfbv"

    # When
    actual = json.dumps({"somebin": somebin}, cls=ExtendedJSONEncoder)

    # Then
    assert_that(actual, json_matching(has_entries(somebin="dfgddzfbv")))


def test_unserialisable_type():
    # Given
    someobject = ExtendedJSONEncoder()

    # Then
    assert_that(
        calling(json.dumps).with_args({"someobject": someobject}, cls=ExtendedJSONEncoder),
        raises(TypeError, ".* is not JSON serializable"),
    )


def test_enum():
    # Given
    class Colour(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    someenumvalue = Colour.GREEN

    # When
    actual = json.dumps({"someenumvalue": someenumvalue}, cls=ExtendedJSONEncoder)

    # Then
    assert_that(actual, json_matching(has_entries(someenumvalue="Colour.GREEN")))
