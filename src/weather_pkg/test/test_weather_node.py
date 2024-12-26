import pytest
import rclpy
from weather_pkg.weather_node import WeatherNode
from std_msgs.msg import String

@pytest.fixture
def weather_node():
    rclpy.init()
    node = WeatherNode()
    yield node
    node.destroy_node()
    rclpy.shutdown()

def test_publish_weather(weather_node):
    assert isinstance(weather_node.publisher_, rclpy.publisher.Publisher)

