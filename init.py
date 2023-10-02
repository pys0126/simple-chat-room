from flask_cors import CORS
from config.project_config import ProjectConfig
from controller.chat_controller import chat_blueprint
from controller.user_controller import user_blueprint
from exception.custom_exception import CustomException
from exception.custom_exception import exception_handle
from flask import Flask, render_template, session, request

app: Flask = Flask(__name__)
app.secret_key = ProjectConfig.secret_key
CORS(app=app)


@app.before_request
def before_api_request():
    if not request.path.endswith("/user/login") and not request.path.endswith("/user/register"):
        if not session.get("user"):
            return render_template("login.html")


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index() -> str:
    return render_template("index.html")


@app.route("/message", methods=["GET"])
def message() -> str:
    return render_template("message.html")


app.register_blueprint(chat_blueprint, url_prefix="/chat")
app.register_blueprint(user_blueprint, url_prefix="/user")

app.register_error_handler(CustomException, exception_handle)

if __name__ == "__main__":
    app.run()
