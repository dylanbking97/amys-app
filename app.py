from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from flask import Flask, request, redirect
from lxml import html
import requests
import untangle

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


# client = Client(
#     os.getenv("ACCOUNT_SID"), 
#     os.getenv("AUTH_TOKEN")
#     )

# for message in client.messages.list():
#     print(str(message.body)[38:])


# msg = client.messages.create(
#     from_= os.getenv("TWILIO_PHONE"),
#     to=os.getenv("MOM_PHONE"),
#     body="hello from Python 2",
# )

# def get_directions(route):

#     legs = []
#     for l in route.leg:
#         if l['mode'] == "Walk":
#             # using f strings requires Python 3.6 or later
#             # direction = f"Walk {l.time_distance.distance.cdata} miles to {l.to.description.cdata}."
#             direction = "Walk " + str(l.time_distance.distance.cdata) \
#                         + "miles to " + str(l.to.description.cdata)    \
#                         + " (" + str(l.time_distance.duration.cdata) + " minutes)"
#             legs.append(direction)
#         else:
#             board = "Board " + str(l.route.name.cdata) \
#                     + " at " + str(l.time_distance.startTime.cdata)

#             getoff = "Get off at " + str(l.to.description.cdata) \
#                     + " (Stop ID " + str(l.to.stopId.cdata) + ")"
#             legs.append(board)
#             legs.append(getoff)       

#     return legs
 
# def get_route(dest):

#     html = requests.get("https://developer.trimet.org/ws/V1/trips/tripplanner?" 
#                     + "fromCoord=" + os.getenv("HOME_COORDS")
#                     #+ "fromplace=" +"pdx"
#                     + "&toplace=" + dest  # replace this with dest
#                     + "&appId=" + os.getenv("TRIMET_ID"))

#     tree = untangle.parse(html.text).response

#     # if there is an error in the request, return the error message to sender
#     # if valid request, get the quickest route
#     try:
#         return str(tree.error.message.cdata)
#     except:
#         route = tree.itineraries.itinerary[0]
    
#     directions = get_directions(route)

#     return directions[0]


@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    dest = request.values.get('Body', None)

    #msg = str(get_route(str(dest)))
    desty = "dest"
    # Start our TwiML response
    resp = MessagingResponse()
    msg = str(desty)
    resp.message(msg)

    return str(resp)
    

if __name__ == "__main__":
    app.run(debug=True)

