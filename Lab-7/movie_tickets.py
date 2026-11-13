"""Movie ticket input-processing functions for Lab 7 fuzz testing."""


def parse_seat(seat):
    """Parse a seat label such as H12 into (row, seat_number)."""
    if not isinstance(seat, str):
        raise ValueError("seat must be a string")
    seat = seat.strip()
    if len(seat) < 2 or not seat[0].isalpha() or not seat[1:].isdigit():
        raise ValueError("invalid seat format")
    row = seat[0].upper()
    number = int(seat[1:])
    if number < 1:
        raise ValueError("seat number must be positive")
    return row, number


def total_price(prices_csv):
    """Return the total ticket price including 18% GST."""
    if not isinstance(prices_csv, str):
        raise ValueError("prices must be a CSV string")
    parts = prices_csv.split(",")
    if not parts or any(not p.strip() for p in parts):
        raise ValueError("prices cannot contain empty values")
    try:
        prices = [int(p.strip()) for p in parts]
    except (TypeError, ValueError) as exc:
        raise ValueError("prices must be integers") from exc
    if any(price < 0 for price in prices):
        raise ValueError("prices cannot be negative")
    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    """Return the average of whitespace-separated integer ratings."""
    if not isinstance(ratings, str):
        raise ValueError("ratings must be a string")
    parts = ratings.split()
    if not parts:
        raise ValueError("at least one rating is required")
    try:
        values = [int(r) for r in parts]
    except ValueError as exc:
        raise ValueError("ratings must be integers") from exc
    if any(value < 1 or value > 5 for value in values):
        raise ValueError("ratings must be between 1 and 5")
    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    try:
        print("Row and Seat:", parse_seat(user_input))
    except ValueError as exc:
        print("Invalid seat:", exc)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    try:
        print("Total with GST:", total_price(user_input))
    except ValueError as exc:
        print("Invalid prices:", exc)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    try:
        print("Average Rating:", average_rating(user_input))
    except ValueError as exc:
        print("Invalid ratings:", exc)


if __name__ == "__main__":
    main()
