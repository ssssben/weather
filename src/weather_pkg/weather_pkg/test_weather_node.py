import pytest
from unittest.mock import patch
from weather_pkg.weather_node import WeatherNode
import rclpy
from std_msgs.msg import String

@pytest.fixture
def weather_node():
    rclpy.init()
    node = WeatherNode()
    yield node
    node.destroy_node()
    rclpy.shutdown()

def test_get_weather_success(weather_node):
    with patch('weather_pkg.weather_node.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 25},
            'weather': [{'description': 'clear sky'}]
        }
        
        result = weather_node.get_weather("Tokyo")
        expected = "Weather in Tokyo: 25.0°C, Clear sky"
        assert result == expected

def test_get_weather_failure(weather_node):
    with patch('weather_pkg.weather_node.requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {'message': 'city not found'}
        
        result = weather_node.get_weather("InvalidCity")
        expected = "Failed to get weather for InvalidCity: city not found"
        assert result == expected

def test_publish_weather(weather_node):
    with patch('weather_pkg.weather_node.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {'temp': 25},
            'weather': [{'description': 'clear sky'}]
        }

        with patch.object(weather_node.publisher_, 'publish') as mock_publish:
            weather_node.publish_weather()
            mock_publish.assert_called_once()


