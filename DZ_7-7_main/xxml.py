import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import pandas as pd 
from pandas import ExcelFile


def read_file():
    wb = openpyxl.load_workbook('data_file.xlsx')
    data_xlsx = wb['data_list']
    return data_xlsx

def read_file_2():
    pd.read_excel('data_file.xlsx')
    data_xlsx_2 = pd.read_excel('data_file.xlsx')
    return data_xlsx_2




