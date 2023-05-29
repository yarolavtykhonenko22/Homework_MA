class BuildingMaterials:
    def __init__(self, material: str, color: str, number: int = 0):
        self.material = material
        self.color = color
        self.__number = number
        self.place(self.__number)

    @property
    def get_number(self):
        return self.__number

    @get_number.setter
    def set_number(self, value):
        if value >= 0:
            self.__number = value
        else:
            raise ValueError()

    def place(self, b):
        if b <= 0:
            print('out of stock!!!')
        elif 0 < b < 100:
            print("warehouse")
        else:
            print("remote warehouse")

    def plus(self, counter):
        self.__number += counter
        self.place(self.__number)

    def minus(self, counter):
        self.__number -= counter
        self.place(self.__number)

    def info(self):
        print(f"material = {self.material}, color = {self.color}, number = {self.__number}")


if __name__ == "__main__":
    brick = BuildingMaterials("brick", "white", 300)
    plank = BuildingMaterials("plank", "brown", 20)
    brick.info()
    plank.info()

    plank.minus(3)
    brick.plus(50)


def test1():
    test_value = BuildingMaterials("marble", "black", 23)
    test_value.number = 35
    assert test_value.number == 35, f"your property doesn't work, excepted 35, got {test_value.number}"

if __name__ == "__main__":
    test1()
