import os
import pandas as pd

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
        if time.isdigit():
            df = pd.read_csv("lists.csv")
            newplan = pd.DataFrame([{"time": time, "plan": plan}])
            df = pd.concat([df, newplan], ignore_index=False)
            df.to_csv("lists.csv", index=False)
            break
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