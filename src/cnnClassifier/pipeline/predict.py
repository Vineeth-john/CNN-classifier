import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        
        # Get raw probabilities from model
        predictions = model.predict(test_image)
        
        # Get the highest confidence score
        confidence = np.max(predictions)
        print(f"Model confidence: {confidence:.3f}")
        print(f"Raw predictions: {predictions[0]}")
        
        # Lower threshold to catch more uncertain predictions
        if confidence < 0.5:  # 50% threshold (lowered from 0.7)
            prediction = 'unknown'
            print(f"Low confidence ({confidence:.3f}), classifying as unknown")
        else:
            # Only trust the prediction if confident
            result = np.argmax(predictions, axis=1)
            print(f"Predicted class index: {result[0]}")
            print(f"Confidence level: {confidence:.3f}")
            
            if result[0] == 0:
                prediction = 'ripe_1'
            elif result[0] == 1:
                prediction = 'rotten_1'
            elif result[0] == 2:
                prediction = 'unripe_1'
            else:
                prediction = 'unknown'
        
        return [{ "image" : prediction}]