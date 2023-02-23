import requests as reqs

weather_api_key = "enter your api here" # Pls enter your own Api by OpenWeather Website
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter your city name : ")
print("Fetching the data..Please Wait")
complete_url = base_url + "appid=" + weather_api_key + "&q=" + city_name
response = reqs.get(complete_url)
x = response.json()
print("Alright, got it !! ")
            
if  x["cod"] != "404":
    y = x['main']
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    #z = x["weather"]
    # weather_description = z[0]["description"]
    print("According to OpenWeather API,")
    print(f"Temperature in {city_name} is around) {str(current_temperature)} Kelvin")
    print(f'Pressure in {city_name} is around {str(current_pressure)} hecto Pascals')
    print(f'Humidity in {city_name} is around {str(current_humidiy)} Percentage.')
                
             
else:
    print("Something went wrong!!")
