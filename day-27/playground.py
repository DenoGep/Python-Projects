def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

# print(add(1, 6, 18, 190))

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=5, multiply=3)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)