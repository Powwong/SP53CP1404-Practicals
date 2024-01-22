import random
from prac_06.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        if random.uniform(0, 100) < float(self.reliability):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven