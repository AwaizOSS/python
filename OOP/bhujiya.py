class Car:
    # first letter capital for class name is the convention
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        # this has been made private
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        # get_ is the convention
        return self.__brand

    def full_name(self):
        print(self.__brand, self.__model)

    def fuel_type(self):
        print("petrol or diesel")

    @staticmethod
    # this is a decorator
    def general_description():
        # self as an argument is needed to make it accessible from objects
        return "car is a means of transport"

    @property
    # makes sure the variable used isnt directly read or written and is only available via this method
    def model(self):
        return self.__model


class ElectricCar(Car):
    # multiple inheritance is also supported
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def fuel_type(self):
        print("electricity")


superCar = Car("lambo", "aventador")
# print(superCar.model)
# print(Car.general_description())
print(isinstance(superCar, Car))
