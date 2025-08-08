
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 330,
    "AMZN": 135
}

total_investment = 0
investment_details = []

print("Welcome to the Simple Stock Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    value = stock_prices[stock] * quantity
    total_investment += value
    investment_details.append(f"{stock} - {quantity} shares - ${value}")

print("\nInvestment Summary:")
for detail in investment_details:
    print(detail)
print(f"Total Investment: ${total_investment}")

# Optional: Save to a .txt file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as file:
        file.write("Investment Summary:\n")
        for detail in investment_details:
            file.write(detail + "\n")
        file.write(f"Total Investment: ${total_investment}\n")
    print("Results saved to 'investment_summary.txt'")

