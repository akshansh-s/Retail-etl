import pandas as pd
# import datetime
# import numpy as np
# import mysql.connector
# import csv
# import os
# import requests
# from sqlalchemy import create_engine
# import pyodbc

def read_source():
    val = input("\nPlease enter the destination of the excel file along with filename & extension:\n")
    sheet=input("\nEnter the sheet name: ")
    file=pd.read_excel(val,sheet_name=sheet)
    print(file)
    return file

def write_target(rs):
    val = input("\nPlease enter the destination of the excel file along with filename & extension:\n")
    sheet = input("\nEnter the sheet name: ")
    rs.to_excel(val, sheet_name=sheet)

def aggregate(group_choice):
    grouped_data=rs.groupby(group_choice)
    #print(grouped_data)
    sum_gd=grouped_data["Sales_Amount"].sum()
    print(sum_gd)
    agg_gd=grouped_data.agg({'Sales_Amount':'mean'})
    print("\n",agg_gd)

def joiner(file1,file2):
    ff=pd.merge(file1,file2)
    print(ff)
    print("Want to save the merged table in an excel file?\n1. Yes\t2. No\n")
    c=int(input())
    if(c==1):
        write_target(ff)
    elif(c==2):
        print("Okay")
    else:
        print("\nWrong input")

def convert(rs):
    c=int(input("\nDo you want to convert to: \n1. JSON\n2. CSV\n"))
    if(c==1):
        print(rs.to_json(orient='records'))
    elif(c==2):
        print(rs.to_csv(index=False))
    else:
        print("\nWrong input")

if __name__ == "__main__":
    choice = 1

    while choice!=6:
        print("\nHello user!\nHow can I help you with data today?:-")
        print("\n1. Read data from source")
        print("\n2. Write data to target")
        print("\n3. Aggregate data")
        print("\n4. Join data")
        print("\n5. Convert into JSON/CSV")
        print("\n6. Exit\n")

        choice=int(input())
        if(choice==1):
            rs = read_source()

        elif(choice==2):
            write_target(rs)

        elif(choice==3):
            print("\nGroup data by? (Mention Column Name):\n")
            group_choice=input()
            aggregate(group_choice)
            #grouped_data.to_excel(r"C:\Users\saksh\Desktop\Akshansh\Coding\Github\Retail-etl\Excel dataset\P1.xlsx ",sheet_name="Sheet1")

        elif(choice==4):
            print("\nWhich is the first file?:\n")
            f1=read_source()
            print("\nWhich is the second file?:\n")
            f2=read_source()
            joiner(f1,f2)

        elif(choice==5):
            convert(rs)

        else:
            quit()