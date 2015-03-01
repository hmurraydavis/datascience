'''
README:
xlrd installation instructions:
    sudo apt-get install python-xlrd
    
Save sheet as sheetname (ending in .xls - convert if necessary) in folder
'''

import csv
import xlrd
import pandas.io.excel as io


def usageExample():
    dfs = read()

    df1 = dfs['Table1']
    #print df1.columns.values
    print 'Example mean: ', df1.tons_nitrogen.mean()
    print '---'

    df9 = dfs['Table9']
    print 'Example value_counts:'
    print df9.Illinois.value_counts().sort_index()


''' master function - builds dict w/ key = sheetname, val = df '''
def read(bookname='fertilizeruse.xls'):
    # open book
    book = xlrd.open_workbook(bookname)

    # setup - read Table 1-8 newnames from csv
    newnames_csvreader = csv.reader(open('rowPerYearCols.csv', 'rb'))
    newnames = []
    for row in newnames_csvreader:
        newnames.append(row)

    # read sheets
    dfs = {}
    for i in range(len(book.sheets())): 
        sheet = book.sheet_by_index(i)
        if (i in range(0,8)): # Tables 1-8
            df = rowPerYear(bookname, sheet.name, newnames[i])
        else:
            df = rowPerState(bookname, sheet.name)
        
        dfs[sheet.name] = df

    return dfs


''' convert sheet in Tables 1-8 to dataframe'''
def rowPerYear(bookname, sheetname, newnames):
    # read to dataframe
    # header = 3 -> use Row 4 (indexed from 1) as the column names
    df = io.read_excel(bookname, sheetname=sheetname, header=3)         

    # build map from old to new column name
    renameMap = {}
    for i, val in enumerate(df.columns.values):
        if ('Unnamed' in val):
            df.drop(val, axis=1, inplace=True) # drop untitled cols
        renameMap[val] = newnames[i].strip()

    # perform rename, drop rows w/ empty year, & return
    df.rename(columns=renameMap, inplace=True)
    df.dropna(inplace=True)
    return df


''' convert sheet in Tables 9-32 to dataframe '''
def rowPerState(bookname, sheetname):
    # read to dataframe
    # header = 2 -> use Row 3 (indexed from 1) as the column names
    df = io.read_excel(bookname, sheetname=sheetname, index_col = 0, header=2)
    for val in df.columns.values:
        if (type(val) != int and 'Unnamed' in val):
            df.drop(val, axis=1, inplace=True)
    df = df.T
    #df['year'] = df.index
    
    # TODO: still some nan columns; clear out if time
    #print df.columns.values
    
    return df