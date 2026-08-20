# Banking Loan Approval System - QA

def process_loan(age, salary, existing_loan, credit_score,
                 employment, requested_loan, tenure):

    if age < 18 or age > 60:
        raise ValueError("Invalid age")

    if salary <= 0:
        raise ValueError("Invalid salary")

    if credit_score < 650:
        return "Rejected: Poor credit score"

    if existing_loan > salary * 5:
        return "Rejected: Existing loan exceeds threshold"

    dti = (existing_loan / salary) * 100

    if dti > 50:
        return "Rejected: High DTI"

    if employment not in ["Salaried", "Self-Employed", "Government"]:
        return "Rejected: Invalid employment type"

    if requested_loan <= 0:
        raise ValueError("Invalid loan amount")

    if requested_loan > salary * 10 - existing_loan:
        return "Rejected: Loan amount exceeds eligibility"

    rate = 8 if credit_score >= 750 else 10
    r = rate / (12 * 100)
    n = tenure * 12

    emi = requested_loan * r * (1 + r) ** n / ((1 + r) ** n - 1)

    return "Approved | EMI: " + str(round(emi, 2))


def test(name, age, salary, loan, credit, job, amount, tenure):
    try:
        result = process_loan(
            age, salary, loan, credit, job, amount, tenure
        )
        print(name, ":", result)
    except Exception as e:
        print(name, ":", e)


print("----- Loan QA Testing -----")

# Minimum age
test("Minimum Age", 18, 50000, 5000, 700, "Salaried", 200000, 5)

# Maximum age
test("Maximum Age", 60, 50000, 5000, 700, "Salaried", 200000, 5)

# Invalid salary
test("Invalid Salary", 30, 0, 5000, 700, "Salaried", 200000, 5)

# Poor credit score
test("Poor Credit Score", 30, 50000, 5000, 500, "Salaried", 200000, 5)

# Existing loan exceeding threshold
test("Existing Loan Threshold", 30, 50000, 300000, 700, "Salaried", 200000, 5)

# High DTI
test("High DTI", 30, 50000, 26000, 700, "Salaried", 100000, 5)

# Different employment categories
test("Salaried", 30, 50000, 5000, 700, "Salaried", 200000, 5)
test("Self-Employed", 30, 50000, 5000, 700, "Self-Employed", 200000, 5)
test("Government", 30, 50000, 5000, 700, "Government", 200000, 5)

# Boundary loan amount
test("Boundary Loan", 30, 50000, 5000, 700, "Salaried", 495000, 5)

# EMI calculation accuracy
result = process_loan(30, 60000, 10000, 750, "Salaried", 500000, 5)
print("EMI Accuracy Test:", result)

# Invalid input handling
test("Invalid Loan Amount", 30, 50000, 5000, 700, "Salaried", -100, 5)

# Exception handling
try:
    process_loan(10, 50000, 5000, 700, "Salaried", 200000, 5)
except Exception as e:
    print("Exception Handling Test:", e)
