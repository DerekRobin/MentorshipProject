import unittest
import pandas as pd

# Method to read entire CSV
#filename: the name of the csv, stored in the same directory as this .py file
def read_CSV(filename):
    df = pd.read_csv(filename)
    return df

#Method to read an entire row
#row: the row you wish to access, must be an integer
#df: the dataframe you wish to search in
def read_entire_row(row, df):
    return df.iloc[row]

#Method to read an entire column
#col_name: the column you wish to access, must be an integer
#df: the dataframe you wish to search in
def read_entire_column_by_integer(col_number, df):
    return df.iloc[:,col_number]

#Method to read an entire column
#col_name: the column you wish to access, must be a string
#df: the dataframe you wish to search in
def read_entire_column_by_name(col_name, df):
    return df.loc[:,col_name]

#Method to read a specific column and row
#row, col: the row, column pair you wish to access
#df: the dataframe you wish to search in
def read_row_col(row, col, df):
    return df.iat[row,col]

#Method to grab all rows from column_name which contains item_to_search_for
#column_name: the name of the column you wish to search
#item_to_search_for: the name of the item which you wish the rows to contain
#return: all rows from column column_name which contain item_tosearch_for
def grab_all_rows_from_specific_column(column_name, item_to_search_for, df):
    return df[df[column_name].str.contains(item_to_search_for)]

#Method to write a new csv file from a dataframe
#df_in: the dataframe which is to be converted to a new csv
#outfile_name: the filename which the new csv will be called
def write_csv(df_in, out_filename):
    df_in.to_csv(out_filename, index = False)

#Method which takes in an array of columns and merges them into a new csv
#columns_to_merge: an array of columns (dataframes) which are to be merged into a new csv
#out_filename: the name of the new csv
def merge_columns_into_csv(columns_to_merge, out_filename):
    new_csv = pd.concat(columns_to_merge, axis = 1, sort = False)
    write_csv(new_csv, out_filename)

def main():
    music_csv = read_CSV("music.csv")
    artist_df = read_entire_column_by_name("artist.name", music_csv)
    duration_df = read_entire_column_by_name("duration", music_csv)
    tempo_df = read_entire_column_by_name("tempo", music_csv)
    title_df = read_entire_column_by_name("title", music_csv)
    year_df = read_entire_column_by_name("year", music_csv)
    frames = [artist_df, duration_df, tempo_df, title_df, year_df]
    new_music_csv = merge_columns_into_csv(frames, "new_music.csv")

if __name__ == '__main__':
    main()