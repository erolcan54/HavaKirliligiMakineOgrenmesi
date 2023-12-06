import pickle

modelLG=pickle.load(open("KAModel.sav","rb"))

from flask import Flask, request
app=Flask(__name__)
@app.route("/tahmin",methods=["POST"])
def tahmin():
    #request_data=request.get_json(force=True)

    aqi_Value=request.json["aqi_Value"]
    CO_aqi_Value=request.json["CO_aqi_Value"]
    Ozone_aqi_Value=request.json["Ozone_aqi_Value"]
    NO2_aqi_Value=request.json["NO2_aqi_Value"]

    sonuc=modelLG.predict([[aqi_Value,CO_aqi_Value,Ozone_aqi_Value,NO2_aqi_Value]])
    
    return str(int(sonuc))

app.run()