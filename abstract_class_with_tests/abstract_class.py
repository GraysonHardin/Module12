from abc import abstractmethod, ABC


class Rider(ABC):
    @abstractmethod
    def ride(self):
        raise NotImplementedError("Abstract method not implemented")

    @abstractmethod
    def rider(self):
        raise NotImplementedError("Abstract method not implemented")


class Bicycle(Rider):
    def __init__(self, ride_message, rider_message):
        self.ride_message = ride_message
        self.rider_message = rider_message

    def ride(self):
        return self.ride_message

    def rider(self):
        return self.rider_message


class Motorcycle(Rider):
    def __init__(self, ride_message, rider_message):
        self.ride_message = ride_message
        self.rider_message = rider_message

    def ride(self):
        return self.ride_message

    def rider(self):
        return self.rider_message


class Car(Rider):
    def __init__(self, ride_message, rider_message):
        self.ride_message = ride_message
        self.rider_message = rider_message

    def ride(self):
        return self.ride_message

    def rider(self):
        return self.rider_message


bicycle_output = Bicycle('Human powered, not enclosed', '1 or 2 if tandem or a daredevil')
print(bicycle_output.ride())
print(bicycle_output.rider())

motorcycle = Motorcycle('Engine powered, not enclosed', '1 or 2')
print(motorcycle.ride())
print(motorcycle.rider())

car = Car('Engine powered, enclosed', '1 plus comfortably')
print(car.ride())
print(car.rider())
