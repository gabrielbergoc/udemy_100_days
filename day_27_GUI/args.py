def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum

print(add(5, 4, 3, 2, 1))

def product(*args):
    product = 1
    for n in args:
        product *= n

    return product

print(product(5, 4, 3, 2, 1))