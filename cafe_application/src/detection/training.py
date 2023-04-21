import os

import cv2
import numpy as np
from PIL import Image


class Training:
    def __init__(self) -> None:
        self.image_dir = r'cafe_application\img\faces'
        self.training_dir = r'cafe_application\classifiers'
        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.face_cascade = cv2.CascadeClassifier(r'cafe_application\src\detection\haarcascade_frontalface_default.xml')

    def train(self, customerID):
        image_path = os.path.join(self.image_dir, customerID)
        labels = []
        faceSamples = []
        for i in range(40):
            img_PIL = Image.open(fr'{image_path}\{i:03}.jpg').convert('L')
            img_numpy = np.array(img_PIL, 'uint8')

            label = int(customerID[3:])
            faces = self.face_cascade.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y+h, x:x+w])
                labels.append(label)

        self.model.train(faceSamples, np.array(labels))
        self.model.save(fr'{self.training_dir}\{customerID}.xml')
