from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<num>", methods=["GET"])
def get_calcs(num):
    num_int = int(num)
    return {
        "dec": num_int-1,
        "hex": hex(num_int)
    }, 200
