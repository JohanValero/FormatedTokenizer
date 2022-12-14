import os
import json
from flask import Flask, request
from lexer import pre_process_text
vApp = Flask(__name__)

@vApp.route("/")
def pre_process_address():
    vAddress = request.args.get("address", default = "", type = str)
    vFormated, vTokens = pre_process_text(vAddress)

    vJsonRespond = {
        "original_address": vAddress,
        "standar_address": " ".join(vFormated),
        "token": "".join(vTokens)
    }

    return json.dumps(vJsonRespond)

vPort = os.getenv("PORT")
print("PORT:", vPort)

#vApp.run(host = "0.0.0.0", port = vPort)