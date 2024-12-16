a = set()
b = {1, 2, 3} #{}

a.add(1)
print(a)
a.add(2)
print(a)
#print(a[0])
list1 = [1,1,2,2,3,3,45,6,6,6,7,8,9,9]
print(set(list1))
list2 = list(set(list1))
print(list2)
print(list2[0])
tup1 = tuple(list1)
print(tup1)
str1 = ' '.join(str(list1))
print(list1)
