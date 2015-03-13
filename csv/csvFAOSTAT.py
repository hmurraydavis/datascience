import pandas
import numpy as np
import scipy
import pprint
import matplotlib.pyplot as plt
import sympy.plotting as tplt
import pylab as P

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
    return cropYear


def cropScatterplotByYear(cropYear, crop):
    plt.plot(cropYear.keys(),cropYear.values(), 'r*', linewidth=4.0)
    plt.xlabel('Year', fontsize=17)
    plt.ylabel('Tonnes Produced', fontsize=17)
    plt.title(crop+' Production Over Time', fontsize=22)
    plt.show()


def makeHistogramByCrop(yearList, cropYear, crop):
    bins=[]
    crops=[]
    years=[]
    for year in yearList:
        years.append(yearList[year])
        crops.append(cropYear[yearList[year]])
###    for year in yearList.values():
###        if (year%5) == 0:
###            bins.append(year)
    pprint.pprint(zip(years,crops))
    years=np.array(years)
    crops=np.array(crops)
    n, bins, patches = P.hist(years, crops, normed=1, histtype='bar', rwidth=0.8)
    P.show()
    
def cropScatterplotByYearLinFit(cropYear, crop):
    x=cropYear.keys(); y=cropYear.values()
    plt.plot(x,y, 'r*', linewidth=4.0)
    m,b = np.polyfit(x, y, 1) 
    plt.plot(x, m*x+b, 'k',linewidth=3.0) 
    plt.xlabel('Year', fontsize=17)
    plt.ylabel('Tonnes Produced', fontsize=17)
    plt.title(crop+' Production Over Time', fontsize=22)
    plt.show()
    
    
def runScatterForCropsWeCareAbout():
    cropsWeCareAbout = ['Corn', 'Cotton lint', 'Soybeans', 'Wheat']
    yearList = buildYearList()
    resultsDict={}
    for crop in cropsWeCareAbout:
        cropYear = sumYieldYears(yearList, crop=crop)
        cropScatterplotByYear(cropYear, crop)
        resultsDict[crop] =cropYear
    return resultsDict


def histTest():
    mu, sigma = 200, 25
    x = mu + sigma*P.randn(10000)
    bins = [100,125,150,160,170,180,190,200,210,220,230,240,250,275,300]
    # the histogram of the data with histtype='step'
    n, bins, patches = P.hist(x, bins, normed=1, histtype='bar', rwidth=0.8)
    # now we create a cumulative histogram of the data
    P.figure()
    P.show()
    
    
#parseOutCountryData()
df = makeFAOSTATdf(region='us')
#runScatterForCropsWeCareAbout()

##cropYear = sumYieldYears(yearList, crop='Spinach')
##cropScatterplotByYear(cropYear, 'Spinach')

yearList = buildYearList()        
cropYear = sumYieldYears(yearList, crop='Spinach')
#makeHistogramByCrop(yearList, cropYear, 'Spinach')
#cropScatterplotByYearLinFit(cropYear,  'Spinach')


