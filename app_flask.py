#!/usr/bin/env python3
#
from flask import Flask, request, jsonify


app = Flask(__name__)
app.json_provider_class.ensure_ascii = False


@app.get("/api/translate_v1")
def translate_v1():
    text = request.args.get("text")
    response = jsonify({"message": f"{text}"})

    return response


@app.post("/api/translate_v2")
def translate_v2():
    text = request.json["text"]
    response = jsonify({"message": f"{text}"})

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
