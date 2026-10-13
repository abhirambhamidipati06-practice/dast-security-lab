from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>DAST Security Lab</h1><p>This is a sample web app for dynamic security testing.</p>"

@app.route("/about")
def about():
    return "<p>A minimal Flask app used to demonstrate automated DAST scanning with OWASP ZAP.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
