from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Gather

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

    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        if choice == '1':
            resp.say('You selected sales. Good for you!')
            return str(resp)
        elif choice == '2':
            resp.say('You need support. We will help!')
            return str(resp)
        elif choice == '3':
            resp.say('You are the third option')
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    resp.redirect('/voice')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
