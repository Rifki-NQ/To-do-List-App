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
    if df.empty:
        print("Empty plan")
    else:
        print(df)

def SecondMenu():
    plan = input("Enter the plan: ")
    while True:
        time = input("Enter the time: ")
        #check if the time is digit and has length of 4
        if time.isdigit() and len(time) == 4:
            #formats the inputted time with string slicing
            time = f"{time[:2]}:{time[2:]}"
            #tells python to use the global df variable
            global df
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

#Open main menu
print("What would you like to do today?")
print("1. Today's Schedule\n2. Add Schedule\n3. Reset Schedule\n4. Edit Schedule")

#First menu, show today's schedule
while True:
    index = input("Input by index: ")
    if index.isdigit():
        index = int(index)
        if index == 1:
            FirstMenu()
        elif index == 2:
            SecondMenu()
        else:
            print("error: invalid index number inputted")
    else:
        print("error: use the index number to access")