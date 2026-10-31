import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------------- TICKET PRICE TESTS ----------------

def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


def test_premium_ticket():
    assert ticket_price("premium", 25, 15, False) == 250


def test_recliner_ticket():
    assert ticket_price("recliner", 25, 15, False) == 400


def test_morning_discount():
    assert ticket_price("regular", 25, 10, False) == 100


def test_evening_charge():
    assert ticket_price("regular", 25, 19, False) == 180


def test_weekend_charge():
    assert ticket_price("regular", 25, 15, True) == 190


def test_weekend_morning():
    assert ticket_price("regular", 25, 10, True) == 140


def test_weekend_evening():
    assert ticket_price("premium", 25, 19, True) == 320


def test_child_below_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_ticket():
    assert ticket_price("regular", 10, 15, False) == 75


def test_senior_citizen():
    assert ticket_price("premium", 65, 15, False) == 125


def test_adult_ticket():
    assert ticket_price("regular", 30, 15, False) == 150


def test_invalid_seat():
    with pytest.raises(ValueError):
        ticket_price("luxury", 25, 15, False)


def test_invalid_negative_time():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)


def test_invalid_time_above_23():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


# ---------------- GROUP DISCOUNT TESTS ----------------

def test_small_group():
    assert group_discount(2, False) == 0


def test_medium_group():
    assert group_discount(7, False) == 10


def test_large_group():
    assert group_discount(12, False) == 15


def test_student_medium_group():
    assert group_discount(7, True) == 15


def test_student_large_group():
    assert group_discount(12, True) == 20


def test_student_small_group():
    assert group_discount(2, True) == 0


def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_negative_tickets():
    with pytest.raises(ValueError):
        group_discount(-2, False)


# ---------------- SNACK COMBO TESTS ----------------

def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack():
    assert snack_combo("medium", False) == 180


def test_large_snack():
    assert snack_combo("large", False) == 250


def test_small_snack_coupon():
    assert snack_combo("small", True) == 70


def test_medium_snack_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack_coupon():
    assert snack_combo("large", True) == 200