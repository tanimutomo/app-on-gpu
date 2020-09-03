import base64
import io

from flask import jsonify
from PIL import Image

import api.service as service


def health():
    return jsonify({"message": "hello"}), 200


def image(inp_b64):
    print("\n---------------------------------------------")
    inp_io = io.BytesIO(base64.b64decode(inp_b64))
    inp_io.seek(0)
    inp_pil = Image.open(inp_io)
    inp_pil = inp_pil.convert("RGB")

    pred_id, pred_name = service.predict(inp_pil)
    print("---------------------------------------------\n")

    return jsonify({
        "id": pred_id,
        "name": pred_name,
    }), 200

