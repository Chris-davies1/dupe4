#Christian Davies
#CBIS 4210
#Assignment 01-02 - Sales tax calculator

#sales tax calculator function
def calculate_sales_tax(price, tax_rate):
    sales_tax = price * (tax_rate / 100)
    return sales_tax

#calculats the price of the item with tax
def calculate_total_price(price, sales_tax):
    total_price = price + sales_tax
    return total_price

#main function to start the sales tax calculator
def main():
    print("Sales Tax Calculator")

#while function to check if price input is valid
    while True:
        try:
            price = float(input("Enter the price of the item: $"))
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")

#while function to check if tax rate input is valid
    while True:
        try:
            tax_rate = float(input("Enter the sales tax rate (in percentage): "))
            if tax_rate < 0:
                print("Tax rate cannot be negative. Please enter a valid tax rate.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the tax rate.")

    sales_tax = calculate_sales_tax(price, tax_rate)
    total_price = calculate_total_price(price, sales_tax)
#display the input price, tax rate, tax amount, and total price
    print(f"\nPrice: ${price:.2f}")
    print(f"Sales Tax ({tax_rate}%): ${sales_tax:.2f}")
    print(f"Total Price: ${total_price:.2f}")

#run the main function
if __name__ == "__main__":
    main()
