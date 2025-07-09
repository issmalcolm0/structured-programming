
def cafeteria_system():
    # 1. Prompt for current hour
    try:
        current_hour = int(input("Enter the current hour (in 24-hour format, e.g., 13 for 1:00 PM): "))
    except ValueError:
        print("Invalid input for hour. Please enter an integer.")
        return

    # 2. Check operating hours
    if not (7 <= current_hour <= 19):  # 7:00 AM to 7:00 PM (19:00 in 24-hour format)
        print("Cafeteria is closed. Orders are only accepted between 7:00 AM and 7:00 PM.")
        return

    # 3. Display meal options and prices
    meal_prices = {
        "Standard Meal": 12000,
        "Vegetarian Meal": 10000,
        "Deluxe Meal": 15000
    }
    print("\nMeal Options:")
    for meal, price in meal_prices.items():
        print(f"{meal} - {price:,} UGX")

    # 4. Prompt for meal orders
    try:
        standard_qty = int(input("Enter the number of Standard Meals: "))
        vegetarian_qty = int(input("Enter the number of Vegetarian Meals: "))
        deluxe_qty = int(input("Enter the number of Deluxe Meals: "))
    except ValueError:
        print("Invalid input for meal quantity. Please enter an integer.")
        return

    # Calculate total meals and base price
    total_meals_ordered = standard_qty + vegetarian_qty + deluxe_qty
    base_price = (standard_qty * meal_prices["Standard Meal"]) + \
                 (vegetarian_qty * meal_prices["Vegetarian Meal"]) + \
                 (deluxe_qty * meal_prices["Deluxe Meal"])

    # 5. Calculate total price with discount
    discount_amount = 0
    if total_meals_ordered > 3:
        discount_amount = base_price * 0.10
        total_amount_to_pay = base_price - discount_amount
    else:
        total_amount_to_pay = base_price

    # 6. Display order summary
    print("\nOrder Summary:")
    print(f"Number of Standard Meals ordered: {standard_qty}")
    print(f"Number of Vegetarian Meals ordered: {vegetarian_qty}")
    print(f"Number of Deluxe Meals ordered: {deluxe_qty}")
    print(f"Total number of meals: {total_meals_ordered}")
    if discount_amount > 0:
        print(f"Discount applied: {discount_amount:,.0f} UGX")
    else:
        print("No discount applied.")
    print(f"Total amount to pay: {total_amount_to_pay:,.0f} UGX")

# Run the system
cafeteria_system()