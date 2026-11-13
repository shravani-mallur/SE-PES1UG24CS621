def parse_seat(seat):
    if not isinstance(seat, str):
        raise ValueError("Seat must be a string")

    seat = seat.strip()

    if len(seat) < 2:
        raise ValueError("Invalid seat format")

    row = seat[0]
    number = seat[1:]

    if not row.isalpha() or not number.isdigit():
        raise ValueError("Invalid seat format")

    seat_number = int(number)

    if seat_number < 1:
        raise ValueError("Seat number must be positive")

    return row.upper(), seat_number

def total_price(prices_csv):
    if not isinstance(prices_csv, str):
        raise ValueError("Prices must be provided as a string")

    parts = prices_csv.split(',')

    if any(not p.strip() for p in parts):
        raise ValueError("Price list cannot contain empty values")

    try:
        prices = [int(p.strip()) for p in parts]
    except ValueError:
        raise ValueError("Prices must contain valid integers")

    if any(p < 0 for p in prices):
        raise ValueError("Prices cannot be negative")

    return round(sum(prices) * 1.18, 2)
def average_rating(ratings):
    if not isinstance(ratings, str):
        raise ValueError("Ratings must be provided as a string")

    values = ratings.split()

    if not values:
        raise ValueError("At least one rating is required")

    try:
        values = [int(r) for r in values]
    except ValueError:
        raise ValueError("Ratings must contain valid integers")

    return round(sum(values) / len(values), 1)

def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)

if __name__ == "__main__":
    main()
