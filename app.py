from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<num>", methods=["GET"])
def get_calcs(num):
    try:
        num_int = int(num)
        return {
            "dec": num_int-1,
            "hex": hex(num_int)
        }, 200
    except:
        return "Error when performing calculations.", 400