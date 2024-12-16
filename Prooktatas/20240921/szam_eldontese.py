var = input('Kérem írjon be valamit: ')

if var.isalpha():
    print('A beirt ertek csak betuket tartalmaz')
elif var.isdigit() == True:
    print('A beirt ertek csak szamokat tartalmaz')
else:
    print('A beirt ertek vegyes karaktereket tartalmaz')
