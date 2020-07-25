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
    a,c,d,r,dp,rp,l1,l2,l3,l4=cv.state(msg)
    # Create reply
    resp = MessagingResponse()
    resp.message("acha: {}".format(msg))
    if l2 == 'no data found' or l2=='not found':
        resp.message(a+'\n'+c+'\n'+d+'\n'+r+'\n'+dp+'\n'+rp)
    else:
        resp.message(a+'\n'+c+'\n'+d+'\n'+r+'\n'+dp+'\n'+rp+'\n'+l1+'\n'+l2+'\n'+l3+'\n'+l4)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
