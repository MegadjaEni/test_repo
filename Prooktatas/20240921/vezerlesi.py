x = False
if x:
    print('Igaz')
else:
    print('Hamis')

x = 'citrom'

if x == 'Alama':
    print('Nagyon finom az alma')
elif x == 'barack':
    print('A barack mindig ledus')
else:
    print(x)

var = input('Adjon meg egy ket szamjegyu szamot')
if len(var) ==2:
    if var[0] > var[1]:
        print('Az elso szamjegy nagyobb mint a masodik')
    elif var[0] < var[1]:
        print('Az elso szamjegy kisebb mindt a masodik')
    else:
        print('A ket szamjegy egyenlo')
else:
    print('csak ketto karaktert fogadunk el')


# Palindrom pl legel vissza felé olvasva ugyan az
