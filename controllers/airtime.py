# Import the Africa's Talking module here
import africastalking

#Define credentials here
username = "sandbox"
api_key = "fbba33f71f5f671f7b1043ff721eec2140c29d6d4e212c23f9c4edcec6b6b898"

#Authenticate with the service
africastalking.initialize(username, api_key)

#Define the airtime service
airtime = africastalking.Airtime 

#Define user variables
phone_number = "+254733745544"
amount = "300"
currency_code = "KES"

#Send the airtime!
response = airtime.send(phone_number = phone_number, amount = amount, currency_code = currency_code)
print(response)