def billing(items):
    total = sum(item["price"] * item["quantity"] for item in items)
    total_quantity = sum(item["quantity"] for item in items)

    if total > 1000:
        discount_rate = 0.15
    elif total > 500:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discount = total * discount_rate
    grand_total = total - discount

    return {
        "items": [item["name"] for item in items],
        "total_quantity": total_quantity,
        "total_price": total,
        "discount_rate": discount_rate,
        "discount": discount,
        "grand_total": grand_total,
    }

items = []
for i in range(1, 4):
    name = input(f"Enter name {i}: ")
    price = int(input(f"Enter price {i}: "))
    quantity = int(input(f"Enter quantity {i}: "))
    items.append({"name": name, "price": price, "quantity": quantity})

invoice = billing(items)
print("Items:", ", ".join(invoice["items"]))
print("Total quantity:", invoice["total_quantity"])
print("Total price:", invoice["total_price"])
print(f"Discount ({int(invoice['discount_rate'] * 100)}%):", invoice["discount"])
print("Grand total:", invoice["grand_total"])
