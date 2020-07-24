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
    a,c,d,r,dp,rp=cv.state(msg)
    # Create reply
    resp = MessagingResponse()
    resp.message("acha: {}".format(msg))
    resp.message(c+'\n'+a+'\n'+r+'\n'+rp+'\n'+d+'\n'+dp)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
