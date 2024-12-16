import pickle

number_of_data = int(input('Adja meg hany darab adatot szeretne felvenni: '))

data = []

for i in range(number_of_data):
    row = input(str(i) + '. Adat beirasa: ')
    data.append(row)

with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

with open('data.pickle', 'rb') as file:
    content = pickle.load(file)
    print(content)
    for item in content:
        print(item)