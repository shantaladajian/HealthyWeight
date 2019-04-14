import json

def loadSetupData():
    with open('datas.json') as file:
        datas = json.load(file)

    user_setup = datas["dataOptions"]
    return user_setup

def AskForDataOptions(setup):
    print("Dear User, you're going to answer for the following:", (",").join(setup.keys()))
    print("please write in the mentioned form:", "1 for male and 0 for female",
          "0 for bad, 1 for normal and 2 for good", "0 for maintaining your weight , 1 to lose and 2 to gain",
          ".input these in an integer form")
    user = {"initialdata": {}}
    while True:
        for key in setup:
            p = int(input("your" + key + "is="))
        if p < 3 and p > -1:
            user["initialdata"][key] = setup[key][p]
            return user
            break
        else:
            print("please try again. Answer in the form of the integers mentioned above")

def SaveData(user):
    print (json.dumps(user))
    file = open("user.json", "w")
    file.write(json.dumps(user))
    file.close()

def main():
    user_setup = loadSetupData()
    user= AskForDataOptions(user_setup)
    SaveData(user)


main()








