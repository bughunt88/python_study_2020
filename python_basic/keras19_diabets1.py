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
model.fit(x_train, y_train, epochs=100, batch_size=4, validation_split=0.2, verbose=1)

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


# loss, mae:  3547.997802734375 47.434669494628906
# RMSE:  59.565078350614904
# R2:  0.45331641394795696

