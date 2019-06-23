import folium
import osmnx as ox
import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors
import pandas as pd
import random
def colo():
	list = ['#FFFFFF', '#000000' , '#FF0033', '#555577','#FF3311']
	color= random.choice(list)
	print("random.choice() to select random item from list - ", random.choice(list))
	return color
def make_folium_polyline(edge, edge_color, edge_width, edge_opacity, popup_attribute=None):

	"""
	Turn a row from the gdf_edges GeoDataFrame into a folium PolyLine with
	attributes.
	Parameters
	----------
	edge : GeoSeries
	a row from the gdf_edges GeoDataFrame
	edge_color : string
	color of the edge lines
	edge_width : numeric
	width of the edge lines
	edge_opacity : numeric
	opacity of the edge lines
	popup_attribute : string
	edge attribute to display in a pop-up when an edge is clicked, if None,
	no popup
	Returns
	-------
	pl : folium.PolyLine
	"""

	# check if we were able to import folium successfully
	if not folium:
		raise ImportError('The folium package must be installed to use this optional feature.')

	# locations is a list of points for the polyline
	# folium takes coords in lat,lon but geopandas provides them in lon,lat
	# so we have to flip them around
	locations = list([(lat, lon) for lon, lat in edge['geometry'].coords])

	# if popup_attribute is None, then create no pop-up
	if popup_attribute is None:
		popup = None
	else:
	# folium doesn't interpret html in the html argument (weird), so can't
	# do newlines without an iframe
		popup = popup_attribute

	# create a folium polyline with attributes
	pl = folium.PolyLine(locations=locations, popup=popup, color=edge_color, weight=edge_width, opacity=edge_opacity)
	return pl
def plot_graph_folium(G, graph_map=None, popup_attribute=None,
                      tiles='cartodbpositron', zoom=1, fit_bounds=True,
                      edge_width=5, edge_opacity=1):
	"""
	Plot a graph on an interactive folium web map.
	Note that anything larger than a small city can take a long time to plot and
	create a large web map file that is very slow to load as JavaScript.
	Parameters
	----------
	G : networkx multidigraph
	graph_map : folium.folium.Map
	if not None, plot the graph on this preexisting folium map object
	popup_attribute : string
	edge attribute to display in a pop-up when an edge is clicked
	tiles : string
	name of a folium tileset
	zoom : int
	initial zoom level for the map
	fit_bounds : bool
	if True, fit the map to the boundaries of the route's edges
	edge_color : string
	color of the edge lines
	edge_width : numeric
	width of the edge lines
	edge_opacity : numeric
	opacity of the edge lines
	Returns
	-------
	graph_map : folium.folium.Map
	"""
	edge_color=colo()
	    # create gdf of the graph edges
	gdf_edges = ox.graph_to_gdfs(G, nodes=False, fill_edge_geometry=True)

	# get graph centroid
	x, y = gdf_edges.unary_union.centroid.xy
	graph_centroid = (y[0], x[0])

	# create the folium web map if one wasn't passed-in
	if graph_map is None:
		graph_map = folium.Map(location=graph_centroid, zoom_start=zoom, tiles=tiles)

	    # add each graph edge to the map
	flag=True
	for _, row in gdf_edges.iterrows():
		if flag==True:
			pl = make_folium_polyline(edge=row, edge_color='#006400', edge_width=edge_width,
			                  edge_opacity=edge_opacity, popup_attribute=popup_attribute)
			flag=False
		else:
			pl = make_folium_polyline(edge=row, edge_color=colo(), edge_width=edge_width,
			                  edge_opacity=edge_opacity, popup_attribute=None)
		pl.add_to(graph_map)
		print("still working waa3")

	    # if fit_bounds is True, fit the map to the bounds of the route by passing
	    # list of lat-lng points as [southwest, northeast]
	if fit_bounds:
		tb = gdf_edges.total_bounds
		bounds = [(tb[1], tb[0]), (tb[3], tb[2])]
		graph_map.fit_bounds(bounds)
	print("bounds done")
	return graph_map
	

#from IPython.display import IFrame
#%matplotlib inline
ox.config(log_console=True, use_cache=True)
# download the street network for Rabat,Maroc
G = ox.graph_from_place('Errachidia,Maroc', network_type='drive')
#G = ox.graph_from_address('Rabat,Maroc', distance=1800, network_type='drive')



# plot the street network with folium

graph_map = plot_graph_folium(G, popup_attribute='name', edge_width=2)
#save map HTML 
filepath = 'graph2.html'
graph_map.save(filepath)



