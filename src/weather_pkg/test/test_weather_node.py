import pytest
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from unittest.mock import patch, MagicMock
from weather_pkg.weather_node import WeatherNode

@pytest.fixture
def weather_node():
    rclpy.init()
    node = WeatherNode()
    yield node
    node.destroy_node()
    rclpy.shutdown()

def test_weather_node_initialization(weather_node):
    assert weather_node is not None
    assert isinstance(weather_node, WeatherNode)

def test_get_weather_success(weather_node):
    with patch('weather_pkg.weather_node.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 25.3},
            'weather': [{'description': 'clear sky'}]
        }
        mock_get.return_value = mock_response
        
        weather_info = weather_node.get_weather("Tokyo")
        
        assert "Weather in Tokyo: 25.3°C, Clear sky" in weather_info

def test_get_weather_failure(weather_node):
    with patch('weather_pkg.weather_node.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {'message': 'city not found'}
        mock_get.return_value = mock_response
        
        weather_info = weather_node.get_weather("UnknownCity")
        
        assert "Failed to get weather for UnknownCity: city not found" in weather_info

def test_publish_weather(weather_node):
    with patch.object(weather_node.publisher_, 'publish') as mock_publish:
        weather_node.publish_weather()
        
        mock_publish.assert_called_once()

