# 2개의 파일을 만드시오
# 1. Earlystopping 을 적용하지 않는 최고의 모델
# 2. Earlystopping 을 적용한 최고의 모델

import numpy as np

#1 데이터 주고
from tensorflow.keras.datasets import boston_housing
(train_data, train_target), (test_data, test_target) = boston_housing.load_data()

x_train = train_data
y_train = train_target
x_test = test_data
y_test = test_target

from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, train_size=0.8, random_state=66)

print(x_train.shape) #(404, 13)
#모델 구성
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input

input1 = Input(shape=(13,))
dense1 = Dense(200, activation='relu')(input1)
dense1 = Dense(200)(dense1)
dense1 = Dense(200)(dense1)
dense1 = Dense(200)(dense1)
dense1 = Dense(200)(dense1)
dense1 = Dense(200)(dense1)
dense1 = Dense(200)(dense1)
dense1 = Dense(100)(dense1)
output1 = Dense(1)(dense1)

model = Model(inputs=input1, outputs=output1)

#컴파일, 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=30, mode='min')
model.fit(x_train, y_train, epochs=1000, batch_size=8, validation_data=(x_val, y_val), verbose=1, callbacks=[early_stopping])

#평가, 예측
loss, mae = model.evaluate(x_test, y_test, batch_size=1)
print('loss, mae: ', loss, mae)

y_predict = model.predict(x_test)

#RMSE, R2
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print('RMSE: ', RMSE(y_test, y_predict))

from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_predict)
print('R2: ', R2)


# 1번 파일
# loss, mae:  12.677735328674316 2.3703505992889404
# RMSE:  3.560580890674209
# R2:  0.8477036261001453

# 2번 파일
# loss, mae:  25.943134307861328 3.2234861850738525
# RMSE:  5.093439921908657
# R2:  0.6883477794527708
