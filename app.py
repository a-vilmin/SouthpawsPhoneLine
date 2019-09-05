from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Sip, Dial

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    gather = Gather(num_digits=1, action='/gather')
    gather.say('Welcome to Scat Phone, press 1, 2, or 3 for some excellent scats.')
    resp.append(gather)

    # redirect if no input
    resp.redirect('/voice')
    return str(resp)


@app.route('/gather', methods=['GET', 'POST'])
def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = VoiceResponse()
    dial = Dial()

    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        if choice in ['1', '2', '3']:
            if choice == '1':
                resp.say('You selected sales. Good for you!')
            elif choice == '2':
                resp.say('You need support. We will help!')
            elif choice == '3':
                resp.say('You are the third option')

            dial.sip('sip:8304765664@wap.thinq.com?X-account-id=11132&X-account-token=67807f4f358d097b53c595e3fdb5be570bf8477d')
            resp.append(dial)
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    resp.redirect('/voice')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
