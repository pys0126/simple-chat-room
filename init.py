from flask_cors import CORS
from flask import Flask, render_template
from config.project_config import ProjectConfig
from controller.chat_controller import chat_blueprint
from controller.user_controller import user_blueprint
from exception.custom_exception import CustomException
from exception.custom_exception import exception_handle

app: Flask = Flask(__name__)
app.secret_key = ProjectConfig.secret_key
CORS(app=app)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


app.register_blueprint(chat_blueprint, url_prefix="/chat")
app.register_blueprint(user_blueprint, url_prefix="/user")

app.register_error_handler(CustomException, exception_handle)

if __name__ == "__main__":
    app.run()
