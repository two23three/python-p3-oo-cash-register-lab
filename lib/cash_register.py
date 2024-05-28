#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def remove_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to remove."
        self.total -= (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        for _ in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
        self.previous_transactions.pop()

#test

register = CashRegister(discount=20)

# Add items to the register
register.add_item("Apple", 1, 3)  # Adding 3 apples at $1 each
register.add_item("Banana", 2, 2)  # Adding 2 bananas at $2 each

# Print the current state
print("Items:", register.items)
print("Total before discount:", register.total)

# Apply the discount
register.apply_discount()

# Add another item
register.add_item("Orange", 1.5, 4)  # Adding 4 oranges at $1.5 each

# Print the current state
print("Items after adding oranges:", register.items)
print("Total after adding oranges:", register.total)

# remove the last transaction
register.remove_last_transaction()

# Print the current state
print("Items after removing last transaction:", register.items)
print("Total after removing last transaction:", register.total)

# Attempt to remove another transaction
register.remove_last_transaction()

# Print the current state
print("Items after removing another transaction:", register.items)
print("Total after removing another transaction:", register.total)
