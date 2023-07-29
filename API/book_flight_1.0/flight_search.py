from requests import get
from flight_data import FlightData
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def getupdate(self,info):
        par={
            "term":info,
            "location_types":"city"
        }
        h={
            "apikey":"YOUR_API_KEY"
        }
        l="https://tequila.kiwi.com/locations/query"
        res=get(url=l,params=par,headers=h)
        res.raise_for_status()
        print(res.text)
        code=res.json()
        # ["locations"][0]["code"]
        print(code)
        return code
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": "YOUR_API_KEY",}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = get(
            url="https://tequila.kiwi.com/v2/search",
            headers=headers,
            params=query,
        )

        data = response.json()["data"][0]
        # pprint(data)

        fd = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )# type: ignore        
        print(f"{fd.destination_city}: £{fd.price}")
        return fd
    