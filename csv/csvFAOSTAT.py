import pandas
import numpy as np
import scipy
import pprint
import matplotlib.pyplot as plt
import sympy.plotting as tplt

def parseOutCountryData(country="United States of America", fileout = "USData.csv", filein = 'Production_Crops_E_Americas_1.csv'):
#United States of America
    FullData = open(filein, 'r')
    with open(fileout, "a") as usadata:
        for line in FullData: 
            if country in line: 
                usadata.write(line)
            
            
#fullDF = pandas.DataFrame.from_csv(FullData)
#with open("USData.csv", "a") as usadata:
#    for index, row in fullDF.iterrows():
#        if row['Country'] == 'United States of America':
#            usadata.write(row)
        

def makeFAOSTATdf(region='short'):
    '''Make a pandas dataframe from the data in a given CSV file'''
    if region=='short':
        data=open('FeedGrains.csv', 'r')
    elif region=='middle':
        data=open('FAOSTAT_Full.csv', 'r')
    elif region=='world':
        data=open('full_FAOSTAT.csv', 'r')
    elif region=='americas':
        data=open('Production_Crops_E_Americas_1.csv', 'r')
    else: 
        raise Exception("Unknown data form. Please specify your data file with the data key in the function call")
    return pandas.DataFrame.from_csv(data)


def sumYieldYears(crop='Corn'):
    cropYear={}
    cropDenotation='Item'
    yearDenotation = 'Year'
    amountDenotation = 'Value'
    for index, row in df.iterrows():
        if row[cropDenotation] == crop:
            if row[yearDenotation] in cropYear.keys():
                cropYear[row[yearDenotation]]=cropYear[row[yearDenotation]]+ row[amountDenotation]
            else:
                cropYear[row[yearDenotation]] = row[amountDenotation]
    return cropYear

##cropsWeCareAbout = ['Corn', 'Cotton lint', 'Soybeans', 'Wheat']
##df = makeFAOSTATdf(region='world')
##cropYear = sumYieldYears()

#pprint.pprint(zip(cropYear.keys(),cropYear.values()))
##plt.plot(cropYear.keys(),cropYear.values(), linewidth=4.0)
##plt.ylabel('Year', fontsize=17)
##plt.xlabel('Busshels Produced', fontsize=17)
##plt.title('Corn Production Over Time', fontsize=22)
##plt.show()
#np.histogram(cropYear.keys(),cropYear.values())
#pprint.pprint(cropYear)
