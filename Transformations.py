import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

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


def clean(rs):
    duplicate_rows = rs[rs.duplicated()]
    duplicate_rows.to_excel('duplicates.xlsx', index=False)
    rs = rs.drop_duplicates()


def filter(rs):
    ch=1
    print("Filter:")
    print("1.Less than")
    print("2. Greater than")
    ch=int(input())

    if (ch==1):
        sales = float(input('\nEnter Sales Amount: '))
        sales_amount = rs[(rs['Sales_Amount'] < sales)] 

    elif (ch==2):
        sales = float(input('\nEnter Sales Amount: '))
        sales_amount = rs[(rs['Sales_Amount'] > sales)] 

    else:
        pass
    
    val = input("\nPlease enter the destination of the excel file along with filename & extension:\n")
    sheet = input("\nEnter the sheet name: ")
    sales_amount.to_excel(val, sheet_name=sheet)
    

def normalize(rs):
    rs_min_max_scaled = rs.copy()
  
    # apply normalization techniques
    #for column in rs_min_max_scaled.columns:
        #if rs[column].dtype.kind in 'biufc':
    rs_min_max_scaled['Sales_Amount'] = (rs_min_max_scaled['Sales_Amount'] - rs_min_max_scaled['Sales_Amount'].min()) / (rs_min_max_scaled['Sales_Amount'].max() - rs_min_max_scaled['Sales_Amount'].min())    
  
    # view normalized data
    #print(rs_min_max_scaled)
    val = input("\nPlease enter the destination of the excel file along with filename & extension:\n")
    sheet = input("\nEnter the sheet name: ")
    rs_min_max_scaled.to_excel(val, sheet_name=sheet)
    return rs_min_max_scaled

def sort(rs):
    Final_result = rs.sort_values('Sales_Amount')
    print(Final_result)


def bar_graph(rs):

    sales_demo=rs.groupby([rs.Date.dt.year, rs.Date.dt.month]).aggregate({"Sales_Amount":"sum"})
    sales_demo.plot(kind='bar')
    plt.xticks(rotation=45)
    plt.show()


def line_graph(rs):
    sales_demo=rs.groupby(["Date"]).aggregate({"Sales_Amount":"sum"})
    sales_demo.plot()
    plt.xticks(rotation=45)
    plt.show()



if __name__ == "__main__":
    choice = 1

    while choice!=15:
        print("\nHello user!\nHow can I help you with data today?:-")
        print("\n1. Read data from source")
        print("\n2. Write data to target")
        print("\n3. Aggregate data")
        print("\n4. Join data")
        print("\n5. Convert into JSON/CSV")
        print("\n6. Clean Data")
        print("\n7. Filter Data (based on Sales Amount)")
        print("\n8. Normalize data[0-1]")
        print("\n9. Sort data")
        print("\n10. Plot bar graph")
        print("\n11. Plot Line Graph")
        print("\n15. Exit\n")

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

        elif(choice==6):
            clean(rs)

        elif(choice==7):
            filter(rs)

        elif(choice==8):
            normalized = normalize(rs)

        elif(choice==9):
            sort(rs)

        elif(choice==10):
            bar_graph(rs)

        elif(choice==11):
            line_graph(rs)
        
        else:
            quit()