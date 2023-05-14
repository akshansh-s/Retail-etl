import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import json
import csv
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
    val = input("\nPlease enter the destination of the data file along with filename & extension:\n")
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
    #join_choice=int(input("What is"))
    common_col=input("Enter the common key column name: ")
    ff=pd.merge(file1,file2,on=common_col)
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
        convert_output=rs.to_json(orient='records')
        print(convert_output)
        print("Want to save the file?\n1. Yes\t2. No\n")
        c1=int(input())
        if(c1==1):
            filename = input("Enter filename: ")+".json"
            with open(filename, "w") as file:
                # write the data to the JSON file
                json.dump(convert_output, file)
                print(f"Data written to {filename} successfully.")

    elif(c==2):
        convert_output=rs.to_csv(index=False)
        print(convert_output)
        print("Want to save the file?\n1. Yes\t2. No\n")
        c1=int(input())
        if(c1==1):
            filename = input("Enter filename: ")+".csv"
            with open(filename, 'w', newline='') as file:

                # create a CSV writer object
                writer = csv.writer(file)

                # write the data to the CSV file
                writer.writerows(convert_output)

                print(f"Data written to {filename} successfully.")
    else:
        print("\nWrong input")

def clean(rs):
    duplicate_rows = rs[rs.duplicated()]
    duplicate_rows.to_excel('duplicates.xlsx', index=False)
    rs = rs.drop_duplicates()


def filter(rs):
    ch=1
    print("\nFilter:")
    print("1. Less than")
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

def Missing(rs):
    missing_cols = rs.isnull().sum()[rs.isnull().sum() > 0]
    print(missing_cols)
    
def Missing(rs):
    missing_cols = rs.isnull().sum()[rs.isnull().sum() > 0]
    print(missing_cols)
    
def Missing_data(rs):
    missing_data = rs.isnull()
    for column in missing_data.columns.values.tolist():
      print(column)
      print(missing_data[column].value_counts())
      print("")
    
    
def rescale_data(rs):

   # This function rescales the values of a column or set of columns to a new range.
    columns = rs['Sales_Amount']
    new_min = float(input("Please enter your new_min: "))
    new_max = float(input("Please enter your new_max: "))
    old_min = rs[columns].min()
    old_max = rs[columns].max()
    rs[columns] = (rs[columns] - old_min) * (new_max - new_min) / (old_max - old_min) + new_min
    rescaled_rs = rs[columns]
    '''
    rescaled_rs = rs.copy()
    for column in columns:
        rescaled_rs[column] = ((rs[column] - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
    '''
    return rescaled_rs
    
def describe(rs):
    """
    Return a DataFrame containing statistics of the input DataFrame df.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to describe.

    Returns:
    pandas.DataFrame: A DataFrame containing statistics of the input DataFrame df.
    """
    print(rs.describe())
    #num_cols = rs.select_dtypes(include=[np.number]).columns
    #stats = rs['count'] = stats.loc['count'].astype(int)
    #stats.loc['missing'] = rs.isna().sum()
    #stats.loc['missing_pct'] = rs.isna().mean() * 100
   # return stats
def pivot_data(rs):
    
    
    index_column = input("Please enter your index_column: ")
    columns_column = input("Please enter your columns_column: ")
    values_column = input("Please enter your values_column: ")
    '''
    This function pivots a DataFrame from long to wide format.
    '''
    pivoted_rs = rs.pivot(index=index_column, columns=columns_column, values=values_column).reset_index()
    
    return pivoted_rs

def merge_names(rs):
    rs['name'] = rs['first_name'] + ' ' + rs['last_name']
    print(rs)
    return rs

