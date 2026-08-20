# E-Commerce Order Processing System

products = [
    {"id": "P101", "category": "Electronics", "quantity": 2,
     "price": 20000, "discount": 10, "tax": 18},

    {"id": "P102", "category": "Clothing", "quantity": 3,
     "price": 1500, "discount": 5, "tax": 5}
]

coupon = "SAVE10"

stock = {
    "P101": 10,
    "P102": 20
}

category_discount = {
    "Electronics": 5,
    "Clothing": 10,
    "Grocery": 3
}

try:
    subtotal = 0
    category_discount_amount = 0

    for product in products:

        if product["id"] not in stock:
            raise ValueError("Invalid product")

        if product["quantity"] <= 0:
            raise ValueError("Invalid quantity")

        if product["quantity"] > stock[product["id"]]:
            raise ValueError("Product out of stock")

        amount = product["quantity"] * product["price"]
        subtotal += amount

        discount = category_discount.get(product["category"], 0)
        category_discount_amount += amount * discount / 100

    # Bulk-order discount
    total_quantity = sum(p["quantity"] for p in products)

    bulk_discount = 5 if total_quantity >= 5 else 0
    bulk_discount_amount = subtotal * bulk_discount / 100

    # Coupon discount
    valid_coupons = {
        "SAVE10": 10,
        "SAVE20": 20
    }

    if coupon in valid_coupons:
        coupon_discount = valid_coupons[coupon]
    else:
        coupon_discount = 0

    coupon_amount = subtotal * coupon_discount / 100

    # Maximum discount limit
    total_discount = (
        category_discount_amount
        + bulk_discount_amount
        + coupon_amount
    )

    maximum_discount = subtotal * 30 / 100

    if total_discount > maximum_discount:
        total_discount = maximum_discount

    discounted_amount = subtotal - total_discount

    # GST
    gst = 18
    gst_amount = discounted_amount * gst / 100

    # Free shipping threshold
    if discounted_amount >= 50000:
        shipping = 0
    else:
        shipping = 500

    final_amount = discounted_amount + gst_amount + shipping

    print("----- E-Commerce Order -----")
    print("Number of Products:", len(products))
    print("Subtotal:", round(subtotal, 2))
    print("Category Discount:", round(category_discount_amount, 2))
    print("Bulk Discount:", round(bulk_discount_amount, 2))
    print("Coupon Discount:", round(coupon_amount, 2))
    print("Maximum Discount Applied:", round(total_discount, 2))
    print("GST:", round(gst_amount, 2))
    print("Shipping Charge:", shipping)
    print("Final Amount:", round(final_amount, 2))

except Exception as e:
    print("Order Processing Error:", e)
