from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello and thanks for calling the Southpaws voicemail line. Please leave your message after the beep. Thank you and Fuck the Cubs!")

    response.record()
    response.hangup()

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
