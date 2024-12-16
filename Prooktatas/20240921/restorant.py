# 1. Adatok betöltése file-ból
# 2. Új rendelések felvitele
# 3. Rendelések mentése
# 4. Rendelés módosítása
# 5. Rendelés megtekintése
# 6. statiszikák
# 7. Rendelés törlése
import csv
import json
from datetime import datetime

MENU_FILE = 'menu.csv'
ORCERS_FILE = 'orders.json'

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} Ft"

    def __repr__(self):
        return f"{self.name} - {self.price} Ft"

    def to_dict(self):
        return {"name": self.name, "price": self.price}

class Order:
    def __init__(self, customer_name: str, table_number: str, items: list[MenuItem]):
        self.customer_name = customer_name
        self.table_number = table_number
        self.items = items
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def total_price(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        item_names = ', '.join(item.name for item in self.items)
        return (f"Vevő: {self.customer_name}, Asztal: {self.table_number}, Tételek: {item_names},"
                f"Total: {self.total_price()} Ft, Idő: {self.timestamp}")

    def __repr__(self):
        item_names = ', '.join(item.name for item in self.items)
        return (f"Vevő: {self.customer_name}, Asztal: {self.table_number}, Tételek: {item_names},"
                f"Total: {self.total_price()} Ft, Idő: {self.timestamp}")

    def to_dict(self):
        return {
            "customert_name": self.customer_name,
            "table_number": self.table_number,
            "items": [item.to_dict() for item in self.items],
            "timestamp": self.timestamp
        }


def load_menu(filename):
    menu = [ ]
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(MenuItem(row['name'], int(row['price'])))
    except FileNotFoundError:
        print('Menu file nem található. Ellenőrizd le, hogy a menu.csv megtalálható e?')
    except:
        print('Kritikus hiba történt')
    return  menu

def save_orders(orders, filename):
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump([order.to_dict() for order in orders], file)
    except TypeError as err:
        print("Kritikus hiba történt: ")
        print(err)

def load_orders(filename):
    orders = []
    try:
        with open(filename, mode="r", encoding='utf-8') as file:
            orders_dict = json.load(file)
            for order_dict in orders_dict:
                items = [MenuItem(item['name'], item['price']) for item in orders_dict['items']]
                orders.append(Order(order_dict['customer_name'], orders_dict['table_number'], items))
    except FileNotFoundError:
        print('Rendelés file nem található. Ellenőrizd le, hogy a rendelés file megtalálható e?')
    except:
        print('Kritikus hiba történt!')
    return orders
        
def list_menu(menu):
    print("=== Menu ===")
    for index, item in enumerate(menu, start=1):
        print(f"{index}, {item}")

def take_order(menu):
    print('=== Új megrendelés ===')
    customer_name = input("Vevő neve: ")
    table_number = input("Asztal száma: ")
    list_menu(menu)
    items = []
    while True:
        choice = input("Kérem válasszon egy elemet szám alapján. (Ha nem akar választani nyomjon entert): ")
        if not choice:
            break
        if choice.isdigit() and 1 <= int(choice) <= len(menu):
            items.append(menu[int(choice) - 1])
        else:
            print("Rossz választási opciót adott meg. Próbálja meg újra...")
    return Order(customer_name, table_number, items)

def list_orders(orders):
    print("=== Jelenlegi rendelések ===")
    for index, order in enumerate(orders, start= 1):
        print(f"{index}, {order}")

def delete_order(orders):
    list_orders(orders)
    choice = input("Válasszon ki egy rendelést a törléshez: ")
    if choice.isdigit() and 1 <= int(choice) <= len(orders):
        del orders[int(choice) - 1]
        print("Rendelés törölve!")
    else:
        print("Rossz a választott opció.")

def generate_statistics(orders):
    if not orders:
        print("Nincs megrendelés a statisztikékhoz!")
        return
    total_revenue = sum(order.total_price() for order in orders)
    all_items = [item.name for order in orders for item in order.items]
    most_popular = max(set(all_items), key=all_items.count)
    print(f"Teljes bevétel: {total_revenue}Ft")
    print(f"Legnépszerűbb: {most_popular}")

def main():
    menu = load_menu(MENU_FILE)
    orders = load_orders(ORCERS_FILE)

    while True:
        print("=== Étterem alkalmazás ===")
        print('1. Menü listázása')
        print("2. Új rendelés felvétele")
        print("3. Rendelés listázása")
        print("4. Rendelés törlése")
        print("5. Statisztikák")
        print("6. Mentés és kilépés")

        choice = input('Válaszon egy elemet: ')
        if choice == '1':
            list_menu(menu)
        elif choice == "2":
            order = take_order(menu)
            orders.append(order)
        elif choice == "3":
            list_orders(orders)
        elif choice == "4":
            delete_order(orders)
        elif choice == "5":
            generate_statistics(orders)
        elif choice == "6":
            save_orders(orders, ORCERS_FILE)
            print("Rendelés sikeressen elmentve, kilépés... ")
            break
        else:
            print("Ilyen opció nincs!")

main()