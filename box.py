
from backend.db import db
from backend.constant import code_provence
import geocoder
code= code_provence

def geo(loc):
	g = geocoder.osm(str(loc))
	latlong=[g.y,g.x]
	return latlong

def getcodeper(nom):
	for i in code_provence:
		if nom == i[1]:
			codepv= i[0]
	return codepv
def getaddresses(locn, data1,data2):
	data=db(data1,data2)
	code = getcodeper(locn)
	d=data.loc[data['COD_PRV'].isin([str(code)])]
	return d


def getadd(loc,data1,data2):
	d=getaddresses(loc,data1,data2)
	dup=d.drop_duplicates(subset=['addr'])
	lis= dup['addr'].tolist()
	
def daate(data,start=None,end=None):
	df=data
	if start != None and end != None :
		print(start.split('-'))
		print(end.split('-'))
	
		s=start.split('-')
		sy,sm,sd=s[0],s[1],s[2]
		e=end.split('-')
		ey,em,ed=e[0],e[1],e[2]
		sy,sm,sd,ey,em,ed=float(sy),float(sm),float(sd),float(ey),float(em),float(ed)
		sy,sm,sd,ey,em,ed=int(sy),int(sm),int(sd),int(ey),int(em),int(ed)
		sy,ey= sy-2000 , ey-2000
		df=df.query('annee >='+ str(sy)+' and annee <='+str(ey)+'and Mois>='+str(sm)+'and Mois <='+str(em)+'and jour >='+str(sd)+'and jour <='+str(ed))
	return df
 
def dist(a,b):
	distance = math.sqrt( ((a[0]-b[0])**2)+((a[1]-b[1])**2) )
	return distance


