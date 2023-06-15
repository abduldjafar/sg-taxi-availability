from time import sleep
import requests
import datetime


class ApiCall(object):
    def __init__(self):
        self.url = "https://api.data.gov.sg/v1/transport/taxi-availability"
    

    def geocode(self,longitude, latitude):
        url =  "https://geocode.maps.co/reverse?lat={}&lon={}".format(str(latitude),str(longitude))
        data = {}
        try:
            response = requests.get(url)
            data = response.json()
            sleep(1)
        except:
            pass
        return data

    def get_data(self):
        response = requests.get(self.url)
        return response.json()

    def get_cordinates_dataset(self):
        data = self.get_data()
        cordinates = data["features"][0]["geometry"]["coordinates"]
        return cordinates
