import folium
from backend.box import getaddresses, getadd, getcodeper, geo
from folium import plugins
from folium import IFrame
import plotinggg as pltg
from backend.constant import countacc, code_provence
from backend.roadcolore import plot_graph_folium
import osmnx as ox
import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors
import pickle
from datetime import datetime
"""from sklearn.externals import joblib
import os
import numpy as np
import pandas as pd
filename='model11.sav'
model = joblib.load(open(filename,"rb"))"""
def col(c):
	red= int((c/50)*255)
	green= int(255-(c/50)*255)
	f='#%02x%02x%02x' % (red, green, 0)
	return f
def mapbuid(loc):
	m = folium.Map(location=loc , zoom_start=12)
	m.save("templates/map.html")
	return m
c=0
"""
def mapp(loc,flag,data):
	c=0
	d=0
	lat=geo(loc)
	m=mapbuid(lat)
	df = data
	if flag==1:
		for i in range(0,len(df.index)):
			c=c+1
			name=pltg.stats(str(df.iloc[i,-4]))
			print(c)
	elif flag==2:
		for i in range(0,len(df.index)):
			c=c+1
			name=pltg.stat(str(df.iloc[i,-4]))
			print(c)
	if flag==0:
		print(flag)
	else:
		for i in range(0,len(df.index)):
				d=d+1
				with open('plt/'+str(df.iloc[i,-4])+'.html', 'r') as f:
					html1= f.read()

				adresse=[df.iloc[i,6]/100000,df.iloc[i,7]/100000]
				popup = folium.Popup(folium.Html(folium.IFrame(html1, width='600px', height='380px').render(), script=True), max_width=2750)
				marker=folium.RegularPolygonMarker(location=adresse,popup=popup,fill_color=col(df.iloc[i,-1]),number_of_sides=30,radius=5)
				marker.add_to(m)
				print(d)
	'''for i in range(6, df.size()-1):
			name=pltg.stats(str(df.iloc[i,-4]))
	for i in range(6, df.size()-1):
			x=df.iloc[i,-3]
			with open('plt/'+str(df.iloc[i,-4])+'1.html', 'data1') as f:
				html1= f.read()
			adr.append([df.iloc[i,6]/100000,df.iloc[i,7]/100000])
			adresse=[df.iloc[i,6]/100000,df.iloc[i,7]/100000]
			popup = folium.Popup(folium.Html(folium.IFrame(html1, width='600px', height='380px').render(), script=True), max_width=2650)
			marker=folium.RegularPolygonMarker(location=adresse,popup=popup,fill_color=col(df.iloc[i,-1]),number_of_sides=6,radius=5)
			marker.add_to(m)'''
	hm = plugins.HeatMap(adr,radius=10)
	m.add_child(hm)
	m.save("templates/map.html")
def mappp(loc,data):
	c=0
	d=0
	lat=geo(loc)
	m=mapbuid(lat)
	df =data
	for i in range(0,len(df.index)):
			d=d+1
			adresse=[df.iloc[i,6]/100000,df.iloc[i,7]/100000]
			popup = folium.Popup('<div><strong>'+str(df.iloc[i,-4])+"</strong></div><div><strong> Nombre d'accident:"+str(countacc(str(df.iloc[i,-4]),data1,data2))+'</strong></div>')
			marker=folium.RegularPolygonMarker(location=adresse,popup=popup,fill_color=col(df.iloc[i,-1]),number_of_sides=30,radius=5)
			marker.add_to(m)
			print(len(df.index)-d)
	'''for i in range(6, df.size()-1):
			name=pltg.stats(str(df.iloc[i,-4]))
	for i in range(6, df.size()-1):
			x=df.iloc[i,-3]
			with open('plt/'+str(df.iloc[i,-4])+'1.html', 'data1') as f:
				html1= f.read()
			adr.append([df.iloc[i,6]/100000,df.iloc[i,7]/100000])
			adresse=[df.iloc[i,6]/100000,df.iloc[i,7]/100000]
			popup = folium.Popup(folium.Html(folium.IFrame(html1, width='600px', height='380px').render(), script=True), max_width=2650)
			marker=folium.RegularPolygonMarker(location=adresse,popup=popup,fill_color=col(df.iloc[i,-1]),number_of_sides=6,radius=5)
			marker.add_to(m)'''
	hm = plugins.HeatMap(adr,radius=10)
	m.add_child(hm)
	m.save("templates/map.html")
"""
def mapp(loc,flag,data,road='drive'):
	
	df = data
	if flag==1:
		name=pltg.stats(str(getcodeper(loc)))
		print(c)
	elif flag==2:
		name=pltg.stat(str(getcodeper(loc)))
		print(c)
	if flag==0:
		print(flag)
	else:
		with open('plt/'+str(getcodeper(loc))+'.html', 'r') as f:
			html1= f.read()
		popup = folium.Popup(folium.Html(folium.IFrame(html1, width='600px', height='380px').render(), script=True), max_width=2750)
				
		ox.config(log_console=True, use_cache=True)
		print("still need to plot")
		# download the street network for Rabat,Maroc
		G = ox.graph_from_place(loc+',Maroc', network_type='all')
		#location=geo(loc+',Maroc')
		#m = folium.Map(location=location, zoom_start=12)
		#m.polygon_marker(location=location ,popup= popup ,fill_color=col(25), num_sides=3, radius=10)
		print("ploting the map is done")
		print("ploting the stats is on going")
		#G = ox.graph_from_address('Rabat,Maroc', distance=1800, network_type='drive')
		# plot the street network with folium
		graph_map = plot_graph_folium(G, popup_attribute=popup, edge_width=2)
		print("the damn statistics done")
		#pdb.set_trace()
		#save map HTML 
		filepath = 'templates/map.html'
		print("making the html start")
		print("making the html done")
		graph_map.save(filepath)
