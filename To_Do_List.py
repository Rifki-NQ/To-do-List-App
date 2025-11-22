import os
import pandas as pd

if os.path.getsize("lists.csv") > 0:
    df = pd.read_csv("lists.csv")
else:
    df = pd.DataFrame()
df.index = df.index + 1

def FirstMenu():
    if df.empty:
        print("Empty plan")
    else:
        print(df)

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
        else:
            print("error: invalid index number inputted")
    else:
        print("error: use the index number to access")