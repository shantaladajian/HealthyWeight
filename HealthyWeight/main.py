import json
import os
import random
print("This Application helps you reach your weight goal. :)")

def MAIN():
    MAIN = input("Have you used our app before?Please answer in yes or no")
    if MAIN == "no":
        def loadOptions():
            with open('datas.json', 'r') as file:
                datas = json.load(file)

            user_options = datas["dataOptions"]
            return user_options

        def AskForDataOptions(data):
            print("Dear User, you're going to answer for the following:", (" , ").join(data.keys()))
            global x
            x = input("Dear user, please create a username by typing it in directly")
            options = {x: {"dataOptions": {}}}

            for key in data:
                while True:
                    datas = tuple(data[key])
                    print("For your " + key + " answer 0 for " + datas[0] + " , answer 1 for " + datas[1])
                    if len(datas) > 2:
                        print("answer 2 for " + datas[2])
                    p = input("your" + key + "is=")
                    if (p.isnumeric()):
                        p = int(p)
                        if p < 3 and p > -1:
                            options[x]["dataOptions"][key] = datas[p]
                            break
                        else:
                            print("please try again. Answer in the form of the integers mentioned above.")
                    else:
                        print("please try again. Answer in the form of the integers mentioned above.")

            return options

        def SaveOptions(options):
            print(json.dumps(options))
            file = open("users.json", "w+")
            file.write(json.dumps(options))
            file.close()

        def AskForinitialData():
            global x
            a = open("users.json", "r")
            dataOptions = json.load(a)
            if dataOptions[x]['dataOptions']["healthCondition"] == "bad":
                print(
                    "WARNING: Dear user,because of your bad health condition, please consult your doctor before following our plan. :)")

            if dataOptions[x]['dataOptions']["initialWightGoal"] == "maintain":
                def loadinitialDataForMaintain():
                    a = os.listdir()
                    if "datas.json" in a:
                        with open('datas.json', 'r') as file:
                            datas = json.load(file)

                        user_initialDataForMaintain = datas["initialDataForMaintain"]
                        return user_initialDataForMaintain

                user_initialDataForMaintain = loadinitialDataForMaintain()

                print("Dear User, you're going to answer for the following:",
                      (" , ").join(user_initialDataForMaintain.keys()))
                initial = {x: {"initialData": {}}}

                for key in user_initialDataForMaintain:
                    print(
                        "Input you height in the integer form in cm, and your weight in kg, and the date in the integer form")
                    while True:
                        n = input("your" + key + "is=")
                        if (n.isnumeric()):
                            n = int(n)
                            initial[x]["initialData"][key] = n
                            break
                        else:
                            print("please try again. Answer in the form of the integers mentioned above.")
                return initial

            elif dataOptions[x]["dataOptions"]["initialWightGoal"] == "lose":
                def loadinitialDataForLose():
                    a = os.listdir()
                    if "datas.json" in a:
                        with open('datas.json', 'r') as file:
                            datas = json.load(file)
                        user_initialDataForLose = datas["initialDataForLose"]
                        return user_initialDataForLose

                user_initialDataForLose = loadinitialDataForLose()

                print("Dear User, you're going to answer for the following:",
                      (" , ").join(user_initialDataForLose.keys()))
                initial = {x: {"initialData": {}}}

                for key in user_initialDataForLose:
                    print(
                        "Input you height in the integer form in cm, and your weight in kg, and the date in the integer form")
                    while True:
                        n = input("your" + key + "is=")
                        if (n.isnumeric()):
                            n = int(n)
                            initial[x]["initialData"][key] = n
                            break
                        else:
                            print("please try again. Answer in the form of the integers mentioned above.")
                return initial

            elif dataOptions[x]["dataOptions"]["initialWightGoal"] == "gain":
                def loadinitialDataForGain():
                    a = os.listdir()
                    if "datas.json" in a:
                        with open('datas.json', 'r') as file:
                            datas = json.load(file)
                        user_initialDataForGain = datas["initialDataForGain"]
                        return user_initialDataForGain

                user_initialDataForGain = loadinitialDataForGain()

                print("Dear User, you're going to answer for the following:",
                      (" , ").join(user_initialDataForGain.keys()))
                initial = {x: {"initialData": {}}}

                for key in user_initialDataForGain:
                    print(
                        "Input you height in the integer form in cm, and your weight in kg, and the date in the integer form")
                    while True:
                        n = input("your" + key + "is=")
                        if (n.isnumeric()):
                            n = int(n)
                            initial[x]["initialData"][key] = n
                            break
                        else:
                            print("please try again. Answer in the form of the integers mentioned above.")
                return initial

        def SaveInitial(initial):
            a = os.listdir()
            if "users.json" in a:
                with open('users.json') as file1:
                    initialold = json.load(file1)
                    print(initialold)
                    initialold[x].update(initial[x])
                    print(initialold)
                file = open('users.json', 'w')
                file.write(json.dumps(initialold))
                file.close()

        def CalculatingBMI():
            a = open("users.json", "r")
            BMIfacts = json.load(a)
            h = int(BMIfacts[x]["initialData"]["height"])
            w = int(BMIfacts[x]["initialData"]["initialWeight"])
            BMI = float(w * 10000 / ((h * h)))
            print("Your BMI is:", BMI)
            if BMI < 18.5:
                print("Dear user, your BMI indicated that you're underweight.The normla range is between 18.5-24.9")
                print("We suggest you choose the gaining goal if you haven't chosen that.")
            elif BMI > 18.5 and BMI < 25:
                print(
                    "Dear user, your BMI indicated that you're in the normal weight range!The normla range is between 18.5-24.9")
                print("We suggest you choose the maintaining goal if you haven't chosen that.")
            elif BMI > 25 and BMI < 30:
                print(
                    "Dear user, your BMI indicated that you're in the overweight range.The normla range is between 18.5-24.9")
                print("We suggest you choose the losing goal if you haven't chosen that.")

        def CalculatingBMR():
            a = open("users.json", "r")
            BMR = json.load(a)
            h = int(BMR[x]["initialData"]["height"])
            w = int(BMR[x]["initialData"]["initialWeight"])
            a = int(BMR[x]["initialData"]["Age"])
            if BMR[x]['dataOptions']["initialWightGoal"] == "maintain":
                if BMR[x]['dataOptions']["gender"] == "male":
                    CalorieIn = float(10 * w + 6.25 * h - 5 * a + 5)
                    print("You should eat:", CalorieIn, "CaloriesPer day, to maintain your current weight :)")
                elif BMR[x]['dataOptions']["gender"] == "female":
                    CalorieIn = float(10 * w + 6.25 * h - 5 * a - 161)
                    print("You should eat:", CalorieIn, "Calories Per day, to maintain your current weight :)")
            if BMR[x]['dataOptions']["initialWightGoal"] == "lose":
                lose = int(BMR[x]["initialData"]["KgsLosePerWeek"])
                if BMR[x]['dataOptions']["gender"] == "male":
                    CalorieIn = float(10 * w + 6.25 * h - 5 * a + 5 - (lose * 3500) / 7)
                    print("You should eat:", CalorieIn, "Calories Per day, to lose", lose,
                          " Kgs from your current weight per week:)")
                if BMR[x]['dataOptions']["gender"] == "female":
                    CalorieIn = float(10 * w + 6.25 * h - 5 * a - 161 - (lose * 3500) / 7)
                    print("You should eat:", CalorieIn, "Calories Per day, to lose", lose,
                          " Kgs from your current weight per week:)")
            if BMR[x]['dataOptions']["initialWightGoal"] == "gain":
                gain = int(BMR[x]["initialData"]["KgsGainPerWeek"])
                if BMR[x]['dataOptions']["gender"] == "male":
                    CalorieIn = float(10 * w + 6.25 * h - 5 * a + 5 + (gain * 3500) / 7)
                    print("You should eat:", CalorieIn, "Calorie Per day, to gain", gain,
                          " Kgs from your current weight per week:)")
                if BMR[x]['dataOptions']["gender"] == "female":
                    CalorieIn = float(10 * w + 6.25 * h - 5 * a - 161 + (gain * 3500) / 7)
                    print("You should eat:", CalorieIn, "Calories Per day, to gain", gain,
                          " Kgs from your current weight per week:)")

        def TipOfTheDay():
            with open('datas.json', 'r') as file:
                tips = json.load(file)
            dailytips = tips["TipsOfTheDay"]
            print("Today's Tip of the day is:", random.choices(tips["TipsOfTheDay"]["aidDigestion"]))
            print("and a fact about essential oils is:", random.choices(tips["TipsOfTheDay"]["essentialOils"]))

        def main():
            user_options = loadOptions()
            options = AskForDataOptions(user_options)
            SaveOptions(options)
            initial = AskForinitialData()
            SaveInitial(initial)
            CalculatingBMI()
            CalculatingBMR()
            TipOfTheDay()

        main()
    elif MAIN == "yes":
        a = os.listdir()
        if "users.json" in a:
            with open("users.json") as file:
                try:
                    user = json.load(file)
                    name = input("please type your previously created username:")
                    if user.get(name) is None:
                        print("Dear user this username doesn't exist :( Please run again")
                    else:
                        a = open("users.json", "r")
                        load = json.load(a)
                        loadd = load[name]["initialData"]["initialWeight"]

                        print('Your initial weight was:', loadd)
                        while True:
                            i = input("Do you want to change it? Please answer in yes or no")
                            if i == "yes":
                                l = load[name]["initialData"]["initialWeight"] = input(
                                    "Insert your current weight in kg in numeric integer form.")
                                if l.isnumeric():
                                    l = int(l)
                                    newWeight = loadd - l
                                    print("You have lost:", newWeight, "Kgs keep on going:)")
                                    break
                                else:
                                    print("Please write in kg in a numeric integer form:( you have to run the program again:(")
                            elif i == "no":
                                print("Okey you can change it whenever you want :)")
                                break
                            else:
                                print("Please run it again and answer in the form of yes or no :)")
                except json.decoder.JSONDecodeError:
                    print("Your file is empty! So you don't have an account.Please run again")
        else:
            print("File doesnt exist! so you do not have an account :(.Please run again")
    else:
        print("sorry run again!Please type yes or no.")

MAIN()