def lookup(dataframe):
    """
    Searches for data in a DataFrame based on user-defined lookup conditions and returns the corresponding values in a specified column.
    """

    lookup_column = input("Enter the name of the column containing the lookup values: ")
    condition_type = input(f"Enter the data type of the lookup condition (e.g., 'int', 'float', 'str'): ")

    if condition_type == 'int':
        condition = int(input("Enter the lookup condition (integer): "))
    elif condition_type == 'float':
        condition = float(input("Enter the lookup condition (float): "))
    elif condition_type == 'str':
        condition = input("Enter the lookup condition (string): ")
    else:
        print("Invalid data type entered. Please try again.")
        return

    return_column = input("Enter the name of the column containing the values to return: ")

    result = dataframe.loc[dataframe[lookup_column] == condition, return_column]
    print(result)
    return result

def fill_missing_values(df):
    print("\nColumns with missing values:")
    missing_cols = df.isnull().sum()[df.isnull().sum() > 0]
    print(missing_cols)

    print("\nChoose a method for filling missing values:")
    print("1. Fill with a specific value")
    print("2. Fill using the mean value of the column")
    print("3. Fill using the median value of the column")
    print("4. Fill using the mode value of the column")
    print("5. Forward fill (use the previous row value)")
    print("6. Backward fill (use the next row value)")

    choice = int(input())

    if choice == 1:
        value = input("Enter the specific value to fill missing data: ")
        df.fillna(value, inplace=True)
    elif choice == 2:
        for col in missing_cols.index:
            df[col].fillna(df[col].mean(), inplace=True)
    elif choice == 3:
        for col in missing_cols.index:
            df[col].fillna(df[col].median(), inplace=True)
    elif choice == 4:
        for col in missing_cols.index:
            df[col].fillna(df[col].mode()[0], inplace=True)
    elif choice == 5:
        df.fillna(method='ffill', inplace=True)
    elif choice == 6:
        df.fillna(method='bfill', inplace=True)
    else:
        print("Invalid choice. Please try again.")

    print("\nMissing values filled successfully.")
    return df


if __name__ == "__main__":
    choice = 1

    while choice!=20:
        print("\nHello user!\nHow can I help you with data today?:-")
        print("\n1. Read data from source")
        print("\n2. Write data to target")
        print("\n3. Aggregate data of single column")
        print("\n4. Join data")
        print("\n5. Convert into JSON/CSV")
        print("\n6. Clean Data")
        print("\n7. Filter Data (based on Sales Amount)")
        print("\n8. Normalize data[0-1]")
        print("\n9. Sort data")
        print("\n10. Plot bar graph")
        print("\n11. Plot Line Graph")
        print("\n12. No of Missing Values")
        print("\n13. The missing data information ")
        print("\n14. Rescale_data ")    
        print("\n15. Statistics of data")
        print("\n16. Pivots a DataFrame from long to wide format.")
        print("\n17. Merging two columns")
        print("\n18. Lookup")
        print("\n19. Handle missing values")
        print("\n20. Exit\n")

        choice=int(input())
        if(choice==1):
            rs = read_source()

        elif(choice==2):
            if 'rs' in locals() or 'rs' in globals():
                write_target(rs)
            else:
                rs=read_source()
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
            if 'rs' in locals() or 'rs' in globals():
                convert(rs)
            else:
                rs=read_source()
                convert(rs)

        elif(choice==6):
            if 'rs' in locals() or 'rs' in globals():
                clean(rs)
                print("\nThe data has been cleaned\n")
            else:
                rs=read_source()
                clean(rs)
                print("\nThe data has been cleaned\n")


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

        elif(choice==12):
            Missing(rs)
            
        elif(choice==13):
            Missing_data(rs)
                
        # elif(choice==14):
        #     rescale_data(rs)  
            
        elif(choice==15):
            describe(rs)
            
        # elif(choice==16):
        #     pivot_data(rs)

        elif(choice==17):
             merge_names(rs)
        
        elif(choice==18):
            if 'rs' in locals() or 'rs' in globals():
                lookup(rs)
            else:
                rs=read_source()
                lookup(rs)
        
        elif(choice==19):
            if 'rs' in locals() or 'rs' in globals():
                fill_missing_values(rs)
            else:
                rs=read_source()
                fill_missing_values(rs)               
        else:
            quit()