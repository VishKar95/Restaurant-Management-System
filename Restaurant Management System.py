# Restaurant Management System

class MenuItem:
    def __init__(self, code, name, quantity, price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price

class Restaurant:
    def __init__(self):
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def display_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(f"{item.code} - {item.name} - Quantity: {item.quantity} - Price: ${item.price}")

    def place_order(self, code, quantity):
        for item in self.menu_items:
            if item.code == code:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    total_price = item.price * quantity
                    print(f"Your order of {quantity} {item.name} has been placed. Total price: ${total_price}")
                    return
                else:
                    print(f"Sorry, {item.name} is out of stock.")
                    return
        print("Invalid menu item code.")

    def generate_report(self):
        total_revenue = 0
        for item in self.menu_items:
            total_revenue += (item.price * (item.quantity - 10))
        print(f"Total revenue: ${total_revenue}")

restaurant = Restaurant()

menu_item1 = MenuItem("P001", "Pizza", 10, 10)
menu_item2 = MenuItem("B001", "Burger", 20, 8)
menu_item3 = MenuItem("PS001", "Pasta", 15, 12)
menu_item4 = MenuItem("SD001", "Salad", 12, 7)
menu_item5 = MenuItem("SC001", "Soup", 8, 5)

restaurant.add_menu_item(menu_item1)
restaurant.add_menu_item(menu_item2)
restaurant.add_menu_item(menu_item3)
restaurant.add_menu_item(menu_item4)
restaurant.add_menu_item(menu_item5)

restaurant.display_menu()

restaurant.place_order("P001", 2)
restaurant.place_order("SC001", 4)

restaurant.generate_report()
