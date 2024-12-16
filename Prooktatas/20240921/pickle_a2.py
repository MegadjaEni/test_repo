import pickle

name = 'Mekk Elek'
url = 'https://mekk.elek'
dic = {'first': 'alma', 'second': 'citrom', 'third': 'eper'}
tup = (31, 'abcdef', 4.1)

with open('data.pickle', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(url, file)
    pickle.dump(dic, file)
    pickle.dump(tup, file)

with open('data.pickle', 'rb') as file:
    first = pickle.load(file)
    second = pickle.load(file)
    third = pickle.load(file)
    forth = pickle.load(file)
    print(first)
    print(second)
    print(third)
    print(forth)
