import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Make NumPy printouts easier to read.
np.set_printoptions(precision=3, suppress=True)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

def build_and_compile_model(norm):
  model = keras.Sequential([
      norm,
      layers.Dense(32, activation='relu'),
      layers.Dense(32, activation='relu'),
      layers.Dense(1)
  ])

  model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model

# Read csv file to a raw dataframe
raw_dataset = pd.read_csv('DistrictDatawithResults.csv')

# Create a copy of the dataframe
dataset = raw_dataset.copy()
del dataset["District"] # Delete the district labeling

fields = list(dataset.columns)
print(fields)

# Divide the datasets in a training and testing set
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# Draw the graphs (if necessary)
# sns.pairplot(train_dataset[fields], diag_kind='kde')
# train_dataset.describe().transpose()

# Copy the features again
train_features = train_dataset.copy()
test_features = test_dataset.copy()

# Separate the dependent variable
train_labels = train_features.pop('Result')
test_labels = test_features.pop('Result')


# Normalize the data (may not be necessary)
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(train_features))

input_layer = layers.Input(shape=(len(train_features.columns),))
normalized_input = normalizer(input_layer)

full_model = build_and_compile_model(normalizer)

full_model.summary()

history = full_model.fit(
    train_features,
    train_labels,
    validation_split=0.2,
    verbose=0, epochs=50)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()
print(hist.tail())

def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 1])
    plt.xlabel('Epoch')
    plt.ylabel('Error[Results]')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_loss(history)

test_results = {}
test_results['full_model'] = full_model.evaluate(test_features, test_labels, verbose=0)

print(pd.DataFrame(test_results, index=['Mean absolute error [Results]']).T)

test_predictions = full_model.predict(test_features).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [Results]')
plt.ylabel('Predictions [Results]')
lims = [0, 1]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)
plt.show()

print("Finished")