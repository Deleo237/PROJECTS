#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime,timedelta
from notification_manager import NotificationManager


ORIGIN_CITY_IATA = "LON"
d=DataManager()
fs=FlightSearch()
nm=NotificationManager()
info=d.getinfo()
pprint(info)

for inf in info:
    if inf["iataCode"]=="":
        inf["iataCode"]=fs.getupdate(inf["city"])
print(info)
d.data=info
d.putinfo()

tom = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in info:
    flight = fs.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tom,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        nm.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )