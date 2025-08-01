class Item:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        if not isinstance(value, str) or value.strip() == "" or value.isdigit():
            raise ValueError("Item name must be a non-empty string and not a number.")
        self._item_name = value

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Item price must be a non-negative number.")
        self._item_price = float(value)

    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Item quantity must be a non-negative integer.")
        self._item_quantity = value

    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, value):
        if not isinstance(value, str):
            raise ValueError("Item description must be a string.")
        self._item_description = value

    def print_item_cost(self):
        total_cost = self.item_quantity * self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        for cart_item in self.cart_items:
            if cart_item.item_name == ItemToPurchase.item_name:
                # Check if parameter has non-default values and modify accordingly
                if ItemToPurchase.item_description != "":
                    cart_item.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_price != 0:
                    cart_item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    cart_item.item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        
        for item in self.cart_items:
            item.print_item_cost()
        
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
    """
    Outputs a menu of options to manipulate the shopping cart.
    Each option is represented by a single character.
    """
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("Choose an option:")


def main():
    # Get customer information
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    
    # Create shopping cart
    cart = ShoppingCart(customer_name, current_date)
    
    # Menu loop
    while True:
        print_menu(cart)
        choice = input().lower().strip()
        
        if choice == 'q':
            print("Goodbye!\n")
            break
            
        elif choice == 'i':
            # Output items' descriptions
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            
        elif choice == 'o':
            # Output shopping cart
            print("OUTPUT SHOPPING CART")
            cart.print_total()
            
        else:
            print("Enter the item name:")
            name = input()
            print("Enter the item price:")
            price = float(input())
            print("Enter the item quantity:")
            quantity = int(input())
            print("Enter the item description:")
            description = input()
            
            item = Item(name, price, quantity, description)
            cart.add_item(item)
            print("Item added to cart.")
        
        print()  # Add blank line for readability
        

# Main program
if __name__ == "__main__":
    main()