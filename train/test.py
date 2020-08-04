import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print( x_train.shape )


x_train = x_train / np.linalg.norm(x_train)


print( type(x_train[0][0][0]))
print( x_train.shape )

print("done")