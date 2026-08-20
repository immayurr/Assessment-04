# Airline Reservation System

flight = {
    "number": "AI101",
    "from": "Chennai",
    "to": "Delhi",
    "seats": {"Economy": 5, "Business": 2, "First": 1},
    "base_fare": {"Economy": 5000, "Business": 10000, "First": 20000}
}

passenger = {
    "name": "Rahul",
    "type": "Adult",
    "class": "Economy",
    "baggage": 25,
    "booking_date": 10,
    "travel_date": 25
}

# Flight search
print("Flight:", flight["number"])
print(flight["from"], "to", flight["to"])

# Seat availability
available = flight["seats"][passenger["class"]]
print("Available Seats:", available)

if available <= 0:
    print("Flight Fully Booked")
else:
    # Dynamic pricing
    fare = flight["base_fare"][passenger["class"]]

    if available <= 2:
        fare *= 1.30
    elif available <= 5:
        fare *= 1.10

    # Earlier booking gets lower fare
    if passenger["travel_date"] - passenger["booking_date"] < 7:
        fare *= 1.20

    # Passenger type
    if passenger["type"] == "Child":
        fare *= 0.75
    elif passenger["type"] == "Senior":
        fare *= 0.80

    # Baggage charge
    free_baggage = 20
    baggage_charge = max(0, passenger["baggage"] - free_baggage) * 500

    total = fare + baggage_charge

    # Booking
    flight["seats"][passenger["class"]] -= 1

    print("Booking Successful")
    print("Passenger:", passenger["name"])
    print("Class:", passenger["class"])
    print("Fare:", round(fare, 2))
    print("Baggage Charge:", baggage_charge)
    print("Total Fare:", round(total, 2))

    # Cancellation and refund
    cancelled = True

    if cancelled:
        refund = total * 0.80
        print("Booking Cancelled")
        print("Refund:", round(refund, 2))
