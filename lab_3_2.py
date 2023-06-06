var1 = None
var2 = True


def testing_val():
    if var1:
        return "var1 =", True
    else:
        return "var1 =", False


def testing_val2():
    if var2:
        return "var2 =", True
    else:
        return "var2 =", False


if __name__ == "__main__":
    print(var1, var2)
    print(type(var1))
    testing_val()
    testing_val2()
