import pandas
import numpy as np
import scipy
import pprint
import matplotlib.pyplot as plt
import sympy.plotting as tplt

data=open('FeedGrains.csv', 'r')

df=pandas.DataFrame.from_csv(data)

cropYear={}
for index, row in df.iterrows():
    if row['SC_GroupCommod_Desc'] == 'Corn':
        if row['Year_ID'] in cropYear.keys():
            cropYear[row['Year_ID']]=cropYear[row['Year_ID']]+ row['Amount']
        else:
            cropYear[row['Year_ID']] = row['Amount']
            
pprint.pprint(zip(cropYear.keys(),cropYear.values()))
plt.plot(cropYear.keys(),cropYear.values(), linewidth=4.0)
plt.ylabel('Year', fontsize=17)
plt.xlabel('Busshels Produced', fontsize=17)
plt.title('Corn Production Over Time', fontsize=22)
plt.show()
#np.histogram(cropYear.keys(),cropYear.values())
#pprint.pprint(cropYear)
