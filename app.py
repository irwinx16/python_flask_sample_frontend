from flask import Flask, render_template, request, json
import requests

app = Flask(__name__)

# Set development/production environment
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False


# Home Page
@app.route('/')
def index():
    WEATHER_KEY = '8f7e90ae66919f9651f80c29d46c0a45'
    city = get_geolocation()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, WEATHER_KEY)
    response = requests.get(url).json()
    k_temp = response['main']['temp']
    f_temp = int(((k_temp - 273.15) * 1.8) + 32)
    c_temp = int(k_temp - 273.15)
    icon   = response['weather'][0]['icon']
    desc   = response['weather'][0]['description'].title()

    return render_template('index.html', temp_f=f_temp, temp_c=c_temp, icon=icon, description=desc, city=city)


# Resume Page
@app.route('/resume')
def resume():
    return render_template('resume.html')

# Geo-Location
def get_geolocation():
    url = 'http://ip-api.com/json/'
    response = requests.get(url).json()
    city = response['city']
    return city


if __name__ == '__main__':
    app.run()
