from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


# Test 1: Fuzz testing parse_seat()
@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    try:
        parse_seat(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"parse_seat crashed with: {e}"


# Test 2: Fuzz testing total_price()
@given(st.text() | st.none())
def test_total_price_no_crash(s):
    try:
        total_price(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"total_price crashed with: {e}"


# Test 3: Fuzz testing average_rating()
@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    try:
        average_rating(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"average_rating crashed with: {e}"