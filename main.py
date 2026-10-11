import requests
import os
from twilio.rest import Client

client = Client(account_sid, auth_token)

account_sid = os.environ.get("TW_ASID")
auth_token = os.environ.get("TW_ATK")
api_key = os.environ.get("OWM_API")

parameters = {
    "lat": -22.823450,
    "lon": -43.058868,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather_data = response.json()
gonna_rain = False
for i in range(0, weather_data['cnt']):
    if weather_data['list'][i]['weather'][0]['id'] < 700:
        gonna_rain = True
        break

if gonna_rain:
    print("Vai chover!")
    #whatsapp
    # message = client.messages.create(
    #     from_='whatsapp:+14155238886',
    #     body="It's going to rain today. Remember to bring an umbrella ☂️",
    #     to='whatsapp:+5521966095744'
    # )

    # print(message.sid)
    #sms
    # message = client.messages \
    #     .create(
    #     body="Its going to rain today. Remember to bring a umbrella ☂️",
    #     from_='+19069703443',
    #     to='+5521979310556'
    # )
    #
    # print(message.sid)
