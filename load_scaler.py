import joblib
import numpy as np

test_conf = 0.7
test_w = 11
test_h = 8

test_if = test_conf * test_w * test_h

my_scaler = joblib.load('scaler.gz')

sclaed_if = my_scaler.transform(np.array([test_if]).reshape(-1, 1))
sclaed_if = (sclaed_if[0][0] * 10)

print(int(round(sclaed_if, -1)))