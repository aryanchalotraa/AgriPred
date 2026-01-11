import cv2
import numpy as np

def detect_disease(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate how dark the leaf is
    mean_intensity = np.mean(gray)

    if mean_intensity < 120:
        return "Diseased"
    else:
        return "Healthy"
