import pandas as pd
def db(data1,data2):
	df=pd.read_excel(data1)
	data =pd.read_excel(data2)
	return df
