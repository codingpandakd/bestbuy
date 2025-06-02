from products import Product
from stores import Store

product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]
best_buy = Store(product_list)
products = best_buy.get_all_products()
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))


def start(store):
    while True:
        print("\nStore Menu")
        print("---------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # List all products in store
            store.list_products()
        elif choice == "2":
            # Show total amount in store
            total_quantity = store.get_total_quantity()
            print(f"Total of {total_quantity} items in store")
        elif choice == "3":
            # Make an order
            store.list_products()
            print("When you want to finish the order, enter empty text.")
            shopping_list = []
            while True:
                product_choice = input("Which product # do you want? ")
                if product_choice == "":
                    break
                try:
                    product_index = int(product_choice) - 1
                    if product_index < 0 or product_index >= len(store.get_all_products()):
                        print("Invalid product number.")
                        continue
                    product = store.get_all_products()[product_index]
                    amount = int(input("What amount do you want? "))
                    if amount <= 0:
                        print("Amount must be positive.")
                        continue
                    shopping_list.append((product, amount))
                except ValueError:
                    print("Please enter a valid number.")
            if shopping_list:
                total_payment = store.order(shopping_list)
                print(f"Order made! Total payment: ${total_payment:.2f}")
            else:
                print("No items in the order.")
        elif choice == "4":
            # Quit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)
