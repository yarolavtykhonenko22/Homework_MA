from lab_7_2_1 import BuildingMaterials
class Market(BuildingMaterials):
    def __init__(self, number: int = 0):
        self.number = number


    def plus(self, counter):
        self.number += counter
    def minus(self, counter):
        self.number -= counter
helper = Market()
helper.plus(0)
helper.minus(0)

if __name__ == "__main__":
    brick = BuildingMaterials("brick", "white", 300)
    plank = BuildingMaterials("plank", "brown", 20)
    brick.info()
    plank.info()
    brick.plus(50)
    plank.minus(3)
