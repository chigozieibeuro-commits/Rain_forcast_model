import pandas as pd
from fastapi import  FastAPI
from  database import  connection
from schema import Records
import  joblib

app=FastAPI()


@app.get("/get")
def get():
    return {
        'message': "Rain_forcast_model_running"
    }

model=joblib.load("rain_model.pkl")


@app.post("/predict")
def predict(data:Records):

    update=data.model_dump()

    match=pd.DataFrame([update])

    prediction=model.predict(match)[0]

    con=connection()
    cursor=con.cursor()

    query=""" INSERT INTO rain_check(Temperature,Humidity,Wind_Speed,Cloud_Cover,
    Pressure,Result)
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,(
            data.Temperature,data.Humidity,data.Wind_Speed,
            data.Cloud_Cover,data.Pressure,prediction
        )
    )


    con.commit()
    cursor.close()
    con.close()

    return {
        "message":prediction
    }