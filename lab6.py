# Part 1

orders = ["chai", "maggi", "chai", "samosa"]


orders.append("brownie")



orders.extend(["coffee", "cookie"])


orders.insert(1, "puff")


orders.remove("cookie")


served = orders.pop(0)

print("Served:", served)
print("Orders left:", len(orders))
print("Chai orders left:", orders.count("chai"))


saved = orders.copy()
saved.sort()

print("Saved (sorted):", saved)



orders.clear()

print("Orders after clearing:", orders)



# Part 2

lakeside_bookings = ["Asha", "Ravi", "Meera", "Asha", "Kabir"]
hilltop_bookings = ["Meera", "Kabir", "Ishaan", "Tara", "Meera"]

lakeside = set(lakeside_bookings)
hilltop = set(hilltop_bookings)

lakeside.add("Zoya")
lakeside.discard("Ravi")

everyone = lakeside.union(hilltop)
both = lakeside.intersection(hilltop)
lakeside_only = lakeside.difference(hilltop)
one_area = lakeside.symmetric_difference(hilltop)

print("Total unique guests:", len(everyone))
print("Both areas:", sorted(both))
print("Lakeside only:", sorted(lakeside_only))
print("Exactly one area:", sorted(one_area))
print("Both is a subset of Lakeside:", both.issubset(lakeside))


# Part 3

recipe = ("Masala Chai", 40, 4)

item_name, item_price, prep_time = recipe

print("item:", item_name, "| price:", item_price)
print("prep time:", prep_time)
print("count of 40:", recipe.count(40))
print("position of 4:", recipe.index(4))
print("first field:", recipe[0])


# Part 4

prices = {
    "Masala Chai": 40,
    "Samosa": 30,
    "Chocolate Brownie": 90,
    "Veg Puff": 45
}

stock = {
    "Masala Chai": 10,
    "Samosa": 4,
    "Chocolate Brownie": 8,
    "Veg Puff": 0
}

order = {
    "Masala Chai": 3,
    "Samosa": 2,
    "Chocolate Brownie": 1,
    "Veg Puff": 2
}

# Add a new item
prices["Lemonade"] = 60

# Change the price of Samosa
prices["Samosa"] = 35

# Remove Lemonade
prices.pop("Lemonade")

# Calculate the bill
bill = 0

for item, qty in order.items():
    bill += prices[item] * qty

# Apply discount
payable = bill

if bill > 300:
    payable = bill * 0.9

# Check stock availability
unavailable = []

for item, qty in order.items():
    if qty > stock.get(item, 0):
        unavailable.append(item)
    else:
        stock[item] -= qty

print("Bill:", bill)
print("Payable:", payable)
print("Unavailable:", unavailable)
print("Stock:", stock)


# Part 5A

menu_prices = {}

with open("data/menu.csv") as f:
    next(f)

    for line in f:
        fields = line.strip().split(",")

        item, category, price, prep_min, vegetarian = fields

        menu_prices[item] = int(price)

print("Items loaded:", len(menu_prices))
print("Masala Chai price:", menu_prices["Masala Chai"])
print("Filter Coffee price:", menu_prices["Filter Coffee"])


# Part 5B

sales = []

with open("data/monsoon_sales.csv") as f:
    columns = next(f).strip().split(",")

    for line in f:
        values = line.strip().split(",")

        row = dict(zip(columns, values))

        row["qty"] = int(row["qty"])

        sales.append(row)

# Calculate units sold per item
units_sold = {}

for row in sales:
    item = row["item"]

    units_sold[item] = units_sold.get(item, 0) + row["qty"]

print("Rows loaded:", len(sales))
print("Masala Chai units:", units_sold["Masala Chai"])
print("Chicken Roll units:", units_sold["Chicken Roll"])


# Part 6

# Read menu prices
menu_prices = {}

with open("data/menu.csv") as f:
    next(f)

    for line in f:
        fields = line.strip().split(",")

        item, category, price, prep_min, vegetarian = fields

        menu_prices[item] = int(price)

# Read sales and calculate revenue
report = {}

with open("data/monsoon_sales.csv") as f:
    columns = next(f).strip().split(",")

    for line in f:
        values = line.strip().split(",")

        row = dict(zip(columns, values))

        item = row["item"]
        qty = int(row["qty"])

        revenue = qty * menu_prices[item]

        if item not in report:
            report[item] = {
                "qty_sold": 0,
                "revenue": 0
            }

        report[item]["qty_sold"] += qty
        report[item]["revenue"] += revenue

# Sort by revenue (highest first)
sorted_report = sorted(
    report.items(),
    key=lambda pair: pair[1]["revenue"],
    reverse=True
)

# Print report
print("item,qty_sold,revenue")

for item, details in sorted_report:
    print(",".join([
        item,
        str(details["qty_sold"]),
        str(details["revenue"])
    ]))

print("Total items:", len(report))


# Part 7


# Read menu prices
menu_prices = {}

with open("data/menu.csv") as f:
    next(f)

    for line in f:
        fields = line.strip().split(",")

        item, category, price, prep_min, vegetarian = fields

        menu_prices[item] = int(price)

# Store customer information
customers = {}

with open("data/monsoon_sales.csv") as f:
    columns = next(f).strip().split(",")

    for line in f:
        values = line.strip().split(",")

        row = dict(zip(columns, values))

        customer = row["customer_id"]

        if customer == "":
            continue

        order_id = row["order_id"]
        item = row["item"]
        qty = int(row["qty"])

        revenue = qty * menu_prices[item]

        customers.setdefault(customer, {
            "orders": set(),
            "items": set(),
            "spend": 0
        })

        customers[customer]["orders"].add(order_id)
        customers[customer]["items"].add(item)
        customers[customer]["spend"] += revenue

# Count customers with at least 2 orders
loyal_customers = 0

for customer, details in customers.items():
    if len(details["orders"]) >= 2:
        loyal_customers += 1

print("Customers with at least 2 orders:", loyal_customers)

# Find highest spender
highest_spender = max(
    customers,
    key=lambda customer: customers[customer]["spend"]
)

print(
    "Highest spender:",
    highest_spender,
    customers[highest_spender]["spend"]
)

# Compare C01 and C02
c01_items = customers["C01"]["items"]
c02_items = customers["C02"]["items"]

common_items = c01_items.intersection(c02_items)
c01_only = c01_items.difference(c02_items)

print("Common items:", sorted(common_items))
print("C01 only:", sorted(c01_only))

# Create loyalty cards
cards = []

for customer, details in customers.items():
    order_count = len(details["orders"])
    item_count = len(details["items"])
    spend = details["spend"]

    cards.append((
        customer,
        order_count,
        item_count,
        spend
    ))

# Sort by spending (highest first), then customer ID
cards.sort(key=lambda row: (-row[3], row[0]))

print("Top 5 customers:")

for card in cards[:5]:
    print(*card)
