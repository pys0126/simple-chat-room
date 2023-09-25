from flask import Flask
from flask_cors import CORS
from controller.chat_controller import chat_blueprint

app: Flask = Flask(__name__)
CORS(app=app)

app.register_blueprint(chat_blueprint, url_prefix="/chat")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9898, debug=True)