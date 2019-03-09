#Import the AfricasTalking SDK into your app
import africastalking

#Create your credentials
username = "sandbox name"
apikey = "YOUR API KEY"

#Initialize the SDK
africastalking.initialize(username, apikey)

#Get the SMS service
sms = africastalking.SMS

#Define some options that we will use to send the SMS
recipients = ['YOUR NUMBER']
message = 'I\'m a John Doe and its ok, I sleep all night and I work all day'
sender = 'SENDER NAME'

#Send the SMS
try:
    #Once this is done, that's it! We'll handle the rest
    response = sms.send(message, recipients,sender)
    print(response)
except Exception as e:
    print(f"Houston, we have a problem {e}")
