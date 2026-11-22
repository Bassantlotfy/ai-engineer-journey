name = input("What is your name? ")
item = input("What is your requested item? ")
price = float(input("How much is it? "))
quantity = int(input("How many did you take? "))
subtotal = price * quantity
tax_percent = 14
tax = subtotal * tax_percent / 100
total = subtotal + tax
if price <= 0 or quantity <=0:
    print("Invalid")
else:
    discount_rate = "0%"
    discount_amount = 0
    if subtotal >= 1000:
       discount_rate = "10%"
       discount_amount = total * 0.10
    elif subtotal >= 500:
       discount_rate = "5%"
       discount_amount = total * 0.05
    else:
       print("no discount")
    final_total = total - discount_amount
    print("                 OFFICIAL RECEIPT")
    print(f"Customer name: {name}")
    print(f"Item purchased: {item}")
    print(f"Unit price: ${price:.2f}")
    print(f"quantity: {quantity}")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: {tax}")
    print(f"Total with tax: ${total}")
    print(f"Discount: {discount_rate} ${discount_amount}")
    print(f"FINAL TOTAL: ${final_total}")
    print("                Thank you for your purchase!")

      