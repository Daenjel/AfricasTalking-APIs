#Import the Africa's Talking SDK
import africastalking

#Set up your credentials
username = "sandbox"
api_key = "fbba33f71f5f671f7b1043ff721eec2140c29d6d4e212c23f9c4edcec6b6b898"

#Initialize the SDK
africastalking.initialize(username, api_key)

#Define the Payment service
payments = africastalking.Payment

#Set your product name
product_name = "Swahili"

#Set the phone number you want and set it to the international format
phone_number = "+254733745544"

#Set the 3 letter ISO currency code and checkout amount
currency_code = "KES"
amount = 100.0

#You can add in your own metadata which will be resent back to you
#For the final payment notification
metadata = {
    "agentId": "",
    "productId": ""
}

#Time to send and we'll handle the rest
try:
    res = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
    print(res)
except Exception as e:
    print(f"Houston we have a problem {e}")
