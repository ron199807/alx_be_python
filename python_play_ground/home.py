# for loops
# words = ["cat", "window", "defenestrate"]
# for w in words:
#     print(w, len(w))

"""
code that modifies a collection while itareting over that same
collection can be tricky to get right . instead, it is usually
is usually more straight forward to loop over a copy of that collection


"""
# a sample collection
#users = {'hans': 'active', 'eleonore': 'inactive', 'ronald': 'active'}

# strategy: iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#         print(f"'{user}' you are not active")

# strategy: creat a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print(f"'{active_users}' thank you for being active")

# the range faction
# for i in range(5):
#     print(i)
# a = list(range(5,10))
# print(a)

# using a step here 2 is a step
# b = list(range(0, 10, 2))
# print(b)

# c = list(range(-10, -100, -30))
# print(c)

# custom exception
# class OutOfStockError(Exception):
#     """Custom exception for handling out-of-stock items."""

#     def __init__(self, item_name):
#         self.item_name = item_name

#     def __str__(self):
#         return f"Sorry, the item '{self.item_name}' is out of stock."

# # Sample Product Inventory
# product_inventory = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 0,  # Out of stock
#     "grapes": 3
# }

# # testing the custom exception
# def purchase_item(item, quantity):
#     try:
#         if product_inventory[item] == 0:
#             raise OutOfStockError(item)
#         else:
#             print(f"Purchase successful: {quantity} {item}(s)")
#             product_inventory[item] -= quantity
#     except KeyError:
#         print(f"Sorry, '{item}' is not available in our inventory.")

# # Testing the Custom Exception
# try:
#     purchase_item("apple", 3)  # Purchase successful
#     purchase_item("orange", 1)  # Raises OutOfStockError
#     purchase_item("watermelon", 1)  # Item not available
# except OutOfStockError as e:
#     print(e)  # Output:

# exercise1 Handling zeroDivisionError
def division(x, y):
    if y == 0:
        raise zeroDivisionError("cant divid by zero")
    return x / Y
division(2, 0)







