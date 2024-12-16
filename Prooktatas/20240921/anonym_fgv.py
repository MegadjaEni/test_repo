import os


def square(num):
    return num * num


square2 = lambda num: num * num
add = lambda a,b: a + b #lambda névtelen függvény

print(square2(7))
print(add(1,2))

print(square.__name__) #neve
print(square2.__name__)
print(add.__name__)

list1 = [1, 5, 4, 6, 8, 11, 3, 12]
even_list = list(filter(lambda x: x%2 == 0, list1)) #filter=részhalmazt akarunk vissza kapni
print(even_list)

square_list = list(map(lambda x: x * x, list1)) # map=minden elemre vonatkozik
print(square_list)

users = [
    {'usersname': 'Elek', 'comments': ['Szuper a Python', 'Nagyon szeretem', 'Szorakoztat a Python']},
    {'usersname': 'Feri', 'comments': ['En is szeretem']},
    {'usersname': 'Jakab', 'comments': []},
    {'usersname': 'Mari', 'comments': []},
    {'usersname': 'Tomi', 'comments': ['Nagyon ehes vagyok']},
]

inactive_users = list(filter(lambda u: not u ['comments'], users))
print(inactive_users)

inactive_users2 = [user for user in users if not user['comments']]
print(inactive_users2)

username = list(map(lambda user: user['usersname'].upper(), filter(lambda u: not u ['comments'], users)))
print(username)

map_fn = lambda user: user['usersname'].upper()
filter_fn = filter(lambda u: not u ['comments'], users)
usernames = list(map(map_fn, filter_fn))


username2 = [user['usersname'].upper() for user in users if not user['comments']]
print(username2)


print(os.walk('zene'))

for utvonal, konyvtarak, fajlok in os.walk('zene', topdown=True): #os.walk generátor függvény
    print(utvonal)
    slpit1 = os.path.split(utvonal)
    print(slpit1)
    slpit2 = os.path.split(slpit1[0])
    print(fajlok)
    for f in fajlok:
       # print(os.path.split(f))
        print(f[:5].split(' - '))
