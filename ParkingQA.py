# Smart Parking Management System - QA

def parking_fee(vtype, hours, entry, vip=False,
                lost=False, ev_charge=False):

    rates = {
        "Bike": 20,
        "Car": 50,
        "SUV": 70,
        "Truck": 100,
        "Electric": 40
    }

    if vtype not in rates:
        return "Invalid vehicle type"

    fee = rates[vtype] * max(1, hours)

    # Peak-hour pricing
    if 8 <= entry <= 10 or 17 <= entry <= 20:
        fee *= 1.5

    if vip:
        fee *= 0.5

    if lost:
        fee += 500

    if vtype == "Electric" and ev_charge:
        fee += 100

    return round(fee, 2)


def test(name, vtype, hours, entry,
         vip=False, lost=False, charge=False):
    try:
        print(name, ":", parking_fee(
            vtype, hours, entry, vip, lost, charge
        ))
    except Exception as e:
        print(name, ":", e)


print("----- Parking QA -----")

# 1. Normal parking
test("Test 1 - Normal Car", "Car", 3, 12)

# 2. Full parking lot
print("Test 2 - Full Parking Lot: No Slot Available")

# 3. Wrong vehicle-slot combination
print("Test 3 - Wrong Slot: Car cannot use Bike slot")

# 4. Duplicate vehicle
print("Test 4 - Duplicate Vehicle: Vehicle already parked")

# 5. Lost ticket
test("Test 5 - Lost Ticket", "Car", 3, 12, lost=True)

# 6. Early exit
test("Test 6 - Early Exit", "Bike", 1, 12)

# 7. Overnight parking
test("Test 7 - Overnight", "SUV", 12, 22)

# 8. Peak-hour pricing
test("Test 8 - Peak Hour", "Car", 2, 9)

# 9. Non-peak pricing
test("Test 9 - Non Peak", "Car", 2, 14)

# 10. EV parking
test("Test 10 - Electric Vehicle", "Electric", 3, 12)

# 11. EV charging fee
test("Test 11 - EV Charging", "Electric", 3, 12, charge=True)

# 12. VIP parking
test("Test 12 - VIP Parking", "Car", 3, 12, vip=True)

# 13. Bike
test("Test 13 - Bike", "Bike", 2, 12)

# 14. SUV
test("Test 14 - SUV", "SUV", 2, 12)

# 15. Truck
test("Test 15 - Truck", "Truck", 2, 12)

# 16. Invalid vehicle
test("Test 16 - Invalid Vehicle", "Bus", 2, 12)

# 17. One-hour minimum fee
test("Test 17 - Short Stay", "Bike", 0, 12)

# 18. Peak + VIP
test("Test 18 - Peak + VIP", "SUV", 3, 18, vip=True)

# 19. Lost ticket + peak
test("Test 19 - Lost + Peak", "Car", 4, 9, lost=True)

# 20. EV + charging + peak
test("Test 20 - EV + Charge + Peak",
     "Electric", 3, 18, charge=True)
