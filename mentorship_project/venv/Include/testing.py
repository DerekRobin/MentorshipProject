import unittest
import pandas as pd
from csv_methods import *

class csv_unittest(unittest.TestCase):

    global FILENAME
    global actual_csv
    global test_csv
    FILENAME = "music.csv"
    actual_csv = read_CSV(FILENAME)
    test_csv = pd.read_csv(FILENAME)

    def test_read_entire_row(self):
        #Arrange
        ROW_VALUE = 0

        #Act
        actual_row = read_entire_row(ROW_VALUE, actual_csv)
        test_row = test_csv.iloc[ROW_VALUE]

        #Assert
        self.assertIs(actual_row.equals(test_row), True)

    def test_read_entire_col_by_integer(self):
        #Arrange
        COL_VALUE = 0

        #Act
        actual_col = read_entire_column_by_integer(COL_VALUE, actual_csv)
        test_col = test_csv.iloc[:,COL_VALUE]

        #Assert
        self.assertIs(actual_col.equals(test_col), True)

    def test_read_entire_col_by_name(self):
        #Arrange
        COL_NAME = "tempo"

        #Act
        actual_col = read_entire_column_by_name(COL_NAME, actual_csv)
        test_col = test_csv.loc[:,COL_NAME]

        #Assert
        self.assertIs(actual_col.equals(test_col), True)

    def test_read_row_col(self):
        #Arrange
        ROW_VALUE = 0
        COL_VALUE = 0

        #Act
        actual_row_col = read_row_col(ROW_VALUE, COL_VALUE,actual_csv)
        test_row_col = test_csv.iat[ROW_VALUE,COL_VALUE]

        #Assert
        self.assertEqual(actual_row_col, test_row_col)

    def test_grab_all_rows_from_specific_column(self):
        #Arrange
        COL_NAME = "artist.name"
        ITEM_TO_SEARCH_FOR =  "Casual"

        #Act
        actual_all_rows = grab_all_rows_from_specific_column(COL_NAME, ITEM_TO_SEARCH_FOR, actual_csv)
        test_all_rows = test_csv[test_csv[COL_NAME].str.contains(ITEM_TO_SEARCH_FOR)]

        #Assert
        self.assertIs(actual_all_rows.equals(test_all_rows), True)


if __name__ == '__main__':
    unittest.main()