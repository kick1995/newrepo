from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import coviddata as cv
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    a,c,d,r=cv.state(msg)
    # Create reply
    resp = MessagingResponse()
    resp.message("acha: {}".format(msg))
    resp.message(a)
    resp.message(c)
    resp.message(d)
    resp.message(r)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)