from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    command = msg.split()[0]
    if command == 'c':
        try:
            resp.message(f"wa.me/91{msg.split()[1]}")
        except Exception as e:
            print(e)
            resp.message(f"Invalid syntax")
    else:
        resp.message(f"hello {msg}")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
