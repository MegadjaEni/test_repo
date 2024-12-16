# ha nem számot ad meg a felhasználó elszáll

#width = int(input("Add meg a szélességet: "))
#height = int(input("Add meg a hosszúságot: "))
#area = width * height
#print(f"A terület: {area}")



# kijavítva:
while True:
    try:
        szelesseg = int(input("Add meg a szélességet: "))
        break  # Ha számot ad meg kilép
    except ValueError:
        print("Hibás adat! Kérlek, csak számot adj meg.")

while True:
    try:
        hosszusag = int(input("Add meg a hosszúságot: "))
        break
    except ValueError:
        print("Hibás adat! Kérlek, csak számot adj meg.") # Ha nem számot ad meg

area = szelesseg * hosszusag
print(f"A terület: {area}")

