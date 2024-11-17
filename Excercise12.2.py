#Familiarize yourself with the OpenWeather weather
# API at: https://openweathermap.org/api. Your task
# is to write a program that asks the user for the
# name of a municipality and then prints out the
# corresponding weather condition description text
# and temperature in Celsius degrees. Take a good
# look at the API documentation. You must register
# for the service to receive the API key required for
# making API requests. Furthermore,
# find out how you can convert Kelvin degrees into Celsius.



import json
import requests


API_key=("23ed1ac24a7a5a0f7998cce76399111e")
city_name=input("Enter the name of the city: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"



try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        data=json_response['main']
        for key, value in data.items():
            if key == 'temp' or key == 'feels_like' or key == 'temp_min' or key == 'temp_max':
                print(f"{key.capitalize()}: {value} degrees Celcius")
            elif key == 'pressure':
                print(f"{key.capitalize()}: {value} mb")
            elif key == 'humidity':
                print(f"{key.capitalize()}: {value} %RH")
            elif key == 'sea_level' or key == 'grnd_level':
                print(f"{key.capitalize()}: {value} meters")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")