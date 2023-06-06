first_set = {1, 4, "r", "t", 5, 8, "q", 0}
second_set = {2, 5, "e", "p", 9, 6, "a"}

intersection = tuple(first_set & second_set)
difference = tuple(first_set - second_set)
slice_inter = intersection[:3]
reversed_tuple = intersection[-1::-1]
first_set = list(first_set)
second_set = list(second_set)


def get_only_nums():
    for val2 in second_set:
        try:
            print(int(val2), end="    ")
        except ValueError:
            val2 = None


if __name__ == "__main__":
    print(set(first_set))
    get_only_nums()
