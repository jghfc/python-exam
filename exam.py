data = ["1234","123456", "12345678910","1234567","013","011","8543210","12345","1238974"]
a =[]
y =[]
def tuple_of_items(arg):
    x = 0
    while x < len(arg):
        if len(arg[x]) <= 4:
            a.append(arg[x])
        elif len(arg[x]) >= 7:
            y.append(arg[x])
        x = x + 1
    z = (a,y)
    print(z)
    

tuple_of_items(data)
