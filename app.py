from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        req_data = request.get_json()

        # user_selection = req_data["selection"]

        # response_data = ""

        # if user_selection == "a":
        #     response_data = "Analysis on a"
        # elif user_selection == "b":
        #     response_data = "Analysis on b"
        # else:
        #     response_data = "Unrecognized input"

        return {
            'request': req_data
            # 'response': response_data
        }
    except Exception as e:
        return {"error": e}
