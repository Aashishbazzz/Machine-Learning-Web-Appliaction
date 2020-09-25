# Not made my django

from django.http import HttpResponse
from django.shortcuts import render
from . import views

def index(request):
	return render(request,"index.html")

def about(request):
	return HttpResponse("About")

def models(request):
	house=request.GET.get('house','off')
	flower=request.GET.get('flower','off')
	
	if(house=="on"):
		return render(request,'house.html')
		
	if(flower=="on"):
		return render(request,'flower.html')

def house(request):
	AREA=request.GET.get('area')
	
	INT_SQFT=request.GET.get('int_sqft')
	
	DIST_MAINROAD=request.GET.get('dist_mainroad')
	
	N_BEDROOM=request.GET.get('n_bedroom')
	
	N_BATHROOM=request.GET.get('n_bathroom')
	
	N_ROOM=request.GET.get('n_room')
	
	SALE_COND=request.GET.get('sale_cond')
	
	PARK_FACIL=request.GET.get('park_facil')
	
	BUILDTYPE=request.GET.get('buildtype')
	
	UTILITY_AVAIL=request.GET.get('utility_avail')
	
	STREET=request.GET.get('street')
	
	MZZONE=request.GET.get('mzzone')
	
	QS_ROOMS=request.GET.get('qs_rooms')
	
	QS_BATHROOM=request.GET.get('qs_bathroom')
	
	QS_BEDROOM=request.GET.get('qs_bedroom')
	
	QS_OVERALL=request.GET.get('qs_overall')
	
	COMMIS=request.GET.get('commis')
	
	
	
	##############################################################################
	##############################################################################
	##############################################################################
	##############################################################################
	
	
	import pandas as pd
	import numpy as np

	ls=['Anna Nagar',1986,26,2.0,1.0,5,'AbNormal','No','Commercial','AllPub','Gravel','RH',4.9,4.2,2.5,3.765,304049,0,0,0,0,0,0,0]

	fea=['AREA','INT_SQFT','DIST_MAINROAD','N_BEDROOM','N_BATHROOM','N_ROOM','SALE_COND','PARK_FACIL','BUILDTYPE','UTILITY_AVAIL','STREET','MZZONE','QS_ROOMS','QS_BATHROOM','QS_BEDROOM','QS_OVERALL','COMMIS','INT_SQFT_NEW','INT_SQFT_1','INT_SQFT_2','BEDROOM_1','BEDROOM_2','QS_FINAL','BATH_BED']


	df = pd.DataFrame([ls],columns=[fea])

	#using dropdown menu, write for correct option----Area
	df.replace(["TNagar","Chrompt","Chrmpet","Karapakam","Ana Nagar","Chormpet","Adyr",
           "Velchery","Ann Nagar","KKNagar"],
           ["T Nagar","Chrompet","Chrompet","Karapakkam","Anna Nagar","Chrompet","Adyar",
            "Velachery","Anna Nagar","KK Nagar"],inplace=True)


	#using dropdown----- sales condition
	df.replace(["Ab Normal","Partiall","Adj Land","PartiaLl"],["AbNormal","Partial","AdjLand","Partial"],inplace=True)

	#dropdown for----- parking facility
	df.replace("Noo","No",inplace=True)

	#dropdown--------building type
	df.replace(["Comercial","Other"],["Commercial","Others"],inplace=True)

	#dropdown-----utility avail
	df.replace("All Pub","AllPub",inplace=True)

	#dropdown--------Street
	df.replace(["Pavd","NoAccess"],["Paved","No Access"],inplace=True)


	#Int sqft
	transformed=abs(df.iloc[0]["INT_SQFT"] - 1382)
	df.iloc[0]["INT_SQFT_NEW"]=transformed
	df.drop("INT_SQFT",axis=1,inplace=True)

	df.iloc[0]["INT_SQFT_1"]=df.iloc[0]["INT_SQFT_NEW"].copy()
	df.iloc[0]["INT_SQFT_2"]=df.iloc[0]["INT_SQFT_NEW"].copy()


	if((df.iloc[0]["AREA"]=="Anna Nagar").bool() or (df.iloc[0]["AREA"]=="T Nagar").bool()):
		df.iloc[0]["INT_SQFT_2"]=0

	if((df.iloc[0]["AREA"]!="Anna Nagar").bool() and (df.iloc[0]["AREA"]!="T Nagar").bool()):
		df.iloc[0]["INT_SQFT_1"]=0
    




	#No of bedroom
	df.iloc[0]["BEDROOM_1"]=df.iloc[0]["N_BEDROOM"].copy()
	df.iloc[0]["BEDROOM_2"]=df.iloc[0]["N_BEDROOM"].copy()


	if((df.iloc[0]["AREA"]=="Velachery").bool() or (df.iloc[0]["AREA"]=="KK Nagar").bool()):
		df.iloc[0]["BEDROOM_2"]=0

	if((df.iloc[0]["AREA"]!="Velachery").bool() or (df.iloc[0]["AREA"]!="KK Nagar").bool()):
		df.iloc[0]["BEDROOM_1"]=0


	#Col type
	num_cols=["INT_SQFT","DIST_MAINROAD","N_BEDROOM","N_BATHROOM","N_ROOM","QS_ROOMS","QS_BATHROOM",
		"QS_BEDROOM","QS_OVERALL","COMMIS"]
	cat_cols=["AREA","SALE_COND","PARK_FACIL","BUILDTYPE","UTILITY_AVAIL","STREET","MZZONE"]


	#dropping transformed
	df.drop(["INT_SQFT_NEW","N_BEDROOM"],axis=1,inplace=True)


	#transformation
	df.iloc[0]["QS_FINAL"]=(df.iloc[0]["QS_ROOMS"]+df.iloc[0]["QS_BATHROOM"]+df.iloc[0]["QS_BEDROOM"]+df.iloc[0]["QS_OVERALL"])/4
	df.iloc[0]["BATH_BED"]=df.iloc[0]["N_BATHROOM"]+df.iloc[0]["N_ROOM"]






	final_features=['QS_BEDROOM', 'COMMIS', 'INT_SQFT_1', 'INT_SQFT_2', 'BEDROOM_1', 'Anna Nagar','Chrompet',
          'KK Nagar', 'Karapakkam', 'T Nagar', 'Velachery', 'AdjLand', 'Family', 'Normal Sale',
          'Partial', 'Yes', 'House', 'Others', 'ELO', 'NoSeWa', 'NoSewr ', 'No Access', 'Paved',
          'C', 'I', 'RH', 'RL', 'RM', 'QS_FINAL', 'BATH_BED']

	final_values=[0]*30

	X_final=pd.DataFrame([final_values],columns=[final_features])




	X_final.iloc[0]['QS_BEDROOM']=df.iloc[0]['QS_BEDROOM']


	X_final.iloc[0]['COMMIS']=df.iloc[0]['COMMIS']


	X_final.iloc[0]['INT_SQFT_1']=df.iloc[0]['INT_SQFT_1']


	X_final.iloc[0]['INT_SQFT_2']=df.iloc[0]['INT_SQFT_2']


	X_final.iloc[0]['BEDROOM_1']=df.iloc[0]['BEDROOM_1']


	X_final.iloc[0]['QS_FINAL']=df.iloc[0]['QS_FINAL']


	X_final.iloc[0]['BATH_BED']=df.iloc[0]['BATH_BED']




	if((df.iloc[0]['AREA']=='Anna Nagar').bool()):
		X_final.iloc[0]['Anna Nagar']=1

	elif((df.iloc[0]['AREA']=='Chrompet').bool()):
		X_final.iloc[0]['Chrompet']=1

	elif((df.iloc[0]['AREA']=='KK Nagar').bool()):
		X_final.iloc[0]['KK NAgar']=1

	elif((df.iloc[0]['AREA']=='Karapakkam').bool()):
		X_final.iloc[0]['Karapakkam']=1

	elif((df.iloc[0]['AREA']=='T Nagar').bool()):
		X_final.iloc[0]['T Nagar']=1

	elif((df.iloc[0]['AREA']=='Velachery').bool()):
		X_final.iloc[0]['Velachery']=1







	if((df.iloc[0]['SALE_COND']=='AdjLand').bool()):
		X_final.iloc[0]['AdjLand']=1

	elif((df.iloc[0]['SALE_COND']=='Family').bool()):
		X_final.iloc[0]['Family']=1

	elif((df.iloc[0]['SALE_COND']=='Normal Sale').bool()):
		X_final.iloc[0]['Normal Sale']=1

	elif((df.iloc[0]['SALE_COND']=='Partial').bool()):
		X_final.iloc[0]['Partial']=1




	if((df.iloc[0]['PARK_FACIL']=='YES').bool()):
		X_final.iloc[0]['YES']=1




	if((df.iloc[0]['BUILDTYPE']=='House').bool()):
		X_final.iloc[0]['House']=1

	elif((df.iloc[0]['BUILDTYPE']=='Others').bool()):
		X_final.iloc[0]['Others']=1




	if((df.iloc[0]['UTILITY_AVAIL']=='ELO').bool()):
		X_final.iloc[0]['ELO']=1

	elif((df.iloc[0]['UTILITY_AVAIL']=='NoSeWa').bool()):
		X_final.iloc[0]['NoSeWa']=1

	elif((df.iloc[0]['UTILITY_AVAIL']=='NoSewr').bool()):
		X_final.iloc[0]['NoSewr']=1




	if((df.iloc[0]['STREET']=='No Access').bool()):
		X_final.iloc[0]['No Access']=1

	elif((df.iloc[0]['STREET']=='Paved').bool()):
		X_final.iloc[0]['Paved']=1




	if((df.iloc[0]['MZZONE']=='C').bool()):
		X_final.iloc[0]['C']=1

	elif((df.iloc[0]['MZZONE']=='I').bool()):
		X_final.iloc[0]['I']=1

	elif((df.iloc[0]['MZZONE']=='RH').bool()):
		X_final.iloc[0]['RH']=1

	elif((df.iloc[0]['MZZONE']=='RL').bool()):
		X_final.iloc[0]['RL']=1

	elif((df.iloc[0]['MZZONE']=='RM').bool()):
		X_final.iloc[0]['RM']=1





	import joblib
	filename = 'house_model.sav'
	loaded_model = joblib.load(filename)
	result = loaded_model.predict(X_final)
	return result
	
	
	
	
def flower(request):

	import pandas as pd
	
	AREA=request.GET.get('area')
	
	INT_SQFT=request.GET.get('int_sqft')
	
	DIST_MAINROAD=request.GET.get('dist_mainroad')
	
	N_BEDROOM=request.GET.get('n_bedroom')
	
	N_BATHROOM=request.GET.get('n_bathroom')
	features=['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']
	
	values=[5.1,3.8,1.6,0.2]

	X_final=pd.DataFrame([values],columns=[features])

	import joblib

	filename='C:\\Users\\bazzz\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\flower.sav'

	loaded_model = joblib.load(filename)
	result = loaded_model.predict(X_final)
	print(result)
	return HttpResponse(result)
	