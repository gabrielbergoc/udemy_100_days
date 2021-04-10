def foo(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print(foo(a=1, b=2, c=3), "\n")


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.num_seats = kwargs.get("num_seats")


my_car = Car(make="Ford", model="Focus")

print(my_car.make, my_car.model, my_car.color, my_car.num_seats)