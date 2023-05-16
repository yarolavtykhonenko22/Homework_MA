class BuildingMaterials:
    def __init__(self, material:str, color:str, number:int=0):
        self.material = material
        self.color = color
        self.number = number
        self.place(self.number)

    def place(self,b):
        if b <= 0:
            print('out of stock!!!')
        elif 0 < b < 100:
            print("warehouse")
        else:
            print("remote warehouse")
    def plus(self, counter):
        self.number += counter
        self.place(self.number)
    def minus(self, counter):
        self.number -= counter
        self.place(self.number)
    def info(self):
        print(f"material = {self.material}, color = {self.color}, number = {self.number}")
if __name__ == "__main__":
    brick = BuildingMaterials("brick", "white", 300)
    plank = BuildingMaterials("plank", "brown", 20)
    brick.info()
    plank.info()

    plank.minus(3)
    brick.plus(50)









