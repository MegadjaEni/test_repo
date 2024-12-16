from nt import remove

list1 = [12, 23, 45, 74, 78, 90, 2, 4]
list2 = [2, 100, 8, 9, 6]
list3 = list1 + list2

print('A ket lista a harmadikba osszesitve: %s' %list3)
print('A list3 elemeinek a maximuma: %s' %max(list3))
print('list3 rendezve: %s' %sorted(list3))
rev = sorted(list3, reverse=True)
print('list3 forditott sorrendben: %s' %rev)
list3.remove(2)
print('A kettes duplikalt elem torolve: ', list3)
list3.pop(-1)
print('A lista torles utan: ', list3)

