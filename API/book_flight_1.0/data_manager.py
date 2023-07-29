from requests import get,put
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data={}
    def getinfo(self):
        self.h={
            "Authorization":"YOUR_ACCESS_TOKEN"
        }
        lg="https://api.sheety.co/040cbe9f6efbccc8aa023c1ebfb85531/flightInfo/prices"
        res=get(url=lg,headers=self.h)
        d=res.json()
        print(f"{d}\n\n\n")
        self.data=d["prices"]
        return self.data
    def putinfo(self):
        for inf in self.data:
            par={
                "price":{
                    "iataCode": inf["iataCode"]
                }
            }
            lp=f"https://api.sheety.co/040cbe9f6efbccc8aa023c1ebfb85531/flightInfo/prices/{inf['id']}"
            res=put(url=lp,json=par,headers=self.h)
            print(res.text)