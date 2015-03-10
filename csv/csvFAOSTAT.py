import pandas
import numpy as np
import scipy
import pprint
import matplotlib.pyplot as plt
import sympy.plotting as tplt

def makeFAOSTATdf(data='short'):
    if data=='short':
        data=open('FeedGrains.csv', 'r')
    elif data=='long':
        data=open('FAOSTAT_Full.csv', 'r')
    else: 
        raise Exception("Unknown data form. Please specify your data file with the data key in the function call")
    return pandas.DataFrame.from_csv(data)

df = makeFAOSTATdf()
cropYear={}
for index, row in df.iterrows():
    if row['SC_GroupCommod_Desc'] == 'Corn':
        if row['Year_ID'] in cropYear.keys():
            cropYear[row['Year_ID']]=cropYear[row['Year_ID']]+ row['Amount']
        else:
            cropYear[row['Year_ID']] = row['Amount']
            
#pprint.pprint(zip(cropYear.keys(),cropYear.values()))
plt.plot(cropYear.keys(),cropYear.values(), linewidth=4.0)
plt.ylabel('Year', fontsize=17)
plt.xlabel('Busshels Produced', fontsize=17)
plt.title('Corn Production Over Time', fontsize=22)
plt.show()
#np.histogram(cropYear.keys(),cropYear.values())
#pprint.pprint(cropYear)
