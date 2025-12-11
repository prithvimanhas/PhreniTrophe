import numpy as np
import cv2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

class ImageRecognizer:
    def __init__(self):
        print("🔍 Loading MobileNetV2 model...")
        self.model = MobileNetV2(weights="imagenet")

    def recognize_file(self, path):
        img = image.load_img(path, target_size=(224, 224))
        return self._predict(img)

    def recognize_camera(self):
        cap = cv2.VideoCapture(0)
        print("📸 Press SPACE to capture.")
        while True:
            ret, frame = cap.read()
            cv2.imshow("Capture Food", frame)
            if cv2.waitKey(1) & 0xFF == 32:
                img = cv2.resize(frame, (224, 224))
                cap.release()
                cv2.destroyAllWindows()
                return self._predict(image.array_to_img(img))

    def _predict(self, img):
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = self.model.predict(x)
        decoded = decode_predictions(preds, top=5)[0]
        for _, label, prob in decoded:
            print(f"🧠 {label} ({prob*100:.2f}%)")
        likely = [lbl for _, lbl, p in decoded if p > 0.2]
        return likely or [decoded[0][1]]
