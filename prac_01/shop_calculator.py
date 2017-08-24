quantity = 0
total = 0
is_valid_number = False
while not is_valid_number:
    quantity = int(input("Number of items: "))
    if quantity <= 0:
        print("Invalid number of items!")
        is_valid_number = False
    else:
        is_valid_number = True

for i in range(0, quantity,1):
    price = float(input("price of items: $"))
    total += price

if total > 100:
    discount = total * 0.10
    total -= discount
print("Total price for", quantity, "items is $", total)