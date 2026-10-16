import pandas as pd
import  joblib
from  sklearn.model_selection import  train_test_split,GridSearchCV
from sklearn.ensemble import  RandomForestClassifier


data=pd.read_csv(r"C:\Users\Dell\Downloads\weather_forecast_data (3).csv")
# print(data.to_string())

data.columns=data.columns.str.strip()

data['Rain']=data['Rain'].replace({"rain":"Rains/heavy_Clouds","no rain":"No_rains"})
print(data.to_string())

X=data.drop(columns=['Rain'])
y=data['Rain']

X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


para={
    "n_estimators":[100,200,300],
    "max_depth":[5,10,15,20],
    "min_samples_split":[2,5,10]
}


model=RandomForestClassifier(random_state=42)


grid=GridSearchCV(
    estimator=model,
    param_grid=para,
    cv=5
)


grid.fit(X_train,y_train)


best_model=grid.best_estimator_

# joblib.dump(best_model,"rain_model.pkl")
