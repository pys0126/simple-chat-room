from flask import Flask
from flask_cors import CORS
from config.project_config import ProjectConfig
from controller.chat_controller import chat_blueprint
from controller.user_controller import user_blueprint
from exception.custom_exception import CustomException
from exception.custom_exception import exception_handle

app: Flask = Flask(__name__)
app.secret_key = ProjectConfig.secret_key
CORS(app=app)


app.register_blueprint(chat_blueprint, url_prefix="/chat")
app.register_blueprint(user_blueprint, url_prefix="/user")

app.register_error_handler(CustomException, exception_handle)

if __name__ == "__main__":
    app.run()
