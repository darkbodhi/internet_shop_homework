import psycopg2

class Category(object):

    def __init__(self, category_name, items, items_in_category):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("CREATE TABLE Categories(Name varchar(255), Items, PRIMARY KEY(Name)")
        cur.execute("CREATE TABLE Items(Name varchar(255), Quantity int, Price int, PRIMARY KEY(Name)")
        cur.close()
        conn.close()

    def display_categories(self, category_name):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("SELECT Name FROM Categories")
        a = cur.fetchone()
        return a
        cur.close()
        conn.close()

    def display_category_items(self, items_in_category):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("SELECT Name, Items FROM Categories")
        a = cur.fetchone()
        return a
        cur.close()
        conn.close()

    def add_category(self, category_name):
        category_name = str(input("Please, insert the name of the category: "))
        items_list = str(input("Please, import the list of the items for the category: "))
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("INSERT INTO Categories VALUES (%s, %s), category_name, items_list")
        cur.close()
        conn.close()


    def remove_category(self, category_name):
        category_name = str(input("Please, insert the name of the category: "))
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("DELETE FROM Categories WHERE VALUES (%s), category_name")
        cur.close()
        conn.close()


class Items(object):

    def __init__(self, items, category_name, items_in_category):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        item_base = cur.execute("SELECT * FROM Items")
        return item_base
        cur.close()
        conn.close()


    def display_items(self):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        item_base = cur.execute("SELECT * FROM Items")
        print(item_base)
        cur.close()
        conn.close()

    def add_item(self, items_in_category):
        new_item = str(input("Please, insert the name of the new item: "))
        quantity = int(input("Please, insert the quantity of the new item: "))
        price = int(input("Please, insert the price of the new item: "))
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("INSERT INTO Items VALUES (%s, %s, %s), new_item, quantity, price")
        cur.close()
        conn.close()

    def remove_item(self):
        remove_item = str(input("Please, insert the name of the item to be removed: "))
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("DELETE FROM Items WHERE VALUES (%s), remove_item")
        cur.close()
        conn.close()

class UserAccount():

    def __init__(self, user_name, user_money):
        self.user_name = str()
        self.user_money = int()
        self.list_of_orders = []


class order_chart(object):

    def __init__ (self):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("SELECT * FROM Items")
        cur.execute("SELECT * FROM Categories")
        a = cur.execute(UNION ALL)
        return purchase_base
        cur.close()
        conn.close()
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        order = cur.execute("CREATE TABLE Basket(User, Name, Quantity, Price, PRIMARY KEY(User))")
        return order
        cur.close()
        conn.close()

    def display_stock(self):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        item_base = cur.execute("SELECT * FROM Items")
        print(item_base)
        cur.close()
        conn.close()

    def add_order(self):
        name_item = str(input("Please, insert the name of the item to add: "))
        price_item = int(input("Please, insert the price of the item to add: "))
        quantity_item = int(input("Please, insert the quantity of items to purchase: "))
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("INSERT INTO Basket VALUES(%s, %s, %s) name_item, price_item, quantity_item")
        cur.close()
        conn.close()

    def remove_order(self):
        name_item = str(input("Please, insert the name of the item to remove: "))
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        cur.execute("DELETE FROM Basket WHERE VALUE(%s) name_item")
        cur.close()
        conn.close()

    def count_the_bill(self):
        conn = psycopg2.connect("dbname=internet_shop, user=postgres")
        order = cur.execute("SELECT * FROM Basket")
        print order
        cur.close()
        conn.close()