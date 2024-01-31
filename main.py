from flask import Flask, render_template
from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

loaded_model = pickle.load(open('model.pkl', 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def predictHelper(comment):
    if comment:
        new_comment = loaded_vectorizer.transform([comment])
        prediction = loaded_model.predict(new_comment)
        return True if prediction[0] == 1 else False
    else:
        return "Internal Server Error"


@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.get_json()
    comment = data.get('comment', '')
    result = predictHelper(comment)
    return jsonify({'result': result})


@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=5000)
