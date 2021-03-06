#실습 19_1,2,3,4,5, earlystopping까지
#총 6개의 파일을 완성하시오

import numpy as np
from sklearn.datasets import load_diabetes 
#당뇨병

# 1. 데이터

dataset = load_diabetes()
x = dataset.data
y = dataset.target

print(x.shape, y.shape) \

print(np.max(x), np.min(y)) 


# 데이터 분리

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state=66)
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, train_size = 0.8, random_state=66)


# 데이터 전처리 (MinMaxScaler를 이용 기준 - x_train)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)


# 2.모델 구성

from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Dense, Input

model = Sequential()
model.add(Dense(120, input_shape=(10,), activation='relu'))
model.add(Dense(120))
model.add(Dense(120))
model.add(Dense(60))
model.add(Dense(1))

# 3.컴파일, 훈련

model.compile(loss='mse', optimizer='adam', metrics=['mae'])

from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=20, mode='min')
model.fit(x_train, y_train, epochs=1000, batch_size=4, validation_data=(x_val, y_val), verbose=1, callbacks=[early_stopping])


# 4.평가, 예측

loss, mae = model.evaluate(x_test, y_test, batch_size=24)
print('loss, mae: ', loss, mae)

y_predict = model.predict(x_test)

# RMSE와 R2 구하기

from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict):
      return np.sqrt(mean_squared_error(y_test, y_predict))
print('RMSE: ', RMSE(y_test, y_predict))

from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_predict)
print('R2: ', R2)


# 1번 파일
# loss, mae:  3547.997802734375 47.434669494628906
# RMSE:  59.565078350614904
# R2:  0.45331641394795696

# 2번 파일
# loss, mae:  3334.061767578125 48.04975128173828
# RMSE:  57.74134117641389
# R2:  0.48628016531363716

# 3번 파일
# loss, mae:  3551.124755859375 49.29926681518555
# RMSE:  59.591314776302326
# R2:  0.4528347161985923

# 4번 파일
# loss, mae:  3507.125732421875 48.26522445678711
# RMSE:  59.220987642207554
# R2:  0.45961424556131214

# 5번 파일
# loss, mae:  3453.349609375 47.44731903076172
# RMSE:  58.76521568539809
# R2:  0.46789998793911425

# 6번 파일
# loss, mae:  3290.349609375 47.47173309326172
# RMSE:  57.36157129187806
# R2:  0.49301550393879634
