import twilio
import twilio.rest

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACea2cfe2dda84be1d8981454dab1e08e7"
# Your Auth Token from twilio.com/console
auth_token  = "db30ccc290e8da5d2392abb67503a5be"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+380639746386",
    from_="+14158516077",
    body="Hello from Python! from Ksu")

print(message.sid)