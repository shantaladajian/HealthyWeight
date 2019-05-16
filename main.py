import json
import os
import random

def loadOptions():
    with open('datas.json', 'r') as file:
        datas = json.load(file)

    user_options = datas["dataOptions"]
    return user_options


def AskForDataOptions(data):
    print("\nDear User, you're going to answer for the following : ", (" , ").join(data.keys()))
    x = input("\nDear user, please create a username by typing it in directly :")
    options = {x: {"dataOptions": {}}}

    for key in data:
        while True:
            datas = tuple(data[key])
            print("\nFor your " + key + " answer 0 for " + datas[0] + " , answer 1 for " + datas[1])
            if len(datas) > 2:
                print("answer 2 for " + datas[2])
            p = input("\nyour" + key + "is : ")
            if (p.isnumeric()):
                p = int(p)
                if p < 3 and p > -1:
                    options[x]["dataOptions"][key] = datas[p]
                    break
                else:
                    print("\nplease try again. Answer in the form of the integers mentioned above. \n")
            else:
                print("\nplease try again. Answer in the form of the INTEGERS mentioned above. \n")
    return x, options


def SaveOptions(options):
    a = os.listdir()
    if "users.json" in a:
        with open('users.json') as file1:
            initialold = json.load(file1)
            initialold.update(options)
        file = open('users.json', 'w')
        file.write(json.dumps(initialold))
        file.close()
    else:
        file = open("users.json", "w")
        file.write(json.dumps(options))
        file.close()


def AskForinitialData(x):
    a = open("users.json", "r")
    dataOptions = json.load(a)
    if dataOptions[x]['dataOptions']["healthCondition"] == "bad":
        print("\nWARNING: Dear user,because of your bad health condition, please consult your doctor before following our plan. :) \n")

    if dataOptions[x]['dataOptions']["initialWeightGoal"] == "maintain":
        def loadinitialDataForMaintain():
            a = os.listdir()
            if "datas.json" in a:
                with open('datas.json', 'r') as file:
                    datas = json.load(file)

                user_initialDataForMaintain = datas["initialDataForMaintain"]
                return user_initialDataForMaintain

        user_initialDataForMaintain = loadinitialDataForMaintain()

        print("\nDear User, you're going to answer for the following: ",
              (" , ").join(user_initialDataForMaintain.keys()), "\n")
        initial = {x: {"initialData": {}}}
        print(
            "\nInput you height in the integer form in cm, and your weight in kg.")
        for key in user_initialDataForMaintain:
            while True:
                inputt = input("your " + key + "is : ")
                if inputt.isnumeric():
                    inputt = int(inputt)
                    initial[x]["initialData"][key] = inputt
                    break
                else:
                    print("\n please try again. Answer in the form of the integers mentioned above.")
        return initial

    elif dataOptions[x]["dataOptions"]["initialWeightGoal"] == "lose":
        def loadinitialDataForLose():
            a = os.listdir()
            if "datas.json" in a:
                with open('datas.json', 'r') as file:
                    datas = json.load(file)
                user_initialDataForLose = datas["initialDataForLose"]
                return user_initialDataForLose

        user_initialDataForLose = loadinitialDataForLose()

        print("\nDear User, you're going to answer for the following : ",
              (" , ").join(user_initialDataForLose.keys()))
        initial = {x: {"initialData": {}}}
        print(
            "\nInput height in the integer form in cm, and weight in kg")

        for key in user_initialDataForLose:
            while True:
                inputt = input("your " + key + " is : ")
                try:
                    inputt = float(inputt)
                    initial[x]["initialData"][key] = inputt
                    break
                except ValueError as e:
                    print("\nplease try again. Answer in the form mentioned above.")
        return initial

    elif dataOptions[x]["dataOptions"]["initialWeightGoal"] == "gain":
        def loadinitialDataForGain():
            a = os.listdir()
            if "datas.json" in a:
                with open('datas.json', 'r') as file:
                    datas = json.load(file)
                user_initialDataForGain = datas["initialDataForGain"]
                return user_initialDataForGain

        user_initialDataForGain = loadinitialDataForGain()

        print("\nDear User, you're going to answer for the following:",
              (" , ").join(user_initialDataForGain.keys()))
        initial = {x: {"initialData": {}}}
        print("\nInput you height in the integer form in CM, and your weight in KG. \n ")
        for key in user_initialDataForGain:
            while True:
                inputt = input("your " + key + " is : ")
                try:
                    inputt = float(inputt)
                    initial[x]["initialData"][key] = inputt
                    break
                except ValueError as e:
                    print("\nplease try again. Answer in the form of the integers mentioned above. \n")
        return initial


