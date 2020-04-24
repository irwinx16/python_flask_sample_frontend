from flask import Flask, render_template, request, json
import requests

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    WEATHER_KEY = '8f7e90ae66919f9651f80c29d46c0a45'
    city = 'Chicago'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8f7e90ae66919f9651f80c29d46c0a45'.format(city)
    response = requests.get(url).json()
    k_temp = response['main']['temp']
    f_temp = int(((k_temp - 273.15) * 1.8) + 32)
    c_temp = int(k_temp - 273.15)
    print(" Temperature : ", f_temp, " Degree Fahrenheit")
    print(" Temperature : ", c_temp, " Degree Celsius")




    # breakpoint()

    return render_template('index.html', temp_f=f_temp, temp_c=c_temp)

# Resume Page
@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)
