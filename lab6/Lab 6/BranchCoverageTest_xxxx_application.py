
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ==========================================
# TICKET PRICE - BRANCH COVERAGE
# ==========================================

def test_invalid_seat():
    with pytest.raises(ValueError):
        ticket_price("luxury", 25, 15, False)


def test_valid_seat():
    assert ticket_price("regular", 25, 15, False) == 150


def test_negative_show_hour():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)


def test_show_hour_above_23():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


def test_morning_show():
    assert ticket_price("regular", 25, 10, False) == 100


def test_afternoon_show():
    assert ticket_price("regular", 25, 15, False) == 150


def test_evening_show():
    assert ticket_price("regular", 25, 19, False) == 180


def test_weekday():
    assert ticket_price("regular", 25, 15, False) == 150


def test_weekend():
    assert ticket_price("regular", 25, 15, True) == 190


def test_age_below_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_age_three_to_twelve():
    assert ticket_price("regular", 10, 15, False) == 75


def test_adult_age():
    assert ticket_price("regular", 25, 15, False) == 150


def test_senior_citizen():
    assert ticket_price("regular", 60, 15, False) == 75


# ==========================================
# GROUP DISCOUNT - BRANCH COVERAGE
# ==========================================

def test_zero_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_negative_tickets():
    with pytest.raises(ValueError):
        group_discount(-2, False)


def test_less_than_five_tickets():
    assert group_discount(2, False) == 0


def test_exactly_five_tickets():
    assert group_discount(5, False) == 10


def test_ten_or_more_tickets():
    assert group_discount(10, False) == 15


def test_student_group_without_discount():
    assert group_discount(2, True) == 0


def test_student_group_with_discount():
    assert group_discount(5, True) == 15


def test_student_group_large():
    assert group_discount(10, True) == 20


# ==========================================
# SNACK COMBO - BRANCH COVERAGE
# ==========================================

def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack():
    assert snack_combo("medium", False) == 180


def test_large_snack():
    assert snack_combo("large", False) == 250


def test_small_snack_with_coupon():
    assert snack_combo("small", True) == 70


def test_medium_snack_with_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack_with_coupon():
    assert snack_combo("large", True) == 200

