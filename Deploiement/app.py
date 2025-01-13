import os
from flask import Flask, request, render_template
from fileinput import filename
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

UPLOAD_FOLDER = './static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


model = load_model('models/pneumonia-x-ray-detection.h5')
def predict_image(image_path) :
    image = load_img(image_path, target_size = (180, 180))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis = 0)
    image_array = image_array / 255.0
    predictions = model.predict(image_array, verbose = 0)

    return 'PNEUMONIA' if predictions[0] >= 0.5 else 'NORMAL'



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/predict', methods = ['GET','POST'])
def predict() :
    print(request.files)
    if request.method == 'POST' :
        if 'file' not in request.files :
            return "Aucun fichier téléchargé", 400

        file = request.files['file']
        if file.filename == '' :
            return "Aucun fichier sélectionné", 400
        
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')) :
            return "Type de fichier non supporté. Veuillez télécharger une image PNG, JPG ou JPEG.", 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        try :
            prediction = predict_image(file_path)
        except Exception as e :
            return "Impossible de lire l'image", 500

        return render_template('index.html', prediction = prediction, image_path = file_path)

    return render_template('index.html')

if __name__ == '__main__' :
    app.run(debug = True, host = '0.0.0.0', port = 5000)