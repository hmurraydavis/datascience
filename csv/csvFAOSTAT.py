import pandas
import numpy as np
import scipy
import pprint
import matplotlib.pyplot as plt
import sympy.plotting as tplt

def parseOutCountryData(country="United States of America", fileout = "USData.csv", filein = 'Production_Crops_E_Americas_1.csv'):
    FullData = open(filein, 'r')
    with open(fileout, "a") as usadata:
        for line in FullData: 
            if country in line: 
                usadata.write(line)
            if 'Country' in line:
                usadata.write(line)
        

def makeFAOSTATdf(region='short'):
    '''Make a pandas dataframe from the data in a given CSV file'''
    if region=='short':
        data=open('FeedGrains.csv', 'r')
    elif region=='middle':
        data=open('FAOSTAT_Full.csv', 'r')
    elif region=='world':
        data=open('full_FAOSTAT.csv', 'r')
    elif region=='us':
        data=open('USData.csv', 'r')
    else: 
        raise Exception("Unknown data form. Please specify your data file with the data key in the function call")
    return pandas.DataFrame.from_csv(data)

def buildYearList(start = 1961, end = 2013):
    yearList = {}
    for year in range(start,end):
        yearStr='Y'+str(year)
        yearList[yearStr]= year
    return yearList

def sumYieldYears(yearList, crop='Corn'):
    cropDenotation='Item'
    cropYear={}
    for index, row in df.iterrows():
        if (row[cropDenotation] == crop) and (row['Element']=='Production'):
            for year in yearList:
                cropYear[yearList[year]] = row[year]
    pprint.pprint(cropYear)
        


#parseOutCountryData()
##cropsWeCareAbout = ['Corn', 'Cotton lint', 'Soybeans', 'Wheat']
df = makeFAOSTATdf(region='us')
yearList = buildYearList()
cropYear = sumYieldYears(yearList, crop='Spinach')

#pprint.pprint(zip(cropYear.keys(),cropYear.values()))
##plt.plot(cropYear.keys(),cropYear.values(), linewidth=4.0)
##plt.ylabel('Year', fontsize=17)
##plt.xlabel('Busshels Produced', fontsize=17)
##plt.title('Corn Production Over Time', fontsize=22)
##plt.show()
#np.histogram(cropYear.keys(),cropYear.values())
#pprint.pprint(cropYear)
