import pandas
import numpy as np
import scipy
import pprint
import matplotlib.pyplot as plt
import sympy.plotting as tplt
import pylab as P
import scipy.stats as stats

def parseOutCountryData(country="United States of America", fileout = "USData.csv", filein = 'Production_Crops_E_Americas_1.csv'):
    '''Parse out data for a specific country into a seprate file so the program doesn't have to craw throguh all 
    the data. 
    
    NOTE: opens file in append mode, so if you call this repetelt, you'll have the data for the country in question
    many times in the same file (unless you change the file name. This probably isn't what you want. To avoid this,
    rm the file before running this function again.'''
    FullData = open(filein, 'r')
    with open(fileout, "a") as usadata:
        for line in FullData: 
            if country in line: 
                usadata.write(line)
            if 'Country' in line:
                usadata.write(line)
        

def makeFAOSTATdf(region='short'):
    '''Make a pandas dataframe from the data in a given region (CSV file)'''
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
    '''Constructs & returns a dictionary with Y[year] as the key and the year as the value for working with the 
    FAOSTAT dataframe.'''
    yearList = {}
    for year in range(start,end):
        yearStr='Y'+str(year)
        yearList[yearStr]= year
    return yearList


def sumYieldYears(yearList, crop='Corn'):
    '''Returns a dictionary of production data for a given crop for a given set of years.'''
    cropDenotation='Item'
    cropYear={}
    for index, row in df.iterrows():
        if (row[cropDenotation] == crop) and (row['Element']=='Production'):
            for year in yearList:
                cropYear[yearList[year]] = row[year]
    return cropYear


def getProductionCertainYear(yearList, year=2013, crop='Asparagus'):
    '''Returns a dictionary of production data for a given crop for a given  year.'''
    cropDenotation='Item'
    cropYear={}
    production = {}
    for index, row in df.iterrows():
        if row['Element'] == 'Production':
            if row['Item'] in production:
                production[row['Item']] = production[row['Item']] + row['Y'+str(year)]
            else: production[row['Item']] = row['Y'+str(year)]
#            pprint.pprint(production)
    return production
    
def derivativesOverTime(yearList, crop='Asparagus'):
    cropDenotation = 'Item'
    last=0;
    derivs = []
    for index, row in df.iterrows():
        if (row[cropDenotation] == crop) and (row['Element']=='Production'):
            for year in yearList.keys():
                if last > 0:
                    derivs.append(row[year]-last)
                else: last=row[year]
#    plt.plot(derivs, linewidth=4.0)
#    plt.xlabel('Years Since ' + str(min(yearList.values())), fontsize=17)
#    plt.ylabel('Derivative of Tonnes Produced', fontsize=17)
#    plt.title(crop+' Production Deratives Over Time', fontsize=22)
#    plt.show()
    return derivs
            

def cropScatterplotByYear(cropYear, crop):
    '''Makes a cscatterplot for a given dataset'''
    plt.plot(cropYear.keys(),cropYear.values(), 'r*', linewidth=4.0)
    plt.xlabel('Year', fontsize=17)
    plt.ylabel('Tonnes Produced', fontsize=17)
    plt.title(crop+' Production Over Time', fontsize=22)
    plt.show()


def makeHistogramByCrop(yearList, cropYear, crop):
    '''Plot a histogram like thing which shows the yield as bars in a bar chart.'''
    bins=[]
    crops=[]
    years=[]	
    for year in yearList:
        years.append(yearList[year])
        crops.append(cropYear[yearList[year]])
    zippy = sorted(zip(years, crops), key=lambda p: p[0])
    years = np.array([y for (y, x) in zippy])
    crops = np.array([x for (y, x) in zippy])
    
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.bar(range(len(years)), crops)
    ax.set_xticks(np.arange(len(years)))
    ax.set_xticklabels(years, rotation=90)
    plt.xlabel('Year', fontsize=17)
    plt.ylabel('Tonnes Produced', fontsize=17)
    plt.title(crop+' Production Over Time', fontsize=22)
    plt.show()
    '''
    print(years)
    print(crops)
    #n, bins, patches = plt.hist(crops, bins=years, normed=1, histtype='bar', rwidth=0.8)
    #n, bins, patches = plt.hist(crops, bins=100, normed=1, histtype='bar', rwidth=0.8)
    plt.plot(years, crops)
    plt.show()'''
    

