product = []
new_product = []
def enter_p():
    x = input('enter name of product')
    return x
def add_p(p):
    y = enter_p()
    p.append(y)
    add_another_p()


def display_p():
    print(product)

def add_another_p():
    z = input("add another Y or exit N")
    if z == "Y":
        add_p(product)
    elif z == "N":
        display_p()
    else:
        print("invalid_input")
        add_another_p()
add_p(product)

def to_lower():
    x = 0
    while x < len(product):
        y= product[x].lower()
        new_product.append(y)
to_lower()
def search_anything():
    x = ('search for any product')
    y = x.lowerlower()
    z = 0
    if y in new_product[z]:
        count_item = new_product.count(y)
        total = len(new_product)
        print('numbers of', y, 'is: ',count_item)
        print("total item in product is:",total)
    else:
        print('item not found')
search_anything()
