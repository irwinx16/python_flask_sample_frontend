from flask import Flask, render_template, request, json
import requests

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    WEATHER_KEY = '8f7e90ae66919f9651f80c29d46c0a45'
    city = 'Chicago'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, WEATHER_KEY)
    response = requests.get(url).json()
    k_temp = response['main']['temp']
    f_temp = int(((k_temp - 273.15) * 1.8) + 32)
    c_temp = int(k_temp - 273.15)
    icon   = response['weather'][0]['icon']
    desc   = response['weather'][0]['description']

    return render_template('index.html', temp_f=f_temp, temp_c=c_temp, icon=icon, description=desc)

# Resume Page
@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)
