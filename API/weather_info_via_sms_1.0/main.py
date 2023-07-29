#API Keys, Authentication, Environment Variables and Sending SMS
from twilio.rest import Client
from requests import get
accid="YOUR_ACCID"
auth="YOUR_AUTH"
K="YOUR_APPID"
LA=4.160185 #The latitude of your area
LO=9.284477 #The longitude of your area
par={
    "lat":LA,
    "lon":LO,
    "appid":K,
    "exclude":"current,minutely,daily"
}
ans= get(url="https://api.openweathermap.org/data/2.5/onecall", params=par)
print(ans.status_code)
ans.raise_for_status()
data=ans.json()
print(data)
wr=False
for i in range(12):
    dd=data["hourly"][i]["weather"][0]["id"]
    print(dd)
    if int(dd)>400:
        wr=True
if wr:
    print("Take your umbrella with you")
    client = Client(accid, auth)
    message = client.messages \
        .create(
            body="Take your umbrella with you\nRain will fall, you will remain in Deleo's place and wouldn't be able to come home on time.",
            from_='YOUR_TWILIO_VIRTUAL_NUMBER',
            to='YOUR_TWILIO_VERIFIED_NUMBER'
        )
    print(message.status)
    
    
# print(data)
#Writting env on teminal gives you enviroment variables
#export ACCID=This is not seen by users
#export AUTH=this is wield

