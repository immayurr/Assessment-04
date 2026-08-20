# E-Commerce Order Processing System - QA

def process_order(products, coupon):

    stock = {
        "P101": 10,
        "P102": 20,
        "P103": 5
    }

    category_discount = {
        "Electronics": 5,
        "Clothing": 10,
        "Grocery": 3
    }

    subtotal = 0
    category_discount_amount = 0

    for p in products:

        if p["id"] not in stock:
            raise ValueError("Invalid product")

        if p["quantity"] < 0:
            raise ValueError("Negative quantity")

        if p["quantity"] == 0:
            return "Zero quantity"

        if p["quantity"] > stock[p["id"]]:
            return "Out of stock"

        amount = p["quantity"] * p["price"]
        subtotal += amount

        discount = category_discount.get(p["category"], 0)
        category_discount_amount += amount * discount / 100

    # Bulk discount
    total_quantity = sum(p["quantity"] for p in products)
    bulk_discount = 5 if total_quantity >= 5 else 0
    bulk_amount = subtotal * bulk_discount / 100

    # Coupon
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20
    }

    if coupon == "":
        coupon_amount = 0
    elif coupon not in coupons:
        return "Invalid coupon"
    else:
        coupon_amount = subtotal * coupons[coupon] / 100

    # Maximum discount
    total_discount = (
        category_discount_amount
        + bulk_amount
        + coupon_amount
    )

    maximum_discount = subtotal * 30 / 100
    total_discount = min(total_discount, maximum_discount)

    amount_after_discount = subtotal - total_discount

    # GST
    gst = amount_after_discount * 18 / 100

    # Free shipping
    shipping = 0 if amount_after_discount >= 50000 else 500

    final_amount = amount_after_discount + gst + shipping

    return round(final_amount, 2)


def test(name, products, coupon=""):
    try:
        result = process_order(products, coupon)
        print(name, ":", result)
    except Exception as e:
        print(name, ":", e)


print("----- Order Management QA -----")

# 1. Single product
test("Test 1 - Single Product", [
    {"id": "P101", "category": "Electronics",
     "quantity": 1, "price": 20000}
])

# 2. Multiple products
test("Test 2 - Multiple Products", [
    {"id": "P101", "category": "Electronics",
     "quantity": 2, "price": 20000},
    {"id": "P102", "category": "Clothing",
     "quantity": 2, "price": 1500}
])

# 3. Zero quantity
test("Test 3 - Zero Quantity", [
    {"id": "P101", "category": "Electronics",
     "quantity": 0, "price": 20000}
])

# 4. Negative quantity
test("Test 4 - Negative Quantity", [
    {"id": "P101", "category": "Electronics",
     "quantity": -2, "price": 20000}
])

# 5. Invalid product
test("Test 5 - Invalid Product", [
    {"id": "P999", "category": "Electronics",
     "quantity": 1, "price": 20000}
])

# 6. Invalid coupon
test("Test 6 - Invalid Coupon", [
    {"id": "P101", "category": "Electronics",
     "quantity": 1, "price": 20000}
], "WRONG10")

# 7. Valid coupon
test("Test 7 - Valid Coupon", [
    {"id": "P101", "category": "Electronics",
     "quantity": 1, "price": 20000}
], "SAVE10")

# 8. Maximum discount
test("Test 8 - Maximum Discount", [
    {"id": "P101", "category": "Electronics",
     "quantity": 5, "price": 20000}
], "SAVE20")

# 9. Tax calculation
test("Test 9 - Tax Calculation", [
    {"id": "P102", "category": "Clothing",
     "quantity": 2, "price": 1500}
])

# 10. Free shipping
test("Test 10 - Free Shipping", [
    {"id": "P101", "category": "Electronics",
     "quantity": 3, "price": 20000}
])

# 11. Shipping charge
test("Test 11 - Shipping Charge", [
    {"id": "P102", "category": "Clothing",
     "quantity": 1, "price": 1500}
])

# 12. Bulk order
test("Test 12 - Bulk Order", [
    {"id": "P102", "category": "Clothing",
     "quantity": 5, "price": 1500}
])

# 13. Out of stock
test("Test 13 - Out of Stock", [
    {"id": "P103", "category": "Grocery",
     "quantity": 10, "price": 500}
])

# 14. Category discount - Electronics
test("Test 14 - Electronics Discount", [
    {"id": "P101", "category": "Electronics",
     "quantity": 1, "price": 20000}
])

# 15. Category discount - Clothing
test("Test 15 - Clothing Discount", [
    {"id": "P102", "category": "Clothing",
     "quantity": 2, "price": 1500}
])

# 16. Category discount - Grocery
test("Test 16 - Grocery Discount", [
    {"id": "P103", "category": "Grocery",
     "quantity": 2, "price": 500}
])

# 17. Multiple products with coupon
test("Test 17 - Multiple + Coupon", [
    {"id": "P101", "category": "Electronics",
     "quantity": 2, "price": 20000},
    {"id": "P102", "category": "Clothing",
     "quantity": 2, "price": 1500}
], "SAVE10")

# 18. Bulk + coupon
test("Test 18 - Bulk + Coupon", [
    {"id": "P102", "category": "Clothing",
     "quantity": 5, "price": 1500}
], "SAVE10")

# 19. Boundary free shipping
test("Test 19 - Shipping Boundary", [
    {"id": "P101", "category": "Electronics",
     "quantity": 3, "price": 20000}
])

# 20. Invalid quantity handling
test("Test 20 - Invalid Quantity", [
    {"id": "P101", "category": "Electronics",
     "quantity": -1, "price": 20000}
])
