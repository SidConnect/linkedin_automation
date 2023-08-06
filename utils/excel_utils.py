import pandas as pd
from openpyxl import load_workbook


def read_excel_data(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name)
        return df
    except Exception as e:
        raise Exception(f"Error occurred while reading data from excel: {str(e)}")


def write_to_excel(df, file_path, sheet_name):

    book = load_workbook(file_path)
    sheet = book[sheet_name]

    df.to_excel(file_path, sheet_name, index=False)
