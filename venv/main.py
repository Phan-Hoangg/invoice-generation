import pandas as pd
import glob

filepaths = glob.glob(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App4-invoice-generation\invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)