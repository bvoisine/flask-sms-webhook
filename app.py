from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello from Flask on Render!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Incoming JSON:", data)
    
    # Later: route to AI agent or action handler
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(debug=True)
