from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"

@app.route('/', methods = ['POST', 'GET'])
def index():
    city = "---"
    temp = 0
    icon = ""
    humidity = "--"
    desc = "---"
    minMax = [0, 0]

    if request.method == 'POST':
        city = request.form['name']

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}' 
        # print('*'*100)
        # print(url.format(city, API_KEY))
        # print('*'*100)

        response = requests.get(url.format(city, API_KEY)).json()

        # print('*'*100)
        # print(response)
        # print('*'*100)

        city = city.title()

        if response['cod'] == 200:
            temp = int(response['main']['temp'] - 273.15)
            desc = response['weather'][0]['description']
            desc = desc.title()
            minMax[0] = int(response['main']['temp_min'] - 273.15)
            minMax[1] = int(response['main']['temp_max'] - 273.15)
            humidity = response['main']['humidity']
            icon = response['weather'][0]['icon']
        else:
            city = "---"

    return render_template("index.html", city_name=city, desc=desc, temp=temp, min_temp=minMax[0], max_temp=minMax[1], humidity=humidity, icon=icon)

if __name__ == "__main__":
    app.run(debug=True)
