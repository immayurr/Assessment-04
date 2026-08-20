# Smart Parking Management System

slots = {
    "Bike": ["B1", "B2"],
    "Car": ["C1", "C2"],
    "SUV": ["S1"],
    "Truck": ["T1"],
    "Electric": ["E1"]
}

vehicle = {
    "number": "TN01AB1234",
    "type": "Car",
    "entry": 10,
    "exit": 14,
    "vip": False,
    "lost_ticket": False,
    "ev_charge": False
}

# Automatically allocate appropriate slot
available = slots.get(vehicle["type"], [])

if not available:
    print("No suitable parking slot available")
else:
    slot = available[0]
    slots[vehicle["type"]].remove(slot)

    print("Vehicle Entry Successful")
    print("Vehicle:", vehicle["number"])
    print("Type:", vehicle["type"])
    print("Allocated Slot:", slot)

    # Parking duration
    hours = vehicle["exit"] - vehicle["entry"]

    # Base hourly rates
    rates = {
        "Bike": 20,
        "Car": 50,
        "SUV": 70,
        "Truck": 100,
        "Electric": 40
    }

    fee = rates[vehicle["type"]] * max(1, hours)

    # Peak-hour pricing
    if 8 <= vehicle["entry"] <= 10 or 17 <= vehicle["entry"] <= 20:
        fee *= 1.5

    # VIP discount
    if vehicle["vip"]:
        fee *= 0.5

    # Lost ticket
    if vehicle["lost_ticket"]:
        fee += 500

    # EV charging
    if vehicle["type"] == "Electric" and vehicle["ev_charge"]:
        fee += 100

    print("Parking Hours:", hours)
    print("Parking Fee:", round(fee, 2))

    # Vehicle exit
    slots[vehicle["type"]].append(slot)
    print("Vehicle Exit Successful")
