import readXls as r
import matplotlib.pyplot as plt
import os

def plot():
	df = r.readJoin()
	scatter('ure_dol', 'ure_all_ton_us', df, 'sample1.jpg')
	scatter('nit_all_ton_us', 'pho_all_ton_us', df, 'sample2.jpg')


def scatter(col1, col2, df, filename):
	ensureDir('plots')
	df.plot(kind='scatter', x=col1, y=col2, color='DarkBlue', label='Group 1')
	plt.savefig('plots/' + filename, format='jpg')

def ensureDir(dirname):
	if not os.path.exists(dirname):
		os.makedirs(dirname)