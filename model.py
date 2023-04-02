import pandas as pd
data=pd.read_csv('kc_house_data.csv')
from sklearn.model_selection import train_test_split
y = data['price']
features = ['bedrooms', 'bathrooms', 'sqft_living','sqft_basement','yr_built']
x = data[features]
x_train , x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
from sklearn.ensemble import RandomForestRegressor
kc_rfmodel = RandomForestRegressor(n_estimators=20, random_state = 0)
kc_rfmodel.fit(x_train, y_train)
y_rfpred = kc_rfmodel.predict(x_test)

import pickle
pickle.dump(kc_rfmodel,open("model1.pkl","wb"))

