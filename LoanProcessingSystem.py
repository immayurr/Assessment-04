# Banking Loan Approval System

customer_id = "C101"
age = 30
monthly_salary = 60000
existing_loan = 10000
credit_score = 750
employment_type = "Salaried"
requested_loan = 500000
loan_tenure = 5

# Debt-to-Income Ratio
dti = (existing_loan / monthly_salary) * 100

# Eligible loan amount
eligible_loan = monthly_salary * 10 - existing_loan

# Interest rate based on credit score
if credit_score >= 750:
    interest_rate = 8.0
elif credit_score >= 650:
    interest_rate = 10.0
else:
    interest_rate = 12.0

# EMI calculation
r = interest_rate / (12 * 100)
n = loan_tenure * 12
emi = requested_loan * r * (1 + r) ** n / ((1 + r) ** n - 1)

# Approval conditions
approved = (
    18 <= age <= 60
    and monthly_salary > 0
    and credit_score >= 650
    and existing_loan <= monthly_salary * 5
    and dti <= 50
    and requested_loan <= eligible_loan
    and employment_type in ["Salaried", "Self-Employed", "Government"]
)

print("----- Loan Processing System -----")
print("Customer ID:", customer_id)
print("Age:", age)
print("Monthly Salary:", monthly_salary)
print("Existing Loan:", existing_loan)
print("Credit Score:", credit_score)
print("Employment Type:", employment_type)
print("Requested Loan:", requested_loan)
print("Loan Tenure:", loan_tenure, "years")
print("Debt-to-Income Ratio:", round(dti, 2), "%")
print("Eligible Loan Amount:", eligible_loan)
print("Interest Rate:", interest_rate, "%")
print("Monthly EMI:", round(emi, 2))

if approved:
    print("Approval Status: APPROVED")
else:
    print("Approval Status: REJECTED")
