import pandas as pd
import plotly as py
import plotly.graph_objs as go
from backend.constant import get_prv
reading=pd.read_excel("Datasets/Maroc/accident.xlsx")
read=pd.read_excel("Datasets/Maroc/vehicule.xlsx")
dup=reading.drop_duplicates(subset=['COD_PRV'])
lis= dup['COD_PRV'].tolist()
c=0
labelsint = ['Hors intersection','Intersection en X','Intersection en T','Intersection en Y','Intersection à plus de 4 branches','Giratoire','Place','Passage à niveau','Autre intersection']
labelsAtmosphere= ['Normale','Pluie légère','Pluie forte','Neige - grêle','Brouillard - fumée','Vent fort - tempête','Temps éblouissant','Temps couvert','Autre']
labelscol=['Deux véhicules - frontale','Deux véhicules – par l’arrière','Deux véhicules – par le coté','Trois véhicules et plus – en chaîne','Trois véhicules et plus - collisions multiples','Autre collision','Sans collision']

def stats(i):
	a = reading.loc[reading['COD_PRV'].isin([i])]
	dataAtmosphere= go.Pie(labels=labelsAtmosphere,values=a.groupby(['COD_INT'])['COD_INT'].count().values,name='tmp')
	dataint=go.Pie(labels=a.groupby(['COD_LUM'])['COD_LUM'].count().index.values,values=a.groupby(['COD_LUM'])['COD_LUM'].count().values,name='Lumiere')
	datacol=go.Pie(labels=labelscol,values=a.groupby(['COD_TYP_COL'])['COD_TYP_COL'].count().values,name='col')
	dataob=go.Pie(labels=a.groupby(['COD_OBS_HRT'])['COD_OBS_HRT'].count().index.values, values=a.groupby(['COD_OBS_HRT'])['COD_OBS_HRT'].count().values,name='obstacle')
	datachau=go.Pie(labels=a.groupby(['COD_ETA_CHA'])['COD_ETA_CHA'].count().index.values, values=a.groupby(['COD_ETA_CHA'])['COD_ETA_CHA'].count().values,name='chausse')
	data=[dataAtmosphere,dataint,datacol,datachau,dataob]
	updatemenus = list([dict(active=-1,buttons=list([   
			    dict(label = 'tmp',
				 method = 'update',
				 args = [{'visible': [True,False, False,False, False]},
				         {'title': "Accidents par type d'athmosphere"}]),
			    dict(label = 'Lumiere',
				 method = 'update',
				 args = [{'visible': [False, True,False,False, False]},
				         {'title': "Accidents par type de lumiere"}]),
			    dict(label = 'col',
				 method = 'update',
				 args = [{'visible':[False, False,True,False, False]},
				         {'title': "Accidents par type de collision"}]),
			    dict(label = 'chausse',
				 method = 'update',
				 args = [{'visible': [False, False,False, True,False]},
				         {'title': 'Accidents per type de chausse'}]),
			    dict(label = 'obstacle',
				 method = 'update',
				 args = [{'visible': [False,  False, False, False,True]},
				         {'title': "Accidents par type d'obstacle"}])	
			]),
		    )
		])
	layout = dict(title=str(get_prv(i)), showlegend=False,
              updatemenus=updatemenus)
	fig = go.Figure(data=data, layout=layout)
	py.offline.plot(fig,filename='plt/'+str(i)+'.html',auto_open=False,show_link=False)
	print("statistics are done making")
def stat(i):
	a = reading.loc[reading['COD_PRV'].isin([i])]
	dataj = go.Bar(x=a.groupby(['HEU_ACC'])['HEU_ACC'].count().index.values, y=a.groupby(['HEU_ACC'])['HEU_ACC'].count().values,name='Heur')
	datamonth=go.Scatter(x=a.groupby(['DAT_ACC'])['DAT_ACC'].count().index.values, y=a.groupby(['DAT_ACC'])['DAT_ACC'].count().values,name='date')
	data=[dataj,datamonth]
	updatemenus1 = list([dict(active=-1,buttons=list([   
			    dict(label = 'jour',
				 method = 'update',
				 args = [{'visible': [True, False]},
				         {'title': "Nombre d'accident par Heur"}]),
			    dict(label = 'Month',
				 method = 'update',
				 args = [{'visible': [False, True]},
				         {'title': "Accidents par Date"}])]),
		    )
		])
	layout = dict(title=str(get_prv(i)), showlegend=False,
              updatemenus=updatemenus1)
	fig = go.Figure(data=data, layout=layout)
	py.offline.plot(fig,filename='plt/'+str(i)+'.html',auto_open=False,show_link=False)
	print("statistics are done making")
