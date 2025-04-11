from abc import ABC, abstractmethod

class Vehicle (ABC):

    @abstractmethod
    def get_rental_cost (self, days):
        pass

    @abstractmethod
    def license_required (self):
        pass

    def vehicle_info (self):
        print ("This is a vehicle available for rental")

class Car (Vehicle):
    def get_rental_cost(self, days):
        return 100 * days
    
    def license_required(self):
        return "Standard Car License"
    
    def vehicle_info(self):
        super().vehicle_info()
        print ("This is a sedan car suitable for families")

        print("Rental cost for 3 days:", self.get_rental_cost(3))
        print("License required:", self.license_required())
        print("-" * 40)




class Bike (Vehicle):
    def get_rental_cost(self, days):
        return 50 * days
    
    def license_required(self):
        return "Two-Wheeler License"
    
    def vehicle_info(self):
        super().vehicle_info()
        print ("This is a bullet bike suitable for solo ride")

        print("Rental cost for 3 days:", self.get_rental_cost(3))
        print("License required:", self.license_required())
        print("-" * 40)


class Truck (Vehicle):
    def get_rental_cost(self, days):
        return 150 * days
    
    def license_required(self):
        return "Heavy Vehicle License"
    
    def vehicle_info(self):
        super().vehicle_info()
        print ("This is a heavy truck suitable for transport")

        print("Rental cost for 3 days:", self.get_rental_cost(3))
        print("License required:", self.license_required())
        print("-" * 40)


def main():
    car = Car()
    car.vehicle_info()
    
    bike = Bike()
    bike.vehicle_info()

    truck = Truck ()
    truck.vehicle_info()

main()