def SaveInitial(x, initial):
    a = os.listdir()
    if "users.json" in a:
        with open('users.json') as file1:
            initialold = json.load(file1)
            initialold[x].update(initial[x])
        file = open('users.json', 'w')
        file.write(json.dumps(initialold))
        file.close()

def CalculatingBMI(x):
    a = open("users.json", "r")
    BMIfacts = json.load(a)
    h = int(BMIfacts[x]["initialData"]["height"])
    w = int(BMIfacts[x]["initialData"]["initialWeight"])
    BMI = float(w * 10000 / ((h * h)))
    BMI= "{:.2f}".format(BMI)
    print("\nYour BMI is:", BMI )
    if float(BMI) < 18.5:
        print("\nDear user, your BMI indicated that you're underweight.The normla range is between 18.5-24.9.")
        print("We suggest you choose the gaining goal if you haven't chosen that. ")
    elif float(BMI) > 18.5 and float(BMI) < 25:
        print(
            "\nDear user, your BMI indicated that you're in the normal weight range!The normla range is between 18.5-24.9 ")
        print("We suggest you choose the maintaining goal if you haven't chosen that.")
    elif float(BMI) > 25 and float(BMI) < 30:
        print(
            "\nDear user, your BMI indicated that you're in the overweight range.The normla range is between 18.5-24.9")
        print("We suggest you choose the losing goal if you haven't chosen that.")


def CalculatingBMR(x):
    a = open("users.json", "r")
    BMR = json.load(a)
    h = int(BMR[x]["initialData"]["height"])
    w = int(BMR[x]["initialData"]["initialWeight"])
    a = int(BMR[x]["initialData"]["Age"])
    if BMR[x]['dataOptions']["initialWeightGoal"] == "maintain":
        if BMR[x]['dataOptions']["gender"] == "male":
            CalorieIn = float(10 * w + 6.25 * h - 5 * a + 5)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "CaloriesPer day, to maintain your current weight :) \n")
        elif BMR[x]['dataOptions']["gender"] == "female":
            CalorieIn = float(10 * w + 6.25 * h - 5 * a - 161)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to maintain your current weight :) \n")
    if BMR[x]['dataOptions']["initialWeightGoal"] == "lose":
        lose = int(BMR[x]["initialData"]["Weight_You_Want_To_Lose_Per_Week"])
        if BMR[x]['dataOptions']["gender"] == "male":
            CalorieIn = float(10 * w + 6.25 * h - 5 * a + 5 - (lose * 3500) / 7)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", lose,
                  " Kgs from your current weight per week:)\nWe suggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
        if BMR[x]['dataOptions']["gender"] == "female":
            CalorieIn = float(10 * w + 6.25 * h - 5 * a - 161 - (lose * 3500) / 7)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", lose,
                  " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
    if BMR[x]['dataOptions']["initialWeightGoal"] == "gain":
        gain = int(BMR[x]["initialData"]["Weight_You_Want_To_Gain_Per_Week"])
        if BMR[x]['dataOptions']["gender"] == "male":
            CalorieIn = float(10 * w + 6.25 * h - 5 * a + 5 + (gain * 3500) / 7)
            CalorieIn="{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calorie Per day, to gain", gain,
                  " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
        if BMR[x]['dataOptions']["gender"] == "female":
            CalorieIn = float(10 * w + 6.25 * h - 5 * a - 161 + (gain * 3500) / 7)
            CalorieIn = "{:.2f}".format(CalorieIn)
            print("\nYou should eat:", CalorieIn, "Calories Per day, to gain", gain,
                  " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories. ")


def TipOfTheDay():
    with open('datas.json', 'r') as file:
        tips = json.load(file)
        dailytips = tips["TipsOfTheDay"]
    j=random.choices(tips["TipsOfTheDay"]["aidDigestion"])
    w=random.choices(tips["TipsOfTheDay"]["essentialOils"])
    print("\nToday's Tip of the day is :", ', '.join(j))
    print("\nand a fact about essential oils is:",', '.join(w))
    print("Dear user, thank you for using HealthyWeight :) Hope to see you soon!")


