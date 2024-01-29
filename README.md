# Spam Predictor API
A minimal Flask web application.
## Getting Started

These instructions will help you get your API up and running.

### Prerequisites

- Node.js installed
- npm (Node Package Manager) installed
- axios library installed (you can install it using `npm install axios`)

### Example
```js
const axios = require('axios');

async function makePrediction(commentText) {
  try {
    const response = await axios.post('https://flask-production-b980.up.railway.app/predict', {'comment': commentText});
    const responseData = response.data;
    console.log('Prediction:', responseData);
  } catch (error) {
    console.error('Error making prediction:', error.message);
  }
}

// Example usage
const commentText = 'This is a sample comment.';
makePrediction(commentText);
```
### API Documentation
----------------------
Document the available endpoints, request parameters, and response format

#### Endpoint: 
- POST /predict
#### Request Body:
- comment (string): The text comment for prediction.
#### Response:
- result (bool): The prediction result.
  ```json
  {
    "result": true
  }
  ```

For a step-by-step guide to deploying on [Railway](https://railway.app/?referralCode=alphasec), see [this](https://alphasec.io/how-to-deploy-a-python-flask-app-on-railway/) post, or click the button below.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/igzwwg?referralCode=alphasec)
