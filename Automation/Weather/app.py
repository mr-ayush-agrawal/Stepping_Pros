from apiKey import API_KEY
import requests

Base_URL = f'https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}'

city = input('Enter the city name : ')
# city = 'Maihar'
# city = 'Chennai'
request_URL = Base_URL+f'&q={city}'

response = requests.get(request_URL)

if response.status_code == 200 :
    # Success
    data = response.json()
    # print(data)

    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    print('Weather = ', weather)
    print('Temprature = ', round(temp-273))
else :
    print('Error Occured')
