import tensorflow as tf

from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Dropout(0.5))

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))

model.summary()

model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

history=model.fit(train_images,train_labels,epochs=500,validation_data=(test_images,test_labels))

test_loss,test_acc=model.evaluate(test_images,test_labels,verbose=2)

plt.plot(history.history['accuracy'],label='accuracy of training set')
plt.plot(history.history['val_accuracy'],label='accuracy of testing set')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5,1])
plt.legend(loc='lower right')

plt.plot(history.history['loss'],label='loss of training set')
plt.plot(history.history['val_loss'],label='loss of testing set')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0.5,1])
plt.legend(loc='lower right')

print(test_acc)



