from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
BASE_URL = "http://api.openweathermap.org/data/2.5/"

@app.route('/')
@app.route('/home')
def homePage():
    return render_template("home.html")

@app.route('/weather')
def weather():
    return render_template("weather.html")

@app.route('/get_weather', methods=['POST'])
def get_weather():
    try:
        city = request.json.get('city')
        if not city:
            return jsonify({'error': 'City name is required'}), 400
        
        if API_KEY == 'your_api_key_here' or not API_KEY:
            return get_demo_weather_data(city)
        
        current_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
        current_response = requests.get(current_url)
        
        if current_response.status_code == 200:
            current_data = current_response.json()
            
            forecast_url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json() if forecast_response.status_code == 200 else None
            
            weather_info = {
                'current': {
                    'city': current_data['name'],
                    'country': current_data['sys']['country'],
                    'temperature': round(current_data['main']['temp']),
                    'feels_like': round(current_data['main']['feels_like']),
                    'description': current_data['weather'][0]['description'].title(),
                    'icon': current_data['weather'][0]['icon'],
                    'humidity': current_data['main']['humidity'],
                    'pressure': current_data['main']['pressure'],
                    'wind_speed': current_data['wind']['speed'],
                    'visibility': current_data.get('visibility', 0) / 1000,  # Convert to km
                    'sunrise': datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M'),
                    'sunset': datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M')
                },
                'forecast': []
            }
            
            if forecast_data:
                daily_forecasts = {}
                for item in forecast_data['list']:
                    date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
                    if date not in daily_forecasts:
                        daily_forecasts[date] = {
                            'date': datetime.fromtimestamp(item['dt']).strftime('%a, %b %d'),
                            'temp_min': item['main']['temp'],
                            'temp_max': item['main']['temp'],
                            'description': item['weather'][0]['description'].title(),
                            'icon': item['weather'][0]['icon'],
                            'humidity': item['main']['humidity']
                        }
                    else:
                        daily_forecasts[date]['temp_min'] = min(daily_forecasts[date]['temp_min'], item['main']['temp'])
                        daily_forecasts[date]['temp_max'] = max(daily_forecasts[date]['temp_max'], item['main']['temp'])
                
                for date_key in sorted(daily_forecasts.keys())[:5]:
                    forecast = daily_forecasts[date_key]
                    forecast['temp_min'] = round(forecast['temp_min'])
                    forecast['temp_max'] = round(forecast['temp_max'])
                    weather_info['forecast'].append(forecast)
            
            return jsonify(weather_info)
        else:
            error_msg = current_response.json().get('message', 'City not found')
            return jsonify({'error': error_msg}), 404
            
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching weather data'}), 500

def get_demo_weather_data(city):
    """Return demo weather data when API key is not configured"""
    from datetime import datetime, timedelta
    
    demo_data = {
        'current': {
            'city': city.title(),
            'country': 'Demo',
            'temperature': 22,
            'feels_like': 25,
            'description': 'Partly Cloudy',
            'icon': '02d',
            'humidity': 65,
            'pressure': 1013,
            'wind_speed': 3.5,
            'visibility': 10.0,
            'sunrise': '06:30',
            'sunset': '19:45'
        },
        'forecast': []
    }
    
    base_date = datetime.now()
    for i in range(5):
        forecast_date = base_date + timedelta(days=i+1)
        demo_data['forecast'].append({
            'date': forecast_date.strftime('%a, %b %d'),
            'temp_min': 18 + i,
            'temp_max': 25 + i,
            'description': ['Sunny', 'Partly Cloudy', 'Cloudy', 'Light Rain', 'Clear'][i],
            'icon': ['01d', '02d', '03d', '10d', '01d'][i],
            'humidity': 60 + i * 5
        })
    
    return jsonify(demo_data)

if __name__ == '__main__':   
    app.run(debug=True)

