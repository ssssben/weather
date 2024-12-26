import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import os
from unittest.mock import patch

class WeatherNode(Node):
    def __init__(self):
        super().__init__('weather_node')
        self.publisher_ = self.create_publisher(String, 'weather_info', 10)
        self.timer = self.create_timer(10, self.publish_weather)

        # APIキーを環境変数から取得
        self.api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        if not self.api_key:
            self.get_logger().error("API key is missing! Please set the OPENWEATHERMAP_API_KEY environment variable.")
            rclpy.shutdown()

    def get_weather(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                return f"Weather in {city}: {temperature:.1f}°C, {description.capitalize()}"
            else:
                return f"Failed to get weather for {city}: {response.json().get('message', 'Unknown error')}"
        except requests.exceptions.RequestException as e:
            return f"Error fetching weather for {city}: {e}"

    def publish_weather(self):
        weather_info = "\n\n".join([self.get_weather(city) for city in ['Tokyo', 'Dalian']])
        msg = String()
        msg.data = weather_info

        self.publisher_.publish(msg)

        self.get_logger().info(f'\nPublishing weather info:\n{msg.data}')


def main(args=None):
    rclpy.init(args=args)
    weather_node = WeatherNode()
    rclpy.spin(weather_node)
    weather_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


