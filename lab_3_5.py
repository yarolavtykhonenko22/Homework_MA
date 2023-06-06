sm_txt = ["s", "w", 332, "S", "W", "q", 12, 46, 32, "r"]
stred_dict = str(sm_txt)


def get_text():
    slice_8_symbols = sm_txt[0:10]
    reversed_text = sm_txt[-1::-1]


get_text()
if __name__ == "__main__":
    print(sm_txt[0])
    print(sm_txt[-1])
    print(sm_txt[2], sm_txt[-3])
    print(sm_txt[2::2])
    print(sm_txt[len(sm_txt) // 2])
    print(stred_dict)
