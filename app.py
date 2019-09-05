from flask import Flask, request, send_from_directory
from twilio.twiml.voice_response import VoiceResponse, Gather, Sip, Dial, Play

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
                resp.say('You are down with the sickness!')
                resp.play('http://thinkathon-api-heroku.herokuapp.com/dwts', loop=10)
            elif choice == '2':
                resp.say('You are a freak on a leash!')
                resp.play('http://thinkathon-api-heroku.herokuapp.com/davis', loop=2)
            elif choice == '3':
                resp.say('Skeebeeebabeebop hell yeah Dave!')
                resp.play('http://thinkathon-api-heroku.herokuapp.com/dave', loop=10)

            dial.sip('sip:8304765664@wap.thinq.com?X-account-id=11132&X-account-token=67807f4f358d097b53c595e3fdb5be570bf8477d')
            resp.append(dial)
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    resp.redirect('/voice')
    return str(resp)


@app.route('/dwts', methods=['GET'])
def dwts():
    return send_from_directory('static', 'sickness.mp3')


@app.route('/davis', methods=['GET'])
def davis():
    return send_from_directory('static', 'davis.mp3')


@app.route('/dave', methods=['GET'])
def dave():
    return send_from_directory('static', 'dmb.mp3')

if __name__ == "__main__":
    app.run(debug=True)
