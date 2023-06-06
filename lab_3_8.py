my = "Hello my file"
file = open("myfile", "w+")
file.write("Hello file world \n")

file = open("myfile", "w+")
if __name__ == "__main__":
    print(file.read())
file.write(my)
