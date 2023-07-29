from requests import post
from datetime import datetime
APP_ID="YOUR_APP_ID"
API_KEY="YOUR_API_KEY"
UID="YOUR_UID"
h1={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":UID
}
par1={
    "query":input("Tell me which exercise you did: "),#"ran 3 miles"
    "gender":"male",
    "weight_kg":float("YOUR_WEIGHT_kG"),
    "height_cm":float("YOUR_HEIGHT_cm"),
    "age":float("YOUR_AGE"),
}
l1="https://trackapi.nutritionix.com/v2/natural/exercise"
r=post(url=l1,json=par1,headers=h1)
inf=r.json()
print(inf)
info=inf["exercises"]
n=datetime.now()
d=n.strftime("%d/%m/%Y")
t=n.strftime("%H:%M:%S")
for i in info:
    par2={
        "workouts":{
            "Date":d,
            "Time":t,
            "Exercise":str(i["name"]).title(),
            "Duration":i["duration_min"],
            "Calories":i["nf_calories"]
        }
    }
    print(par2)
    h2={
        "Authorization":"YOUR_ACCESS_TOKEN"
    }
    l2="https://api.sheety.co/040cbe9f6efbccc8aa023c1ebfb85531/workoutTracking/workouts"
    res=post(url=l2,json=par2,headers=h2)
    print(res.text)
    
