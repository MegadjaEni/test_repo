var1 = input('irjon be egy szoveget: ')
print(" A kovetkezo szoveget irta be: {}".format(var1))
list1 = list(var1)
print(list1)
print(list1[-1])
print(len(list1))
var2 = '-'.join(list1)
print(var2)