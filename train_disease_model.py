import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

data = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train = data.flow_from_directory(
    "disease_data",
    target_size=(128,128),
    batch_size=8,
    class_mode="categorical",
    subset="training"
)

val = data.flow_from_directory(
    "disease_data",
    target_size=(128,128),
    batch_size=8,
    class_mode="categorical",
    subset="validation"
)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), activation="relu", input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(2, activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(train, validation_data=val, epochs=5)

model.save("disease_model.h5")

print("Disease model saved")
