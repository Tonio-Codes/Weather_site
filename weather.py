from __future__ import print_function
import time
import weatherapi
from weatherapi.rest import ApiException
from pprint import pprint


configuration = weatherapi.Configuration()
configuration.api_key['key'] = open("api_key","r").read()


# create an instance of the API class
api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
#q = '92683' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.
#dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format


def create_api_instance():
    configuration = weatherapi.Configuration()
    configuration.api_key['key'] = open("api_key","r").read()
    return weatherapi.APIsApi(weatherapi.ApiClient(configuration))


def get_forecast(api_instance,location):
    forecast = {"high": 0,
                "low": 0,
                "current_temp": 0,
                "wind_mph": 0,
                "country": "",
                "name": "",
                "region": "",
                "local_time": "",
                "text": "",
                "picture": "",
                "location" : ""
                }
    
    api_forecast = api_instance.forecast_weather(location,1)
    print(api_forecast)
    forecast["high"] = api_forecast["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
    forecast["low"] = api_forecast["forecast"]["forecastday"][0]["day"]["mintemp_f"]
    forecast["wind_mph"] = api_forecast["current"]["wind_mph"]
    forecast["current_temp"] = api_forecast["current"]["temp_f"]
    forecast["region"] = api_forecast["location"]["region"]
    forecast["country"] = api_forecast["location"]["country"]
    forecast["name"] = api_forecast["location"]["name"]
    forecast["local_time"] = api_forecast["location"]["localtime"]
    forecast["text"] = api_forecast["current"]["condition"]["text"]
    forecast["picture"] = api_forecast["current"]["condition"]["icon"]
    forecast["location"] = f"{api_forecast["location"]["name"]}, {api_forecast["location"]["region"]}"

    return forecast



if __name__ == "__main__":
    try:
        api_instance = create_api_instance()
        forecast = api_instance.forecast_weather(92683,1)
        print(forecast)
    except ApiException as e:
        print("Exception when calling APIsApi->astronomy: %s\n" % e)
