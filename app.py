from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, MessagingResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello and thanks for calling the Southpaws voicemail line. Please leave your message after the beep. Thank you and Fuck the Cubs!")

    response.record()
    response.hangup()

    return str(response)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Message recieved, thanks for contributing to the Darren Rovell fan data survey. Your input is valuable for knowing what the official soft drink of 9/11 will be.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
