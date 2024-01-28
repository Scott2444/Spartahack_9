from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
    return[{"district":"Michigan1","party":"democrat"},
            {"district":"Michigan2","party":"republican"},
            {"district":"Ohio3","party":"republican"}]

if __name__ == "__main__":
    app.run(debug=True)
