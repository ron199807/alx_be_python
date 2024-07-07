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
a = list(range(5,10))
print(a)

# using a step here 2 is a step
b = list(range(0, 10, 2))
print(b)

c = list(range(-10, -100, -30))
print(c)
