# Import the Africa's Talking module here
import africastalking

#Define credentials here
username = "sandbox NAME"
api_key = "YOUR API KEY"

#Authenticate with the service
africastalking.initialize(username, api_key)

#Define the airtime service
airtime = africastalking.Airtime 

#Define user variables
phone_number = "YOUR PHONE NUMBER"
amount = "300"
currency_code = "KES"

#Send the airtime!
response = airtime.send(phone_number = phone_number, amount = amount, currency_code = currency_code)
print(response)
