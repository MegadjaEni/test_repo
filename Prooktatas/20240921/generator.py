def simle_gen_func():
    n = 1
    print('Ezt irja ki először')
    yield n

    n += 1
    print('Ezt irjuk ki másodiknak')
    yield n

    n += 1
    print('Ezt irjuk ki harmadiknak')
    yield n

v1 = simle_gen_func()
print(next(v1))
print(next(v1))
print(next(v1))
#print(next(v1))

for item in simle_gen_func():
    print(item)


test_list = [1, 3, 6, 10]

print([x ** 2 for x in test_list])

print((x ** 2 for x in test_list))

v2 = (x ** 2 for x in test_list)

print("##GEN")
print(next(v2))
print(next(v2))
print(next(v2))
print(next(v2))


print(sum(x ** 2 for x in test_list))
print(max(x ** 2 for x in test_list))


class Sample1:

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 * self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = Sample1(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i))
print('=======')

i2 = iter(a)

for item in i2:
    print(item)