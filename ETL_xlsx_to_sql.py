import pandas as pd
import datetime
import numpy as np
import mysql.connector
import csv
import os
import requests
from sqlalchemy import create_engine
import pyodbc

def read_source():
    
    val = input("\nPlease enter the destination of the excel file along with filename & extension:\n")
    sheet=input("\nEnter the sheet name: ")
    file=pd.read_excel(val,sheet_name=sheet)
    print(file)

if __name__ == "__main__":
    print("Hello user!\nHow can I help you with data today?:-")
    print("\n1. Read data from source")
    print("\n2. Write data to target")
    print("\n3. Read data from source")
    read_source()


















#engine = create_engine(r'postgresql://posgres:akshansh2001@127.0.0.1:5433/retail_etl', echo = True)

# prod1 = pd.read_excel(r'C:\Users\saksh\Desktop\Akshansh\Coding\Github\Retail-etl\Product details.xlsx',sheet_name="Sheet1")
# trans= pd.read_excel(r'C:\Users\saksh\Desktop\Akshansh\Coding\Github\Retail-etl\Transaction details.xlsx',sheet_name="Sheet1")

# df=pd.merge(trans,prod1)
# #print(df)

#trans.to_sql('transactions',engine,if_exists='replace')
# filename="Transaction details.xlsx"
# def extract():
#     try:
#         directory = dir
#         # iterate over files in the directory
#         for filename in os.listdir(directory):
#             #get filename without ext
#             file_wo_ext = os.path.splitext(filename)[0]
#             # only process excel files
#             if filename.endswith(".xlsx"):
#                 f = os.path.join(directory, filename)
#                 # checking if it is a file
#                 if os.path.isfile(f):
#                     df = pd.read_excel(f)
#                     # call to load
#                     load(df, file_wo_ext)
#     except Exception as e:
#         print("Data extract error: " + str(e))

# #load data to postgres
# def load(df, tbl):
#     try:
#         rows_imported = 0
#         engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
#         print(f'importing rows {rows_imported} to {rows_imported + len(df)}... ')
#         # save df to postgres
#         df.to_sql(f"stg_{tbl}", engine, if_exists='replace', index=False)
#         rows_imported += len(df)
#         # add elapsed time to final print out
#         print("Data imported successful")
        
#     except Exception as e:

#         print("Data load error: " + str(e))

# try:
#     #call extract function
#     df = extract()
# except Exception as e:
#     print("Error while extracting data: " + str(e))




