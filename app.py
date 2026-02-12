from flask import Flask, render_template, request, jsonify
from ai_agent import ai_agent
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    answer = ai_agent(data["question"])
    return jsonify({"answer": answer})

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)

