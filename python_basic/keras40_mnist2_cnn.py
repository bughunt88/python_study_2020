# 인공지능계의 hello world라 불리는 mnist!!!


# 실습!!! 완성하시요!!!
# 지표는 acc

# 응용
# y_test 10개와 y_pred 10개를 출력하시오

# y_test[:10] = (?,?,?,?,?,?,?,?,?,?)
# y_pred[:10] = (?,?,?,?,?,?,?,?,?,?)

# 0.985


import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist


(x_train, y_train), (x_test,y_test)= mnist.load_data()

# plt.imshow(x_train[1])
# plt.show()



# 데이터 전처리

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1],x_train.shape[2], 1)/255.
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1],x_test.shape[2], 1)/255.
# (x_test.reshape(x_test.shape[0], x_test.shape[1],x_test.shape[2], 1))



# OnHotEncoding (다중 분류 데이터에서 Y값을 해주는 것)

from tensorflow.keras.utils import to_categorical # OneHotEncoding from tensorflow
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)




from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout,LSTM

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3), padding='same', input_shape=(28,28,1), activation='relu'))
model.add(Conv2D(filters=32, kernel_size=(3), padding='same', input_shape=(28,28,1), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=64, kernel_size=(3), padding='same', input_shape=(28,28,1), activation='relu'))
model.add(Conv2D(filters=64, kernel_size=(3), padding='same', input_shape=(28,28,1), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(365))
model.add(Dense(180))

model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))


model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])


from tensorflow.keras.callbacks import EarlyStopping
stop = EarlyStopping(monitor='loss', patience=16, mode='auto')

model.fit(x_train, y_train, epochs=5, batch_size=70, validation_split=0.2, verbose=2, callbacks=[stop])


#4. 평가, 예측
loss, mae = model.evaluate(x_test, y_test, batch_size=70)

y_predict = model.predict(x_test[:10])


print(loss)
print(mae)


print('y_test : ',  y_test[:10].argmax(axis=1))
print('y_predict_argmax : ', y_predict.argmax(axis=1)) 

# CNN
# 0.02563497982919216
# 0.991599977016449
# y_test :  [7 2 1 0 4 1 4 9 5 9]
# y_predict_argmax :  [7 2 1 0 4 1 4 9 5 9]