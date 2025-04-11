import tensorflow as tf
from tensorflow.keras import mixed_precision
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Enable mixed precision for Apple Silicon (float16 accelerates training)
mixed_precision.set_global_policy("mixed_float16")

# Load CIFAR-100 dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar100.load_data()

# Normalize input data
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Optimized data pipeline using tf.data
batch_size = 64
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)) \
    .shuffle(10000).batch(batch_size).prefetch(tf.data.AUTOTUNE)
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)) \
    .batch(batch_size).prefetch(tf.data.AUTOTUNE)

# EfficientNetB0 without top to manually add Dense + softmax with correct dtype
base_model = tf.keras.applications.EfficientNetB0(
    include_top=False,
    weights=None,
    input_shape=(32, 32, 3),
    pooling="avg"
)

# Add final classification layer manually with float32 to avoid dtype mismatch
outputs = tf.keras.layers.Dense(100, activation="softmax", dtype="float32")(base_model.output)
model = tf.keras.Model(inputs=base_model.input, outputs=outputs)

# Compile the model with compatible loss
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

# Train the model
history = model.fit(train_ds, validation_data=test_ds, epochs=5, verbose=1)

# Print history
print("History keys:", history.history.keys())
print("Train Accuracy:", history.history["accuracy"])
print("Val Accuracy:", history.history["val_accuracy"])

# Plot training and validation accuracy
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Val Accuracy")
plt.title("Accuracy per Epoch")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()

# Plot ACF of validation loss residuals
residuals = np.array(history.history["val_loss"])
plot_acf(residuals - np.mean(residuals), lags=10)
plt.title("Autocorrelation of Validation Loss Residuals")
plt.show()
