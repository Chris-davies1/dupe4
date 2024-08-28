#Christian Davies
#CBIS 4210
#Assignment 01-02 - Sales tax calculator

# This is where the user imputs the price of the item
price = float(input("Enter the item price: $"))

# Here the user imputs the sales tax rate
tax_rate = float(input("Enter the sales tax rate (in percentage): "))

# Calculate the sales tax
sales_tax = price * (tax_rate / 100)

# Calculate the total price including tax
total_price = price + sales_tax

# Display the results
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Price: ${total_price:.2f}")
