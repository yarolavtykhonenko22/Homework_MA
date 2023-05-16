from lab_7_2_1 import BuildingMaterials
class Market(BuildingMaterials):
    def __init__(self, price):
        self.price = price

if __name__ == "__main__":
    brick = BuildingMaterials("brick", "white", 300)
    plank = BuildingMaterials("plank", "brown", 20)
    brick.info()
    plank.info()



