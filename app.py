from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvenuto su WebVision!"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
