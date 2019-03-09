#Import the AfricasTalking SDK into your app
import africastalking

#Create your credentials
username = "doe"
apikey = "63c37ff8dba1ed8a8a1533c9ad1636da6e4896b0aa8e9990be11b368a33f74e8"

#Initialize the SDK
africastalking.initialize(username, apikey)

#Get the SMS service
sms = africastalking.SMS

#Define some options that we will use to send the SMS
recipients = ['+254733745544']
message = 'I\'m a John Doe and its ok, I sleep all night and I work all day'
#sender = 'DAENJEL'

#Send the SMS
try:
    #Once this is done, that's it! We'll handle the rest
    response = sms.send(message, recipients)
    print(response)
except Exception as e:
    print(f"Houston, we have a problem {e}")