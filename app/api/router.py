from flask import request

from api import app
from api import controllers as con
from api import service


@app.before_first_request
def init():
    service.init()


@app.route("/health")
def health():
    return con.health()


@app.route("/image", methods=["POST"])
def image():
    img_b64 = request.json["image"]
    return con.image(img_b64)