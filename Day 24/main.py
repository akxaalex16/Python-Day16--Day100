# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# this closes the files 
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
