from flask import Flask, render_template, url_for
import requests
from flask import request as req
from waitress import serve

# Starting the webapp
app = Flask(__name__)

# Creating Routes
@app.route('/', methods=['GET',"POST"])
def home():

    if req.method == 'POST':
        import requests

        API_URL = "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": req.form["data"],
        })[0]

        return render_template("index.html", result = output["summary_text"])
    else:
        return render_template("index.html")

if __name__ == "__main__":
    print("Server is up and running on PORT 3000")
    serve(app, host='0.0.0.0', port=3000)