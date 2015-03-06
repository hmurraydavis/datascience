'''
README:
xlrd installation instructions:
sudo apt-get install python-xlrd

Save sheet as sheetname (ending in .xls - convert if necessary) in folder
'''

import csv
import xlrd
import pandas.io.excel as io
import pandas as p


# look through the df's column names for a certain search
def grep(search, df):
	for val in df.columns.values:
		if search in val:
			print val

# Known issues: Table 4 (multiple entries per year...sum?)
def readJoin(bookname='fertilizeruse.xls'):
	dfs = readDict(bookname)
	keys = dfs.keys()

	dfj = dfs['Table1']

	while len(keys) > 0:
		key = keys.pop()
		if key in 'Table4 Table7':
			df = dfs[key]
			dfj = df.join(dfj, on='year', rsuffix='_r')
			#if key == 'Table7':
			#	print dfj.ure_dol

	#print dfj.ure_dol

	# drop extra columns from join
	#for val in dfj.columns.values:
	#	if '_r' in val:
	#		dfj.drop(val, axis=1, inplace=True)

	return dfj


''' master function - builds dict w/ key = sheetname, val = df '''
def readDict(bookname='fertilizeruse.xls'):
	# setup
	# ...open book
	book = xlrd.open_workbook(bookname)

	# ...read Table 1-8 newnames from csv
	newnames_rowperyear_csvreader = csv.reader(open('codebook/rowPerYearCols.csv', 'rb'))
	newnames_rowperyear = []
	for row in newnames_rowperyear_csvreader:
		newnames_rowperyear.append(row)

	# ...read Table 9-end prefixes from csv
	prefixes_rowperstate_csvreader = csv.reader(open('codebook/rowPerStatePrefixes.csv', 'rb'))
	prefixes_rowperstate = []
	for prefix in prefixes_rowperstate_csvreader:
		prefixes_rowperstate.append(prefix)

	# ...read state abbreviations from csv
	state_abbrevs_csvreader = csv.reader(open('codebook/states.csv', 'rb'))
	state_abbrevs = {}
	for abbrev in state_abbrevs_csvreader:
		state_abbrevs[abbrev[0]] = abbrev[1].lower()

	# read sheets
	dfs = {}
	for i in range(len(book.sheets())): 
		sheet = book.sheet_by_index(i)
		if (i in range(0,8)): # Tables 1-8
			df = rowPerYear(bookname, sheet.name, newnames_rowperyear[i])
		else:
			df = rowPerState(bookname, sheet.name, prefixes_rowperstate[i-8][0], state_abbrevs)

		dfs[sheet.name] = df
		#if sheet.name == 'Table7':
		#	print df.ure_dol

	return dfs


''' convert sheet in Tables 1-8 to dataframe'''
def rowPerYear(bookname, sheetname, newnames):
	# read to dataframe
	# header = 3 -> use Row 4 (indexed from 1) as the column names
	df = io.read_excel(bookname, sheetname=sheetname, header=3)         

	# build map from old to new column name
	renameMap = {}
	for i, val in enumerate(df.columns.values):
		newname = newnames[i].strip()
		if (newname == 'na'):
			df.drop(val, axis=1, inplace=True) # drop untitled cols
		else:
			renameMap[val] = newname


	# perform rename, drop rows w/ empty year, & return
	df.rename(columns=renameMap, inplace=True)
	df.dropna(inplace=True)
	df.index = df.year
	return df


''' convert sheet in Tables 9-32 to dataframe '''
def rowPerState(bookname, sheetname, prefix, abbrevs):
	# read to dataframe
	# header = 2 -> use Row 3 (indexed from 1) as the column names
	df = io.read_excel(bookname, sheetname=sheetname, index_col = 0, header=2)
	for val in df.columns.values:
		if (type(val) != int and 'Unnamed' in val):
			df.drop(val, axis=1, inplace=True)

	# rename empty rows before transposing
	newIndex = []
	for i, val in enumerate(df.index):
		if type(val) == float:
			newIndex.append('na')
		else:
			newIndex.append(val)
	series = p.Series(data=newIndex)
	df.index = series

	# transpose dataframe and drop empty cols (previously rows)
	df = df.T
	df.drop('na', axis=1, inplace=True)

	# build map from old to new column name
	renameMap = {}
	for val in df.columns.values:
		if ('/' in val or '=' in val or '(' in val):
			df.drop(val, axis=1, inplace=True) # drop untitled cols
		else:
			renameMap[val] = prefix + abbrevs[val]

	# perform rename
	df.rename(columns=renameMap, inplace=True)

	# copy year (currently index) to its own column
	df['year'] = df.index

	return df