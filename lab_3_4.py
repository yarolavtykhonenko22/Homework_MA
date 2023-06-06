sm_txt = "some1_doing_someTHING56789"


def get_text():
    slice_8_symb = sm_txt[0:8]
    rvrs_txt = sm_txt[-1::-1]


get_text()
if __name__ == "__main__":
    print(sm_txt[0])
    print(sm_txt[-1])
    print(sm_txt[2], sm_txt[-3])
    print(sm_txt[3::3])
    print(sm_txt[len(sm_txt) // 2])
