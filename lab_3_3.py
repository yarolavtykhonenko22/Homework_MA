import math
import random


def get_rdoms():
    val1 = random.sample(range(100), 5)
    val2 = random.random()
    max_val = max(val1)
    res_div = max_val // val2
    if __name__ == "__main__":
        print(max_val)
        print(math.factorial(int(res_div)))


get_rdoms()
