# Hospital Appointment and Billing System

patient = {
    "name": "Rahul",
    "age": 65,
    "doctor": "Dr. Kumar",
    "department": "Cardiology",
    "type": "Emergency",
    "duration": 30,
    "labs": ["Blood Test", "ECG"],
    "medicines": 1200,
    "insurance": True,
    "follow_up": False
}

# Consultation fee
fee = 500

if patient["type"] == "Emergency":
    fee += 500

if patient["age"] >= 60:
    fee *= 0.8

if patient["follow_up"]:
    fee *= 0.5

# Lab charges
lab_prices = {
    "Blood Test": 300,
    "ECG": 500,
    "X-Ray": 700
}

lab_charge = sum(lab_prices.get(x, 0) for x in patient["labs"])

# Total bill
total = fee + lab_charge + patient["medicines"]

# Insurance coverage
insurance = total * 0.70 if patient["insurance"] else 0
payable = total - insurance

print("----- Hospital Management -----")
print("Patient:", patient["name"])
print("Doctor:", patient["doctor"])
print("Department:", patient["department"])
print("Appointment:", patient["type"])
print("Consultation Fee:", round(fee, 2))
print("Lab Charges:", lab_charge)
print("Medicine Charges:", patient["medicines"])
print("Insurance Coverage:", round(insurance, 2))
print("Patient Payable:", round(payable, 2))