def NewUser():
    user_options = loadOptions()
    username, options = AskForDataOptions(user_options)
    SaveOptions(options)
    initial = AskForinitialData(username)
    SaveInitial(username, initial)
    CalculatingBMI(username)
    CalculatingBMR(username)
    TipOfTheDay()


def Save_New_Data(New_Weight, name):
    with open("users.json") as a:
        load = json.load(a)
        load[name]["initialData"]["initialWeight"] = New_Weight
        file = open('users.json', 'w')
        file.write(json.dumps(load))
        file.close()

def Create_New_Username():
    print("\nFile doesn't exist! so you do not have an account :(. ")
    create = input("\nDo you want to create a new account? Please answer in yes or no .")
    while True:
        if create == "yes":
            NewUser()
            break
        elif create == "no":
            print("\nokey See you next time :)")
            break
        else:
            print("\nplease answer in yes or no form.")

def CheckIfGoalisReached(New_Weight, name , Old_Weight):
    difference = New_Weight - Old_Weight
    with open("users.json") as a:
        load = json.load(a)
        Goal = load[name]["dataOptions"]["initialWeightGoal"]
        if difference > 0 and (Goal =="maintain" or Goal=="lose"):
            print("\nDear user, you have gained : ", difference , "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to", Goal," weight.\nWork harder you'll reach there")
        if difference >0  and Goal =="gain":
            print("\nDear user, you have gained : " , difference, "Kgs since we last saw you !\nYou're on the right track as your goal was to ", Goal, "your weight :) Keep on going :)")
        if difference <0 and (Goal =="maintain" or Goal=="gain"):
            print("\nDear user, you have lost: ", abs(difference),
                  "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to gain weight.\nWork harder you'll reach there")
        if difference <0 and Goal =="lose":
            print("\nDear user, you have lost : ", abs(difference),
                  "Kgs since we last saw you !\nYou're on the right track as your goal was to lose"
                  "weight :) Keep on going :)")

def Load_Old_Data(name):
    with open("users.json") as a:
        load = json.load(a)
        Old_Weight = load[name]["initialData"]["initialWeight"]
        print('Your initial weight was : ', Old_Weight)
        while True:
            change = input("Do you want to change it? Please answer in yes or no : ")
            if change == "yes":
                while True:
                    New_Weight = input("Insert your current weight in kg in numeric integer form : ")
                    if New_Weight.isnumeric():
                        New_Weight = int(New_Weight)
                        CheckIfGoalisReached(New_Weight, name, Old_Weight)
                        Save_New_Data(New_Weight, name)
                        TipOfTheDay()
                        break
                    else:
                        print("\nPlease write in kg in a numeric integer form:(")
                break
            elif change == "no":
                print("Okey you can change it whenever you want :) \n")
                TipOfTheDay()
                break
            else:
                print("\nPlease try it again and answer in the form of yes or no :)")
def UsernameisNone():
    while True:
        end = input("\nSory this username doesn't exist. Type 0 to end the Application\nType 1 to create a new username.")
        if end.isnumeric():
            end=int(end)
            if end==0:
                print("\nDear user, thank you for using HealthyWeight :) Hope to see you soon!")
                break
            elif end==1:
                NewUser()
                break
        else:
            print("please input an INTEGER.")

def OldUser():
        a = os.listdir()
        if "users.json" in a:
            with open("users.json") as file:
                user = json.load(file)
                while True:
                    name = input("\nplease type your previously created username : ")
                    if user.get(name) is None:
                        UsernameisNone()
                    else:
                        Load_Old_Data(name)
                        break
        else:
            Create_New_Username()

def Check():
    print("\nThis Application helps you reach your weight goal. :)")
    while True:
        MAIN = input("Have you used our app before? Please answer in yes or no : ")
        if MAIN == "no":
            NewUser()
            break
        elif MAIN == "yes":
            OldUser()
            break
        else:
            print("\nsorry Try again!Please type yes or no.(not capital)")

def MAIN():
    Check()
MAIN()














