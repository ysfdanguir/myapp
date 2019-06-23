import pandas as pd
import numpy as np
import plotly
import plotly.offline as plt
import plotly.graph_objs as go
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib as mplt


charactestics = pd.read_csv('../Datasets/France/data/caracteristics.csv', encoding = "ISO-8859-1", low_memory=False)
holiday = pd.read_csv('E:/Projet_Mascir/dataset/fr/holidays.csv', low_memory=False)
places = pd.read_csv('../Datasets/France/data/places.csv', low_memory=False)
users = pd.read_csv('../Datasets/France/data/users.csv',low_memory=False)
vehicles = pd.read_csv('../Datasets/France/data/vehicles.csv', low_memory=False)


"""
English mapping:

Mapping = {
    'Num_Acc':'AccidentID',
    'jour':'Day',
    'mois':'Month',
    'an':'Year',
    'hrmn':'Hour',
    'lum':'LightingCondition',
    'dep':'Department',
    'com':'Municipality',
    'agg':'Localisation',
    'int':'Intersection',
    'atm':'AtmosphericCondition',
    'col':'CollisionType',
    'adr':'Address',
    'gps':'GpsCoding',
    'lat':'Latitude',
    'long':'Longitude',
    'catr':'RoadCategory',
    'voie':'RoadNumber',
    'v1':'RouteNumber',
    'v2':'RouteName',
    'circ':'TrafficType',
    'nbv':'NumberofLanes',
    'vosp':'OuterLane',
    'Prof':'RoadProfile',
    'pr':'HomePRNumber',
    'pr1':'PRDistance',
    'plan':'LaneStructure',
    'lartpc':'CentralLaneWidth',
    'larrout':'OuterLaneWidth',
    'surf':'SurfaceCondition',
    'infra':'Infrastructure',
    'situ':'SituationofAccident',
    'env1':'SchoolPoint',
    'Acc_number':'AccidentID',
    'Num_Veh':'NumberOfVehicles',
    'place':'Place',
    'catu':'UserCatagory',
    'grav':'Severity ',
    'Year_on':'UserYoB',
    'locp':'Locationofpedestrian',
    'actp':'Actionofpedestrian',
    'etatp':'PedestrianGroup',
    'sexe' : 'Sex',
    'secu':'SafetyEquipment'
}

"""
Mapping02 = {
    'Num_Acc':'AccidentID',
    'jour':'jour',
    'mois':'Mois',
    'an':'annee',
    'hrmn':'Heure',
    'lum':'lumiere',
    'dep':'Department',
    'com':'Municipalite',
    'agg':'Localisation',
    'int':'Intersection',
    'atm':'Atmosphere',
    'col':'CollisionType',
    'adr':'Addresse',
    'gps':'GpsCoding',
    'lat':'Latitude',
    'long':'Longitude',
    'catr':'CategorieRoute',
    'voie':'voie',
    'v1':'NombreRoute',
    'v2':'NomRoute',
    'circ':'TypeTraffic',
    'nbv':'NombereDeVoies',
    'vosp':'VoieExterieure',
    'Prof':'ProfilRoutier',
    'pr':'HomePRNumber',
    'pr1':'PRDistance',
    'plan':'StructureVoie',
    'lartpc':'CentralVoieLargeur',
    'larrout':'LargeurVoie Exterieur',
    'surf':'ConditionSurface',
    'infra':'Infrastructure',
    'situ':'SituationAccident',
    'env1':'PointEcole',
    'Acc_number':'AccidentID',
    'Num_Veh':'NombreVehicules',
    'place':'Lieux',
    'catu':'UsagerCategorie',
    'grav':'Gravite ',
    'Year_on':'UserYoB',
    'locp':'EmplacementDuPieton',
    'actp':'ActionDupieton',
    'etatp':'PietonsGroup',
    'sexe' : 'Sexe',
    'secu':'EquipmentDeSecurite'
}

charactestics.rename(index=str, columns=Mapping02, inplace=True)
holiday.rename(index=str, columns=Mapping02, inplace=True)
places.rename(index=str, columns=Mapping02, inplace=True)
users.rename(index=str, columns=Mapping02, inplace=True)
vehicles.rename(index=str, columns=Mapping02, inplace=True)

