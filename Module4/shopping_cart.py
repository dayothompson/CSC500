class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        # Initialize item attributes with default values
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        # Calculate total cost for this item
        total_cost = int(self.item_quantity) * float(self.item_price)
        # Print item cost in the required format
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost:.2f}")


if __name__ == "__main__":
    # Prompt user for details of the first item
    print("Item 1")
    while True:
        name1 = input("Enter the item name:\n")
        # Try to convert to integer; if successful, ask again
        try:
            int(name1)
            print("Item name cannot be an integer. Please enter a valid name.")
        except ValueError:
            break  # Input is not an integer, so accept it
    price1 = float(input("Enter the item price:\n"))
    quantity1 = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(name1, price1, quantity1)

    # Prompt user for details of the second item
    print("\nItem 2")
    while True:
        name2 = input("Enter the item name:\n")
        # Try to convert to integer; if successful, ask again
        try:
            int(name2)
            print("Item name cannot be an integer. Please enter a valid name.")
        except ValueError:
            break  # Input is not an integer, so accept it
    price2 = float(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(name2, price2, quantity2)

    # Print the total cost summary
    print("\nTOTAL COST\n")
    item1.print_item_cost()
    item2.print_item_cost()
    # Calculate and print the combined total cost
    total_cost = float(item1.item_price) * int(item1.item_quantity) + float(item2.item_price) * int(item2.item_quantity)
    print(f"\nTotal: ${total_cost:.2f}")
    