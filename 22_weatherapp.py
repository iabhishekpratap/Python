import requests

API_KEY='xxxxxxxxxx'
city_name=input("enter name of the city : ")

url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

respo= requests.get(url)

if respo.status_code==200:
    weather_data =respo.json()

    weather_discription=weather_data['weather'][0]['description']
    temp=weather_data['main']["temp"]-273.15
    print(weather_discription,temp)


