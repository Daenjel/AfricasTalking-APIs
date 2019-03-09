#Import the Africa's Talking SDK
import africastalking

#Set up your credentials
username = "sandbox NAME"
api_key = "YOUR API KEY"

#Initialize the SDK
africastalking.initialize(username, api_key)

#Define the Payment service
payments = africastalking.Payment

#Set your product name
product_name = "PRODUCT NAME"

#Set the phone number you want and set it to the international format
phone_number = "PHONE NUMBER"

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
