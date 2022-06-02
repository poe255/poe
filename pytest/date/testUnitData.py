from openpyxl import Workbook
from index import lendemain
import pytest
import openpyxl


def test_00():
    # Create a Workbook on Excel:
    wb = Workbook()
    wb = openpyxl.load_workbook('Data.xlsx')
    sheet = wb.active
    for row in sheet:
      for cell in row:
        if cell.column == 1 :
            p1 = cell.value
        if cell.column == 2 :
            p2 = cell.value
        if cell.column == 3 :
            p3 = cell.value
        if cell.column == 4 :
            p4 = cell.value
        if cell.column == 5 :
            p5 = cell.value
        if cell.column == 6 :
            p6 = cell.value
      assert lendemain(p1,p2,p3) == [p4,p5,p6]
    wb.close()

