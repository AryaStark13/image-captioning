from sklearn.preprocessing import MinMaxScaler

min_conf = 0.5
min_w = 10
min_h = 10

max_conf = 1.0
max_w = 100
max_h = 100

min_if = min_conf * min_w * min_h
max_if = max_conf * max_w * max_h

test_conf = 0.7
test_w = 50
test_h = 50

test_if = test_conf * test_w * test_h

import numpy as np

# scale min_if to 1 and max_if to 10 using MinMaxScaler

scaler = MinMaxScaler(feature_range=(1, 10))

scaler.fit(np.array([min_if, max_if]).reshape(-1, 1))

sclaed_if = scaler.transform(np.array([test_if]).reshape(-1, 1))
sclaed_if = int(sclaed_if[0][0] * 10)

print(round(sclaed_if, -1))

import joblib
joblib.dump(scaler, 'scaler.gz')
# my_scaler = joblib.load('scaler.gz')
