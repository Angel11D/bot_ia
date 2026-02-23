import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

IMG_SIZE = 150
CLASSES = ['ardilla', 'huron']  # ajusta a tus clases

# Cargar modelo
model = load_model("moodpet_model.h5")

def getclass(image_path: str):
    """
    Recibe la ruta de una imagen, la procesa y devuelve la predicción.
    Soporta modelos con 1 o 2 entradas.
    """
    try:
        # Cargar y preparar la imagen
        img = Image.open(image_path).convert("RGB")
        img = img.resize((IMG_SIZE, IMG_SIZE))
        arr = np.expand_dims(np.asarray(img) / 255.0, axis=0)  # normalización

        # Detectar si el modelo espera 1 o 2 entradas
        if isinstance(model.input_shape, list) and len(model.input_shape) == 2:
            preds = model.predict([arr, arr], verbose=0)[0]  # parche si son 2 inputs
        else:
            preds = model.predict(arr, verbose=0)[0]

        # Obtener clase y confianza
        idx = np.argmax(preds)
        clase = CLASSES[idx]
        conf = preds[idx]

        return f"Predicción: {clase} ({conf*100:.1f} %)"

    except Exception as e:
        return f"Error en predicción: {str(e)}"
