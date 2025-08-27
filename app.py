from flask import Flask, request

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_webhook():
    data = request.get_json()
    
    print("📨 Incoming Webhook:")
    print(data)  # <--- THIS will print the JSON to the Render logs

    if data and "data" in data and "payload" in data["data"]:
        payload = data["data"]["payload"]
        from_number = payload.get("from")
        to_number = payload.get("to")
        message_text = payload.get("text")

        print(f"From: {from_number} | To: {to_number} | Message: {message_text}")

    return "OK", 200
