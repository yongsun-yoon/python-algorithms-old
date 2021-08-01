class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_limit = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.parking_limit[carType] -= 1
        return self.parking_limit[carType] >= 0