import os
import pandas as pd

#try reading the csv
try:
    df = pd.read_csv("lists.csv")
#add the headers if the file is completely empty
except:
    df = pd.DataFrame(columns=["time", "plan"])
    df.to_csv("lists.csv", index=False)
    df = pd.read_csv("lists.csv")

def FirstMenu():
    df = pd.read_csv("lists.csv")
    df.index = df.index + 1
    if df.empty:
        print("Empty plan")
    else:
        print(df)

def SecondMenu():
    df = pd.read_csv("lists.csv")
    plan = input("Enter the plan: ")
    while True:
        time = input("Enter the time: ")
        #check if the time is digit and has length of 4
        if time.isdigit() and len(time) == 4:
            #formats the inputted time with string slicing
            time = f"{time[:2]}:{time[2:]}"
            #converts the new plan to DataFrame which can be added to csv
            newplan = pd.DataFrame([{"time": time, "plan": plan}])
            #merge the old data with new values which carries new plan to the file
            df = pd.concat([df, newplan], ignore_index=False)
            #save it again to the file
            df.to_csv("lists.csv", index=False)
            break
        #return error if the inputted time is digits but the length is not 4
        elif time.isdigit():
            print("error: use 4 digits of hour and minute (for example 1200 = 12:00)")
        #return error if the inputted time is not only in digits
        else:
            print("error: use digits for the time")

def ThirdMenu():
    df = pd.read_csv("lists.csv")
    if df.empty:
        print("Already empty schedule")
    else:
        #rewrite the data to headers only
        df = pd.DataFrame(columns=["time", "plan"])
        #save the file
        df.to_csv("lists.csv", index=False)
        print("Schedule resetted!")

def FourthMenu():
    df = pd.read_csv("lists.csv")
    df.index = df.index + 1
    if not df.empty:
        print(df)
        while True:
            df = pd.read_csv("lists.csv")
            index = input("Select which plan you want to edit (by index): ")
            if index.isdigit() and int(index) > 0 and int(index) <= len(df):
                #check the validity of the inputted time then formats it
                while True:
                    time = input("Enter the new time: ")
                    if time.isdigit() and len(time) == 4:
                        time = f"{time[:2]}:{time[2:]}"
                        break
                    #error if the inputted time is less than o and more than 4 digits
                    elif time.isdigit() and not len(time) == 4:
                        print("error: use 4 digits of hour and minute (for example 1200 = 12:00)")
                    #error if the inputted time is not digits only
                    else:
                        print("error: use digits for the time")
                plan = input("Input the plan: ")
                #change the value of inputted digits with new plan
                df.loc[int(index) - 1] = [time, plan]
                df.to_csv("lists.csv", index=False)
                print("Success!")
                break
            else:
                if len(df) == 1:
                    print("Enter the correct index (1)")
                elif len(df) == 2:
                    print("Enter the correct index (1 or 2)")
                print(f"Enter the correct index (1 to {len(df)})")
    else:
        print("Empty plan to edit")

#Main menu
while True:
    print("What would you like to do today?")
    print("1. Today's Schedule\n2. Add Schedule\n3. Reset Schedule\n4. Edit Schedule")
    index = input("Input by index: ")
    if index.isdigit():
        index = int(index)
        if index == 1:
            FirstMenu()
        elif index == 2:
            SecondMenu()
        elif index == 3:
            ThirdMenu()
        elif index == 4:
            FourthMenu()
        else:
            print("error: invalid index number inputted")
        print("\n")
    else:
        print("error: use the index number to access")