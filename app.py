from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

cluster_arn = "REPLACEME"
secret_arn = "REPLACEME"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+auroradataapi://:@/REPLACEME"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "connect_args": {"aurora_cluster_arn": cluster_arn, "secret_arn": secret_arn}
}

db = SQLAlchemy(app)
