from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from getRedditPost import getRedditPost

accountSID = '*******************************'
authToken = '********************************'

client = Client(accountSID, authToken)

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def send_reddit_post():
    number = request.form['From']
    body = request.form['Body']

    resp = MessagingResponse()

    redditPost = getRedditPost(body)
    if ('.jpg' or '.png') in redditPost:
        splitURL = redditPost.split("(#)")
        print(splitURL)
        msg = resp.message(splitURL[0])
        msg.media(splitURL[1])
    else:
        msg = resp.message(redditPost)

    return str(resp)

if __name__ == "__main__":
    app.run()
