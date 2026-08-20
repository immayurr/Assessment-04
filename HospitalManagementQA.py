# Hospital Management - QA

def calculate(age, appointment, labs, medicine, insurance, follow_up):

    fee = 500

    if appointment == "Emergency":
        fee += 500

    if age >= 60:
        fee *= 0.8

    if follow_up:
        fee *= 0.5

    lab_prices = {"Blood": 300, "ECG": 500, "XRay": 700}
    lab = sum(lab_prices.get(x, 0) for x in labs)

    total = fee + lab + medicine
    coverage = total * 0.70 if insurance else 0
    payable = total - coverage

    return round(total, 2), round(coverage, 2), round(payable, 2)


def test(name, age, appointment, labs, medicine, insurance, follow_up):
    try:
        total, coverage, payable = calculate(
            age, appointment, labs, medicine, insurance, follow_up
        )
        print(name)
        print("Total:", total, "Insurance:", coverage,
              "Payable:", payable)
        print()
    except Exception as e:
        print(name, "Error:", e)


print("----- Hospital QA -----")

# 1. Normal patient
test("Test 1 - Normal Patient",
     30, "Normal", ["Blood"], 500, False, False)

# 2. Emergency patient
test("Test 2 - Emergency",
     30, "Emergency", ["Blood", "ECG"], 1000, False, False)

# 3. Senior citizen
test("Test 3 - Senior Citizen",
     65, "Normal", ["Blood"], 500, False, False)

# 4. Insurance patient
test("Test 4 - Insurance",
     40, "Normal", ["ECG"], 1000, True, False)

# 5. Follow-up consultation
test("Test 5 - Follow-up",
     40, "Normal", ["Blood"], 500, False, True)

# 6. Senior + Insurance
test("Test 6 - Senior + Insurance",
     65, "Normal", ["Blood", "ECG"], 1000, True, False)

# 7. Emergency + Insurance
test("Test 7 - Emergency + Insurance",
     45, "Emergency", ["ECG"], 1500, True, False)

# 8. Emergency + Senior
test("Test 8 - Emergency + Senior",
     70, "Emergency", ["Blood"], 800, False, False)

# 9. Follow-up + Insurance
test("Test 9 - Follow-up + Insurance",
     35, "Normal", ["XRay"], 600, True, True)

# 10. No lab tests
test("Test 10 - No Lab Tests",
     25, "Normal", [], 300, False, False)
