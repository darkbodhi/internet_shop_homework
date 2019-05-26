class Category(object):

    def __init__(self, category_name, items, items_in_category):
        self.category_name = []
        self.items = []
        self.items_in_category = {"Name of category: ": {}, "Items: ": {}.format(self.category_name, self.items)}

    def display_categories(self, category_name):
        print(self.category_name)

    def display_category_items(self, items_in_category):
        print(self.items_in_category)

    def add_category(self, category_name):
        add_name = str(input("Please, insert the name of a new category: "))
        self.category_name.append(add_name)

    def remove_category(self, category_name):
        remove_name = str(input("Please, insert the name of a new category: "))
        for remove_name in self.category_name:
            self.category_name.remove()
        else:
            raise Exception("Error. The name is not in the list.")


class Items(object):

    def __init__(self, items, category_name, items_in_category):
        self.items = []
        self.category_name = []
        self.items_in_category = []

    def display_items(self):
        print (self.items_in_category.keys())

    def add_item(self, items_in_category):
        particular_category_name = str(input("Please, insert the name of the category to append with the item: "))
        new_item = str(input("Please, insert the name of the new item: "))
        self.items_in_category.update["particular_category_name": "new_item"]

    def remove_item(self):
        remove_item = str(input("Please, insert the name of the item to be removed: "))
        for remove_item in self.items:
            self.items.remove()

class UserAccount():

    def __init__(self, user_name, user_money):
        self.user_name = str()
        self.user_money = int()
        self.list_of_orders = []


class order_chart(object):

    def __init__ (self):
        self.items = []
        self.prices = []
        self.stock = []
        self.bascet = {"Name: ": {}, "Price: ": {}, "Number in stock: ": {} .format(self.items, self.prices, self.stock)}
        self.order = {{}, {} .format(self.items, self.prices)}

    def display_stock(self):
        print(self.basket)

    def add_order(self):
        product = str(input("Insert the name of the item you would like to order: "))
        for product in self.items:
            self.order.append(product)
        else:
            print('Error. The item is not in the stock')

    def remove_order(self):
        product = str(input("Insert the name of the item you would like to remove from order: "))
        for product in self.order:
            self.order.remove()
        else:
            print("Error. Item is not in the order list.")

    def count_the_bill(self):
        print(sum(self.order))
        list_of_orders.append(self.order)