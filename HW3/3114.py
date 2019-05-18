def PrintData(**Data):
    if "uid" in Data:
        print("The user id: " + str(Data["uid"]))

    if "name" in Data:
        print("The username: " + str(Data["name"]))

    if "age" in Data:
        print("The user age: " + str(Data["age"]))



n1 = input()
n2 = input()
n3 = input()
PrintData(uid = n1, name = n2, age = n3)

n4 = input()
n5 = input()
PrintData(uid = n4, name = n5)

n6 = input()

PrintData(name = n6)
