import os
import time

from PIL import Image
import torch
from torchvision import models
from typing import Tuple
import yaml

from .parser import ConfigParser
from .transform import get_transform
from .imagenet import classes


cfg = None
model = None
preprocessor = None


def init():
    _load_config()
    _load_model()
    _load_preprocessor()


def predict(inp_pil):
    print(f"[INFO] image size: {inp_pil.size}")
    inp = preprocessor(inp_pil).unsqueeze(0)
    pred = model(inp.to(cfg.device))
    pred_id = pred[0].argmax().item()
    print(f"[INFO] predicted class id  : {pred_id}")
    print(f"[INFO] predicted class name: {classes[pred_id]}")
    return pred_id, classes[pred_id]


def _load_config():
    global cfg
    cfg_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "config.yml",
    )
    with open(cfg_path) as f:
        cfg = yaml.safe_load(f)
    cfg = ConfigParser(cfg)
    print("[INFO] Device: ", cfg.device)


def _load_model():
    global model
    if cfg.arch == "resnet18":
        model = models.resnet18(pretrained=True)
    else:
        raise NotImplementedError(f"Error: {cfg.arch} is not implemented")

    model.to(cfg.device)
    model.eval()


def _load_preprocessor():
    global preprocessor
    preprocessor = get_transform()

