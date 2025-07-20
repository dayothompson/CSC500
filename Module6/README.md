# Online Shopping Cart

A Python-based shopping cart application that allows users to manage items in their cart through an interactive menu system.

## Overview

This project implements a complete shopping cart system with two main classes:
- `Item` (formerly `ItemToPurchase`) - Represents individual items in the cart
- `ShoppingCart` - Manages the collection of items and provides cart operations

## Features

### Shopping Cart Management
- Add items to cart
- Remove items from cart
- Modify item quantities, prices, and descriptions
- View cart totals and item descriptions
- Interactive menu-driven interface

### Data Validation
- Input validation for item names, prices, and quantities
- Error handling for invalid operations
- User-friendly error messages

## Class Structure

### Item Class

**Constructor:**
```python
def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="")
```

**Attributes:**
- `item_name` (string) - Name of the item
- `item_price` (float) - Price of the item
- `item_quantity` (int) - Quantity of the item
- `item_description` (string) - Description of the item

**Methods:**
- `print_item_cost()` - Displays item cost in format: "Item @ $price = $total"

### ShoppingCart Class

**Constructor:**
```python
def __init__(self, customer_name="none", current_date="January 1, 2020")
```

**Attributes:**
- `customer_name` (string) - Name of the customer (default: "none")
- `current_date` (string) - Current date (default: "January 1, 2020")
- `cart_items` (list) - List of items in the cart

**Methods:**

#### add_item(ItemToPurchase)
- Adds an item to the cart_items list
- Parameter: ItemToPurchase object
- Returns: Nothing

#### remove_item(item_name)
- Removes item from cart_items list by name
- Parameter: String (item's name)
- Returns: Nothing
- Error handling: Outputs "Item not found in cart. Nothing removed." if item not found

#### modify_item(ItemToPurchase)
- Modifies an item's description, price, and/or quantity
- Parameter: ItemToPurchase object
- Returns: Nothing
- Logic: Checks if parameter has non-default values and modifies accordingly
- Error handling: Outputs "Item not found in cart. Nothing modified." if item not found

#### get_num_items_in_cart()
- Returns the total quantity of all items in cart
- Parameters: None
- Returns: Integer (total quantity)

#### get_cost_of_cart()
- Determines and returns the total cost of items in cart
- Parameters: None
- Returns: Float (total cost)

#### print_total()
- Outputs the total of objects in cart
- Parameters: None
- Returns: Nothing
- Special case: Outputs "SHOPPING CART IS EMPTY" if cart is empty

#### print_descriptions()
- Outputs each item's description
- Parameters: None
- Returns: Nothing

## Menu System

The application features an interactive menu system with the following options:

```
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:
```

### Menu Options

- **a** - Add item to cart
  - Prompts for item name, price, quantity, and description
  - Creates new Item object and adds to cart

- **r** - Remove item from cart
  - Prompts for item name to remove
  - Removes item if found, displays error if not found

- **c** - Change item quantity
  - Prompts for item name and new quantity
  - Modifies existing item quantity

- **i** - Output items' descriptions
  - Displays all item descriptions in formatted output

- **o** - Output shopping cart
  - Shows complete cart summary with totals

- **q** - Quit
  - Exits the program with goodbye message

## Output Examples

### Shopping Cart Output
```
OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2020
Number of Items: 8
Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128
Total: $521
```

### Item Descriptions Output
```
OUTPUT ITEMS' DESCRIPTIONS
John Doe's Shopping Cart - February 1, 2020
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones
```

## Error Handling

The application includes comprehensive error handling:

- **Invalid menu options**: Displays "Invalid option. Please try again."
- **Item not found for removal**: Displays "Item not found in cart. Nothing removed."
- **Item not found for modification**: Displays "Item not found in cart. Nothing modified."
- **Empty cart**: Displays "SHOPPING CART IS EMPTY"
- **Input validation**: Validates item names, prices, and quantities

## Usage

1. Run the main.py script
2. Enter customer name and current date
3. Use the interactive menu to manage your shopping cart
4. Choose 'q' to quit the program

## Technical Details

- **Language**: Python 3
- **Classes**: Object-oriented design with proper encapsulation
- **Input Validation**: Property decorators with validation logic
- **User Interface**: Console-based interactive menu
- **Data Structures**: Lists for cart management
- **Error Handling**: Comprehensive exception and error message handling

## File Structure

```
├── main.py          # Main application file
├── shopping_cart.py # Alternative implementation
└── README.md        # This documentation file
```

## Development Notes

- The `ItemToPurchase` class was renamed to `Item` to avoid naming conflicts
- Parameter names in methods use `ItemToPurchase` as specified in requirements
- All methods include proper documentation and error handling
- The menu system provides a user-friendly interface for all cart operations 