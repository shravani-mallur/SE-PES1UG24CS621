"""Demonstration fuzz tests against the unmodified buggy starter module."""
import pytest
from hypothesis import given, strategies as st

from movie_tickets_buggy import parse_seat, total_price, average_rating


@given(st.one_of(st.text(), st.none(), st.integers(), st.floats(allow_nan=True, allow_infinity=True)))
def test_parse_seat_rejects_or_parses_without_unexpected_crash(value):
    try:
        result = parse_seat(value)
        assert isinstance(value, str)
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], str) and len(result[0]) == 1
        assert isinstance(result[1], int) and result[1] >= 1
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_total_price_rejects_or_returns_valid_total(value):
    try:
        result = total_price(value)
        assert isinstance(value, str)
        assert isinstance(result, float)
        assert result >= 0
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_average_rating_rejects_or_returns_valid_average(value):
    try:
        result = average_rating(value)
        assert isinstance(value, str)
        assert 1 <= result <= 5
    except ValueError:
        pass


@pytest.mark.parametrize("bad_seat", [None, "", "A0", "A-1", "12A", "AB12", "A1.5"])
def test_invalid_seats(bad_seat):
    with pytest.raises(ValueError):
        parse_seat(bad_seat)


@pytest.mark.parametrize("bad_prices", [None, "", "1,,2", "one,2", "-1,2", "1,"])
def test_invalid_prices(bad_prices):
    with pytest.raises(ValueError):
        total_price(bad_prices)


@pytest.mark.parametrize("bad_ratings", [None, "", "1 x 3", "0 3", "6 2"])
def test_invalid_ratings(bad_ratings):
    with pytest.raises(ValueError):
        average_rating(bad_ratings)
