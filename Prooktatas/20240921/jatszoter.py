#ARDS_KWARGS
def summarise(*args):
    return sum(args)

print(summarise(1, 2, 3))
print(summarise(4, 5, 6, 7, 8, 9))


def display_user_details(**kwargs): # szótárba gyüjti a kulcsérték párokat
    for k, v in kwargs.items():
        print(f"{k}: {v}")


display_user_details(nev='Elek', kor=33, lakhely='Budapest')


def display_all(name, *args, **kwargs):
    print(f"nev: {name}")
    print(f"pozicionált argomentumok: {args}")
    print(f"kulcs érték párok: {kwargs}")


    display_all('Elek', 1, 2, 3, kor=33, lakhely='Budapest')


def fn1(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

def fn2(*args, **kwargs):
    fn1(*args, **kwargs)

fn2(1, 2, 3, kor=33, lakhely='Budapest')

def display_discounted_products(*products, **discounts):
    print('Termékek akcióban:', ', '.join(products))
    for product, discount in discounts.items():
        print(f"{product}: {discount}& kedvezmény")


display_discounted_products("kenyér", "tej", "tojás", kenyér="10", tojás="20", tej="30")


def display_discounted_products(*args, **kwargs):
    print('Termékek akcióban:', ', '.join(args))
    for product, discount in kwargs.items():
        print(f"{product}: {discount}& kedvezmény")

display_discounted_products("kenyér", "tej", "tojás", kenyér="10", tojás="20", tej="30")