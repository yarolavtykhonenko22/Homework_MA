import lab_7_3_1


class UserDate(lab_7_3_1.Date):
    pass


if date3 := lab_7_3_1.Date.from_string("12-2-345", "-"):
    if date3:
        date4 = lab_7_3_1.Date.from_string_static("12-2-345", "-")
        if date4:
            print(isinstance(date3, UserDate))
            print(isinstance(date4, UserDate))
