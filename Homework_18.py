class House:
    def __init__(self):
        self.numberOfFloors = 0
        print(self.numberOfFloors)

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = 10
        print(self.numberOfFloors, floors)

house = House()
house.setNewNumberOfFloors(floors='floors')

