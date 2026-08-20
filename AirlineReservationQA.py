# Airline Reservation System - QA

def calculate_fare(seats, class_name, booking_date, travel_date,
                   passenger_type, baggage):

    fares = {"Economy": 5000, "Business": 10000, "First": 20000}

    if seats <= 0:
        return "Fully Booked"

    fare = fares[class_name]

    # Dynamic pricing based on seats
    if seats <= 2:
        fare *= 1.30
    elif seats <= 5:
        fare *= 1.10

    # Dynamic pricing based on booking date
    if travel_date - booking_date < 7:
        fare *= 1.20

    # Passenger discount
    if passenger_type == "Child":
        fare *= 0.75
    elif passenger_type == "Senior":
        fare *= 0.80

    # Baggage
    if baggage > 20:
        baggage_charge = (baggage - 20) * 500
    else:
        baggage_charge = 0

    return round(fare + baggage_charge, 2)


def test(name, seats, cls, book, travel, passenger, baggage):
    try:
        result = calculate_fare(
            seats, cls, book, travel, passenger, baggage
        )
        print(name, ":", result)
    except Exception as e:
        print(name, ":", e)


print("----- Airline QA -----")

# 1. Successful booking
test("Test 1 - Successful Booking",
     10, "Economy", 1, 20, "Adult", 15)

# 2. Double booking
test("Test 2 - Double Booking",
     1, "Economy", 1, 20, "Adult", 15)
test("Test 2 - Second Booking",
     0, "Economy", 1, 20, "Adult", 15)

# 3. Cancellation
fare = calculate_fare(5, "Economy", 1, 20, "Adult", 15)
print("Test 3 - Cancellation:", fare, "Booking Cancelled")

# 4. Refund
refund = fare * 0.80
print("Test 4 - Refund:", round(refund, 2))

# 5. Fully booked flight
test("Test 5 - Fully Booked",
     0, "Economy", 1, 20, "Adult", 15)

# 6. Invalid passenger
test("Test 6 - Invalid Passenger",
     5, "Economy", 1, 20, "Unknown", 15)

# 7. Excess baggage
test("Test 7 - Excess Baggage",
     5, "Economy", 1, 20, "Adult", 30)

# 8. Dynamic fare - low seats
test("Test 8 - Low Seat Fare",
     2, "Economy", 1, 20, "Adult", 15)

# 9. Dynamic fare - early booking
test("Test 9 - Early Booking",
     8, "Business", 1, 30, "Adult", 15)

# 10. Dynamic fare - last minute
test("Test 10 - Last Minute",
     8, "Business", 15, 20, "Adult", 15)

# 11. Business class
test("Test 11 - Business Class",
     5, "Business", 1, 20, "Adult", 15)

# 12. First class
test("Test 12 - First Class",
     3, "First", 1, 20, "Adult", 15)

# 13. Child passenger
test("Test 13 - Child Passenger",
     5, "Economy", 1, 20, "Child", 15)

# 14. Senior passenger
test("Test 14 - Senior Passenger",
     5, "Economy", 1, 20, "Senior", 15)
