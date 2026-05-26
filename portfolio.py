# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

# Input stock details
for i in range(n):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        portfolio[stock_name] = quantity

    else:
        print("Stock not available!")

# Calculate total investment
print("\n===== PORTFOLIO DETAILS =====")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(f"{stock} -> Price: ${price} | Quantity: {quantity} | Total: ${investment}")

print("\nTotal Investment Value = $", total_investment)

# Save result to text file
file = open("portfolio.txt", "w")

file.write("STOCK PORTFOLIO DETAILS\n\n")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    file.write(f"{stock} -> Price: ${price}, Quantity: {quantity}, Total: ${investment}\n")

file.write(f"\nTotal Investment Value = ${total_investment}")

file.close()

print("\nPortfolio saved successfully in portfolio.txt")