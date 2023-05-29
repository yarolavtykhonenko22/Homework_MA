from lab_7_2_1 import BuildingMaterials


class MarketFactory(BuildingMaterials):
    def __init__(self):
        pass

    @staticmethod
    def factory(type):
        if type == "brick":
            return Brick()
        if type == "plank":
            return Plank()
        assert 0, f"we don't have such material as {type}"


class Brick(MarketFactory):
    def info(self):
        brick = ["brick", "white", 100]
        return brick


class Plank(MarketFactory):
    def info(self):
        plank = ["plank", "brown", 20]
        return plank


def test1():
    object = MarketFactory.factory("brick")
    object.info()
    assert object.info() == ['brick', 'white', 100], f" it's doesn't work, excepted: ['brick', 'white', 100], got {object.info()}"


def test2():
    object = MarketFactory.factory("plank")
    object.info()
    assert object.info() == ["plank", "brown", 20], f" it's doesn't work, excepted: ['plank', 'brown', 20], got {object.info()}"


if __name__ == "__main__":
    test1()
    test2()