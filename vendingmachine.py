class VendingMachine:
    def __init__(self):
        self.items = {
            'A1': {'name': 'Coke', 'price': 3.00, 'stock': 86, 'category': 'Drinks'},
            'A2': {'name': 'Pepsi', 'price': 3.00, 'stock': 10, 'category': 'Drinks'},
            'B1': {'name': 'Rani', 'price': 2.50, 'stock': 7, 'category': 'Drinkss'},
            'B2': {'name': 'Mars', 'price': 3.50, 'stock': 8, 'category': 'Snacks'},
            'C1': {'name': 'lays', 'price': 1.00, 'stock': 5, 'category': 'Snacks'},
            'C2': {'name': 'Dairymilk', 'price': 3.00, 'stock': 4, 'category': 'Snacks'},
            'D1': {'name': 'pringles', 'price': 5.00, 'stock': 9, 'category': 'Snacks'},
            'D2': {'name': 'dew', 'price': 3.00, 'stock': 31, 'category': 'Drinkss'},
            
        }
        self.balance = 0.0

    def display_menu(self):
        print("Available Items:")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - ${item['price']} ({item['stock']} in stock)")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Current balance: ${self.balance:.2f}")

    def suggest_item(self, category):
        print(f"Since you bought an item from {category}, you might also like:")
        for code, item in self.items.items():
            if item['category'] == category and item['stock'] > 0:
                print(f"{code}: {item['name']} - ${item['price']}")

    def select_item(self, code):
        if code in self.items:
            item = self.items[code]
            if item['stock'] > 0:
                if self.balance >= item['price']:
                    self.items[code]['stock'] -= 1
                    self.balance -= item['price']
                    change = self.balance
                    self.balance = 0
                    print(f"Dispensing {item['name']}")
                    print(f"Change returned: ${change:.2f}")
                    self.suggest_item(item['category'])
                else:
                    print("Insufficient balance. Please insert more money.")
            else:
                print("Item out of stock.")
        else:
            print("Invalid code. Please try again.")

    def run(self):
        while True:
            self.display_menu()
            code = input("Enter the code of the item you want to purchase: ")
            self.select_item(code)
            more = input("Do you want to buy another item? (yes/no): ").lower()
            if more != 'yes':
                break
            money = float(input("Insert money: "))
            self.insert_money(money)

if __name__ == "__main__":
    vm = VendingMachine()
    initial_money = float(input("Insert money to start: "))
    vm.insert_money(initial_money)
    vm.run()
