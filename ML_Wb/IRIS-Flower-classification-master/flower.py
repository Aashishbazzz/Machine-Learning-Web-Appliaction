import pandas as pd

features=['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']

values=[5.1,3.8,1.6,0.2]

X_final=pd.DataFrame([values],columns=[features])

import joblib

filename='flower.sav'

loaded_model = joblib.load(filename)
result = loaded_model.predict(X_final)
print(result)
