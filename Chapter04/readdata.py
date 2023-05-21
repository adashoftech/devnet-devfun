# readdata = open("randomtext.txt", "r")
# print(readdata.read())
# readdata.close()

with open("randomtext.txt", "r") as data:
    print(data.read())

with open("randomtext.txt", "+a") as data:
    data.write('\nstate: Virginia')

with open("randomtext.txt", "r") as data:
    print(data.read())