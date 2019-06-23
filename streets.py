import osmnx as ox
import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors
ville=['Province de Sidi Slimane إقليم سيدي سليمان',' Province de Midelt إقليم ميدلت','Berrechid Province','Province de Sidi Bennour إقليم سيدي بنور','Rhamna Province','Province de Fquih Ben Saleh إقليم الفقيه بن صالح',' Province de Youssoufia إقليم اليوسفية',' Province de Tinghir إقليم تنغير','Sidi Ifni Province','Tarfaya Province']
ox.config(log_console=True, use_cache=True)
# download the street network for Rabat,Maroc
street_count=[]
for vil in ville:
	a=0
	print(vil)
	G = ox.graph_from_place(vil+',Maroc', network_type='all_private')
	street=ox.count_streets_per_node(G, nodes=None)
	for v in street.values():
		a=v+a
	
	street_count.append([vil,a])
	print("#################################################################################################################")
	print(a)
	print(street_count)
	print("#################################################################################################################")



