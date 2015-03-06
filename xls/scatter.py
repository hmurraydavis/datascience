import readXls as r
import matplotlib.pyplot as plt

def plot():
	df = r.readJoin()
	#scatter('ure_dol', 'ure_all_ton_us', df)
	scatter('nit_all_ton_us', 'pho_all_ton_us', df)


def scatter(col1, col2, df):
	df.plot(kind='scatter', x=col1, y=col2, color='DarkBlue', label='Group 1')
	plt.savefig('plot2.jpg', format='jpg')