def mappp(loc,data):
	ox.config(log_console=True, use_cache=True)
	# download the street network for Rabat,Maroc
	print("still need to plot")
	G = ox.graph_from_place(loc+',Maroc', network_type='drive')
	print("ploting the map is done")
	print("ploting the stats is on going")
	#G = ox.graph_from_address('Rabat,Maroc', distance=1800, network_type='drive')
	# plot the street network with folium
	graph_map = plot_graph_folium(G, popup_attribute='name', edge_width=2)
	print("the damn statistics done")
	#save map HTML 
	filepath = 'templates/map.html'
	graph_map.save(filepath)
"""
def prediction(date):
	#NEEEEEEDDD THE BOUNDERIES ADD THEM AT MORNING ..
	state_geo = os.path.join('/Datasets/Maroc/', 'Morocco.GeoJson')
	state_data=pre(predict(date))
	m = folium.Map(location=[33.9716,-6.8498], zoom_start=5)
	m.choropleth(
		geo_data=geo,
		name='choropleth',
		data=state_data,
		columns=['State', 'counts'],
		key_on='feature.id',
		fill_color='YlGn',
		fill_opacity=0.7,
		line_opacity=0.2,
		legend_name='Accident Rate (%)'
	)
	filepath = 'templates/map.html'
	m.save(filepath)
def predict(date):
	a=[]
	dt=datetime.strptime(date , '%Y-%m-%d')
	annee=dt.year
	mois=dt.month
	jours=dt.day
	for i in code_provence:
		pred=[annee,mois,jours,i[0],1,0,0,0,0,0,0,0,0,0,0]
		for j in range(6,9):
			pred[j]=1
			for k in range(9,15):
				pred[k]=1
				prede=np.asarray(pred)
				prede.reshape(1,-1)
				prediction = model.predict(prede)
				a.append([i[0],prediction])
	return a
def pre(d):
	data = d
	df = pd.DataFrame(data, columns = ['prov', 'Acc'])
	dataf=df.query('Acc > 0')
	dataf.groupby(['prov']).size().reset_index(name='counts')
	dataf.drop(['Acc'])
	return dataf
"""

