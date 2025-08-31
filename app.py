from flask import Flask, request

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_webhook():
    # Twilio sends URL-encoded form data, not JSON
    from_number = request.form.get('From')
    to_number = request.form.get('To')
    message_text = request.form.get('Body')

    print("📨 Incoming Twilio SMS:")
    print(f"From: {from_number} | To: {to_number} | Message: {message_text}")

    return "OK", 200
