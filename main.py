import database


menu = '''\nPlease select what you would like to do: 
1. Insert new inventory item
2. Remove inventory items
3. Search for item by name
4. Search for item by category
5. Update number of item in stock
6. Insert new Manufacturers
7. Insert Delivery Schedule
8. View sold out items and delivery dates
9. Update last delivery person for a manufacturer
10. View Database Tables
11. Exit

Your selection: '''

def prompt_add_inventory():
        name = input('Name of product: ')
        category = input('Category of product: ')
        cost = input('Price of product: ')
        amount = input('Amount of product: ')
        manufacturer = input('Manufacturer of product: ')
        database.add_item(name, category, cost, amount, manufacturer)


def prompt_add_manufacturer():
    manufacturer = input('Manufacturer of product: ')
    address = input('Manufacturer address: ')
    delivery_day = input('Manufacturer delivery day: ')
    database.add_manufacturer(manufacturer, address, delivery_day)


def prompt_remove_from_inventory():
    try:
        name = input('What is the name of the item you would like to delete: ')
        database.remove_item(name)
        print('Item deleted')
    except ValueError as error:
        print(error)

def search_item_by_name():
    name = input('What is the name of the item you are looking for: ')
    return name

def search_item_by_category():
    try:
        category = input('What is the category you are looking for: ')
        return category
    except ValueError as error:
        print(error)

def update_inventory():
    name = input('What is the name of the item would you like to update: ')
    amount = input('What is the new stock amount: ')
    database.update_stock(name, amount)

def sold_out():
    sold_out = database.check_sold_out()
    print(sold_out)

def delivery_schedule():
    delivery_person = input('What is the name of the delivery driver: ')
    phone_number = input('What is the number of the delivery driver: ')
    manufacturer = input('What is the manufacturer that the delivery is from: ')
    delivery_day = input('What day of the week do the deliveries come: ')
    database.create_deliveries(delivery_person, phone_number, manufacturer, delivery_day)


def update_delivery_person():
    person = input('What is the name of the new Delivery Person: ')
    number = input('What is the number of the new Delivery Person: ')
    manufacturer = input('What is the manufacturer they are delivering for: ')
    database.update_delivery_person(person, number, manufacturer)

def view_tables():
    choice = input('Which table would you like to view: \n1. Inventory\n2. Manufacturers\n3. Delivery Schedule\n: ')
    if choice == '1':
        inventory = database.view_inventory()
        print(inventory)
    elif choice == '2':
        manufacturers = database.view_manufacturers()
        print(manufacturers)
    elif choice == '3':
        deliveries = database.view_deliveries_table()
        print(deliveries)
#I put these together because the menu would be too crowded if they were separate.




database.create_tables()
# Main program starts here
while (user_input := input(menu)) != "11":
    if user_input == '1':
        prompt_add_inventory()

    elif user_input == '2':
        prompt_remove_from_inventory()

    elif user_input == '3':
        name = search_item_by_name()
        item = database.search_by_name(name)
        if item is not None:
            print(item)
        else:
            print('There is no item by that name, please try again.')
# I used an if statement to flag whether an item existed or not, but I couldn't figure out how to flag if it was out of stock.


    elif user_input == '4':
        category = search_item_by_category()
        item = database.search_by_category(category)
        if item is not None:
            print(item)
        else:
            print('There is no item byy that name, please try again.')

    elif user_input == '5':
        update_inventory()

    elif user_input == '6':
        prompt_add_manufacturer()

    elif user_input == '7':
        delivery_schedule()

    elif user_input == '8':
        sold_out()

    elif user_input == '9':
        update_delivery_person()

    elif user_input == '10':
        view_tables()

    else:
        print('Please select from the available options.')


