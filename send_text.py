import twilio
import twilio.rest

from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "XXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXX"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+3806XXXXX",
    from_="+14158516XXX",
    body="Hello from Python! from Ksu")

print(message.sid)