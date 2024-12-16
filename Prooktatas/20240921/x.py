a = 'Almafa'

def some_fn():
    global a
    a = 'Barack'

some_fn()
print(a)