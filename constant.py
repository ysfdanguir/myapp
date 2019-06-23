from flask import flash, request, redirect, url_for
import pandas as pd
ville_list = ['Rabat', 'Sale', 'Skhirat', 'Temara', 'Khemisset', 'Prefecture of Casablanca', 'Mohammedia', 'Fès Province', 'Sefrou', 'Boulmane', 'Meknès Province', 'El Hajeb', 'Ifrane', 'province de Khenifra', 'Errachidia', 'Préfecture de Marrakech', 'Chichaoua', 'Kelâat Es-Sraghna', 'Essaouira Province', 'Préfecture de Agadir', 'Inezgane', 'Aït Melloul', 'Chtouka – Aït Baha Province', 'Taroudant Province', 'Tiznit Province', 'Ouarzazate Province', 'Zagora Province', 'Prefecture of Tangier', 'Larache Province', 'Ksar El Kebir Province', 'Chefchaouen Province', 'Tetouan Province', 'El Hoceima Province', ' Province de Taza اقليم تازة', 'Taounate Province', "Préfecture d'Oujda-Angad", 'Province de Berkane إقليم بركان', 'Province de Nador إقليم الناظور', 'Province de Taourirt إقليم تاوريرت', 'Province de Jerada إقليم جرادة', 'Province de Figuig إقليم الناظور', 'Province de Safi إقليم أسفي', 'El Jadida Province', 'Settat Province', ' Province de Khouribga إقليم خريبكة', ' Province de Benslimane إقليم بن سليمان', ' Province de Kenitra إقليم القنيطرة', ' Province de Sidi Kacem إقليم سيدي قاسم', ' Province de Beni Mellal إقليم بني ملال', "Province d'Azilal إقليم أزيلال", "Province d'Es-Semara إقليم السمارة", 'Guelmim Province', 'Province de Tan-Tan إقليم طانطان', 'Tata Province', 'Assa-Zag Province', 'Laâyoune Province', 'Boujdour Province', "Province d'Aousserd إقليم أوسرد", 'cercle de Hrara', 'Médiouna Province', " Préfecture de M'diq-Fnideq عمالة المضيق الفنيدق", 'Province de Driouch إقليم الدريوش', 'Guercif Province', 'Ouazzane Province', 'Province de Sidi Slimane إقليم سيدي سليمان', ' Province de Midelt إقليم ميدلت', 'Berrechid Province', 'Province de Sidi Bennour إقليم سيدي بنور', 'Rhamna Province', 'Province de Fquih Ben Saleh إقليم الفقيه بن صالح', ' Province de Youssoufia إقليم اليوسفية', ' Province de Tinghir إقليم تنغير', 'Sidi Ifni Province', 'Tarfaya Province']

code_provence=[[1, 'Rabat'], [2, 'Sale'], [3, 'Sale'], [4, 'Skhirat'],[4, 'Témara'], [5, 'Khémisset'], [6, 'Prefecture of Casablanca'], [7, 'Prefecture of Casablanca'], [8, 'Prefecture of Casablanca'], [9, "Prefecture of Casablanca"], [10, 'Prefecture of Casablanca'], [11, 'Prefecture of Casablanca'], [12, 'Prefecture of Casablanca'], [13, 'Prefecture of Casablanca'], [14, 'Mohammédia'], [15, 'Fès Province'], [16, 'Fès Province'], [17, 'Fès Province'], [18, 'Sefrou'], [19, 'Boulmane'], [20, 'Meknès Province'], [21, 'Meknès Province'], [22, 'El Hajeb'], [23, 'Ifrane'], [24, 'province de Khenifra'], [25, 'Errachidia'], [26, 'Préfecture de Marrakech'], [27, 'Préfecture de Marrakech'], [28, 'Préfecture de Marrakech'], [29, 'Préfecture de Marrakech'], [30, 'Chichaoua'], [31, 'Kelâat Es-Sraghna'], [32, 'Essaouira Province'], [33, 'Préfecture de Agadir'], [34, 'Inezgane'], [34, ' Aït Melloul'], [35, 'Chtouka – Aït Baha Province'], [36, 'Taroudant Province'], [37, 'Tiznit Province'], [38, 'Ouarzazate Province'], [39, 'Zagora Province'], [40, 'Prefecture of Tangier'], [41, 'Prefecture of Tangier'], [42, 'Larache Province'],[42, 'Ksar El Kébir Province'], [43, 'Chefchaouen Province'], [44, 'Tétouan Province'], [45, 'El Hoceima Province'], [46, 'Province de Taza اقليم تازة'], [47, 'Taounate Province'], [48, "Préfecture d'Oujda-Angad"], [49, 'Province de Berkane إقليم بركان'], [50, 'Province de Nador إقليم الناظور'], [51, 'Province de Taourirt إقليم تاوريرت'], [52, 'Province de Jerada إقليم جرادة'], [53, 'Province de Figuig إقليم الناظور'], [54, 'Province de Safi إقليم أسفي'], [55, 'El Jadida Province'], [56, 'Settat Province'], [57, 'Province de Khouribga إقليم خريبكة'], [58, 'Province de Benslimane إقليم بن سليمان'], [59, 'Province de Kenitra إقليم القنيطرة'], [60, 'Province de Sidi Kacem إقليم سيدي قاسم'], [61, 'Province de Beni Mellal إقليم بني ملال'], [62, "Province d'Azilal إقليم أزيلال"], [63, 'Smara'], [64, 'Guelmim'], [65, 'Tan-Tan'], [67, 'Tata'], [68, 'Assa-Zag'], [69, 'Laâyoune'], [70, 'Boujdour'], [71, 'Oued Ed-Dahab-Lagouira'], [72, "Province d'Aousserd إقليم أوسرد"], [73, 'Prefecture of Casablanca'], [74, 'Prefecture of Casablanca'], [75, 'Médiouna Province'], [76, " Préfecture de M'diq-Fnideq عمالة المضيق الفنيدق"], [77, 'Province de Driouch إقليم الدريوش'], [78, 'Guercif Province'], [79, 'Ouazzane Province'], [80, 'Province de Sidi Slimane إقليم سيدي سليمان'], [81, ' Province de Midelt إقليم ميدلت'], [82, 'Berrechid Province'], [83, 'Province de Sidi Bennour إقليم سيدي بنور'], [84, 'Rhamna Province'], [85, 'Province de Fquih Ben Saleh إقليم الفقيه بن صالح'], [86, 'Province de Youssoufia إقليم اليوسفية'], [87, 'Province de Tinghir إقليم تنغير'], [88, 'Sidi Ifni Province'], [89, 'Tarfaya Province']]

a="Datasets/Maroc/accident.xlsx"
b="Datasets/Maroc/vehicule.xlsx"
def me():
	return [33.9716,-6.8498]
def countacc(addresse,data1,data2):
	data=db(data1,data2)
	adr=data.loc[data['addr'].isin([str(addresse)])]
	c= len(adr.index)
	print('##################################################################################################################################')
	print(c)
	return c
road_type= ['drive','drive_service','walk','bike','all','all_private']
def get_code(place):
	a=""
	for i in code_provence:
		if i[1]==place:
			a=i[0]
	return a
def db(data1,data2):
	df=pd.read_excel(data1)
	data =pd.read_excel(data2)
	return df
def get_prv(place):
	a=""
	for i in code_provence:
		if i[0]==place:
			a=i[1]
	return a