def makeHistogramProductionAmt(cropYear, crop):
    n, bins, patches = plt.hist(cropYear.values(), bins=20)
    plt.xlabel('Tonnes Produced', fontsize=17)
    plt.ylabel('Number of Years Produced from ' + str(min(cropYear.keys())) + ' to ' + str(max(cropYear.keys())), fontsize=17)
    plt.title(crop+' Production Frequency', fontsize=22)
    plt.show()
    

def makeCDFCropProductionValues(cropYear, crop):
    hist, bin_edges = np.histogram(cropYear.values(), bins=30, density=False)
    CDF = np.cumsum(hist)
    CDF = np.insert(CDF, 0, 0)
    xlab = bin_edges
    plt.plot(xlab, CDF, linewidth=4.0)
    plt.xlabel('Tonnes Produced', fontsize=17)
    plt.ylabel('Cumulative Production Values by Year From ' + str(min(cropYear.keys())) + ' to ' + str(max(cropYear.keys())), fontsize=17)
    plt.title(crop+' Production CDF', fontsize=22)
    plt.show()


def cropScatterplotByYearLinFit(cropYear, crop):
    #TODO: Fix error yielded
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
    
    
def makePMF(cropYear):
    from scipy.stats import binom
    import matplotlib.pyplot as plt2
    fig, ax = plt2.subplots(1, 1)
    n=cropYear.keys(); p=cropYear.values()
    scipy.stats.rv_discrete.pmf(n)
    #x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
###    x=n; y=p;
###    ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
###    ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
###    plt2.show()
#    rv = binom(n, p)
#    ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
#    ax.legend(loc='best', frameon=False)
#    plt2.show()
    
def getSumaryStatistics(cropYear, crop):
    var = np.var(cropYear.values()); print crop, ' production variance is: ',var, ' tonnes'
    std = np.std(cropYear.values()); print crop, ' production standard deviation is: ',std, ' tonnes'
    
#parseOutCountryData()
df = makeFAOSTATdf(region='us')
#runScatterForCropsWeCareAbout()
yearList = buildYearList()

#cropYear = sumYieldYears(yearList, crop='Barley')
#cropScatterplotByYear(cropYear, 'Barley')
 
cropYear = sumYieldYears(yearList, crop='Soybeans')
#makeHistogramByCrop(yearList, cropYear, 'Spinach')

#makeHistogramProductionAmt(cropYear, 'Spinach')

makeCDFCropProductionValues(cropYear, 'Spinach')
#cropScatterplotByYearLinFit(cropYear,  'Spinach')
#getSumaryStatistics(cropYear, crop='Soybeans')
#makePMF(cropYear)
#getProductionCertainYear(yearList)

def plotManyCropDerivsOverTime(yearList, crops):
    derivs = {}
    for crop in crops:
        deriv = derivativesOverTime(yearList, crop[0])
        deriv = [x * crop[1] for x in deriv] 
        label = crop[0]+ ' derivitative, scale = '+str(crop[1])
        plt.plot(deriv, linewidth=4, label = label)
        derivs[crop[0]] = deriv
    plt.xlabel('Years since 1961', fontsize=17)
    plt.ylabel('Derivative of Tonnes Produced', fontsize=17)
    plt.title('Crop Production Over Time', fontsize=22)
    plt.legend()
    plt.show()
    return derivs
        
        
#plotManyCropDerivsOverTime(yearList, [('Soybeans', .5), ('Apples', 15), ('Apricots', 600)])    
#makePMF(cropYear)


#    plt.plot(derivs, linewidth=4.0)
#    plt.xlabel('Years Since ' + str(min(yearList.values())), fontsize=17)
#    plt.ylabel('Derivative of Tonnes Produced', fontsize=17)
#    plt.title(crop+' Production Deratives Over Time', fontsize=22)
#    plt.show()

#TODO: 
##PMF
##PDF
