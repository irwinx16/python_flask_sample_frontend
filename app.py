from flask import Flask, render_template, request, json
import requests
import smtplib

app = Flask(__name__)


# Home Page
@app.route('/')
def index():

    WEATHER_KEY = '8f7e90ae66919f9651f80c29d46c0a45'
    city = "Chicago" # get_geolocation()

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

#Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sent', methods=['POST'])
def sent():
    email       = request.form.get('email')
    contact_msg = request.form.get('message')
    if not email or not contact_msg:
        return render_template('contact.html')
    message = 'Subject: New Request | imarcano.com \n' + email + '\n' + contact_msg
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('irgranados16@gmail.com', 'password')
    server.sendmail('irgranados16@gmail.com', 'irgranados16@gmail.com', message)
    return render_template('sent.html', email=email)



# Geo-Location
def get_geolocation():
    url = 'http://ip-api.com/json/{}'.format(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    response = requests.get(url).json()
    city = response['city']
    return city
