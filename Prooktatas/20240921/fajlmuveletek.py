content = open('./teszt.txt', 'r', encoding='utf-8')
print(content.read())
content.close()

with open('./teszt.txt', 'r', encoding='utf-8') as content:
    print(content.read())

with open('.venv/./teszt.txt', 'w', encoding='utf-8') as file:
    file.write('ez az elso sor\n')
    file.write('Ez as masodik sor\n')
    file.write('ez a harmadik sor')

with open('.venv/lol.txt', 'w', encoding='utf-8') as file:
    file.write("hahaha" * 1000)

with open('.venv/teszt.txt', 'a', encoding='utf-8') as file:
    file.seek(0)
    file.write('Hozzsfuz')

with open('.venv/teszt.txt', 'r+', encoding='utf-8') as file:
    file.write('teszt')
    print(file.read())

with open('nincs.txt', 'r+', encoding='utf-8') as file:
    file.write('TESZT')

