# Weather Forecast App

A modern, responsive weather forecast application built with Flask and the OpenWeatherMap API.

## Features

- **Current Weather**: Real-time weather conditions including temperature, humidity, wind speed, and atmospheric pressure
- **5-Day Forecast**: Detailed weather predictions for the next 5 days
- **Global Coverage**: Search for weather information in cities worldwide
- **Responsive Design**: Modern, mobile-friendly interface
- **Interactive UI**: Smooth animations and user-friendly experience

## Setup Instructions

### 1. Get OpenWeatherMap API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key
4. Copy your API key

### 2. Configure the Application

1. Open `app.py`
2. Replace `"your_api_key_here"` with your actual OpenWeatherMap API key:
   ```python
   API_KEY = "your_actual_api_key_here"
   ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. Navigate to the home page to learn about the features
2. Click "Check Weather Now" or go to `/weather`
3. Enter a city name in the search box
4. View current weather conditions and 5-day forecast

## API Endpoints

- `/` or `/home` - Home page
- `/weather` - Weather search page
- `/get_weather` - POST endpoint for fetching weather data

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Weather Data**: OpenWeatherMap API
- **Icons**: Font Awesome
- **Design**: Modern responsive design with glassmorphism effects

## Project Structure

```
Weather-App/
├── venv/
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── templates/          # HTML templates
│   │   ├── home.html      # Landing page
│   │   ├── weather.html   # Weather search page
│   │   └── user.html      # Additional template
│   └── static/            # Static files (CSS, JS, images)
```

## Features Overview

### Current Weather Display
- Temperature (current and "feels like")
- Weather description with icon
- Humidity percentage
- Wind speed
- Visibility distance
- Atmospheric pressure
- Sunrise and sunset times

### 5-Day Forecast
- Daily temperature ranges (min/max)
- Weather conditions with icons
- Humidity levels
- Easy-to-read date formatting

### User Interface
- Modern glassmorphism design
- Responsive layout for all devices
- Smooth animations and transitions
- Error handling with user-friendly messages
- Loading indicators
- Search suggestions

## Customization

You can customize the appearance by modifying the CSS styles in the HTML templates or by creating separate CSS files in the `static/css/` directory.

## Troubleshooting

1. **API Key Issues**: Make sure your OpenWeatherMap API key is valid and properly configured
2. **City Not Found**: Ensure the city name is spelled correctly
3. **Network Errors**: Check your internet connection
4. **Port Issues**: If port 5000 is in use, modify the port in `app.py`

## License

This project is open source and available under the MIT License.
