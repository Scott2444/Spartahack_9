from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
    return[{"district":"1","party":"democrat"},
            {"district":"2","party":"republican"}]

if __name__ == "__main__":
    app.run(debug=True)
