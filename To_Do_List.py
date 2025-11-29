import os
import pandas as pd

#helper function for reading the file
def read():
    #try reading the csv
    try:
        df = pd.read_csv("lists.csv")
        return df
    #add the headers if the file is completely empty
    except:
        df = pd.DataFrame(columns=["time", "plan"])
        df.to_csv("lists.csv", index=False)
        df = pd.read_csv("lists.csv")
        return df

#helper function for reading the plan
def showplan():
    df = read()
    df.index = [f"Plan {i + 1}. " for i in range(len(df))]
    print("<------------------------>")
    print(df)
    print("<------------------------>")

#Show today's plan
def FirstMenu():
    df = read()
    if df.empty:
        print("- Empty plan for today")
    else:
        showplan()

#Add new plan
def SecondMenu():
    df = read()
    plan = input("- Enter the plan: ")
    while True:
        time = input("- Enter the time: ")
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
            print("- New plan created! ")
            break
        #return error if the inputted time is digits but the length is not 4
        elif time.isdigit():
            print("-- error: use 4 digits of hour and minute (for example 1200 = 12:00)")
        #return error if the inputted time is not only in digits
        else:
            print("-- error: use digits for the time")

#Delete certain plan
def ThirdMenu():
    df = read()
    #stop the function here if the plan is empty
    if df.empty:
        print("- Empty plan to delete!")
        return
    showplan()
    index = input("- Enter which plan to delete (by index): ")
    if index.isdigit() and int(index) > 0 and int(index) <= len(df):
        #reset index of plans
        df.reset_index(drop=True, inplace=True)
        #delete plan with resetted index
        df.drop(index=int(index)-1, inplace=True)
        df.to_csv("lists.csv", index=False)
        print(f"- Plan no. {index} deleted!")
    elif index.isdigit():
        if len(df) == 1:
            print("-- error: enter the correct index (1)")
        elif len(df) == 2:
            print("-- error: enter the correct index (1 or 2)")
        else:
            print(f"-- error: enter the correct index (1 to {len(df)})")
    else:
        print("-- error: use digits for the index!")

#Reset all plan
def FourthMenu():
    df = read()
    if df.empty:
        print("- Already empty plan!")
    else:
        #rewrite the data to headers only
        df = pd.DataFrame(columns=["time", "plan"])
        #save the file
        df.to_csv("lists.csv", index=False)
        print("- plan resetted!")

#Edit certain plan
def FifthMenu():
    df = read()
    if not df.empty:
        showplan()
        while True:
            df = read()
            index = input("- Select which plan you want to edit (by index): ")
            if index.isdigit() and int(index) > 0 and int(index) <= len(df):
                #check the validity of the inputted time then formats it
                while True:
                    time = input("- Enter the new time: ")
                    if time.isdigit() and len(time) == 4:
                        time = f"{time[:2]}:{time[2:]}"
                        break
                    #error if the inputted time is less than o and more than 4 digits
                    elif time.isdigit() and not len(time) == 4:
                        print("-- error: use 4 digits of hour and minute (for example 1200 = 12:00)")
                    #error if the inputted time is not digits only
                    else:
                        print("-- error: use digits for the time")
                plan = input("- Input the plan: ")
                #change the value of inputted digits with new plan
                df.loc[int(index) - 1] = [time, plan]
                df.to_csv("lists.csv", index=False)
                print("- Success!")
                break
            elif index.isdigit():
                if len(df) == 1:
                    print("-- error: enter the correct index (1)")
                elif len(df) == 2:
                    print("-- error: enter the correct index (1 or 2)")
                else:
                    print(f"-- error: enter the correct index (1 to {len(df)})")
            else:
                print("-- error: use digits for the index!")
    else:
        print("- Empty plan to edit!")

#Main menu
while True:
    print("What would you like to do today?")
    print("1. Today's plan\n2. Add plan\n3. Delete plan\n4. Reset plan\n5. Edit plan")
    index = input("- Input by index (select q for quit): ")
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
        elif index == 5:
            FifthMenu()
        else:
            print("-- error: invalid index number inputted")
        print("<-------------------------------------------->")
    elif index.lower() == "q":
        break
    else:
        print("-- error: use the index number to access")