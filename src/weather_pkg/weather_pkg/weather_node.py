import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import os

class WeatherNode(Node):
    def __init__(self):
        super().__init__('weather_node')
        self.publisher_ = self.create_publisher(String, 'weather_info', 10)
        self.timer = self.create_timer(10, self.publish_weather)

    def get_weather(self, city):
        # 環境変数からAPIキーを取得
        api_key = os.getenv('OPENWEATHERMAP_API_KEY', None)
        if not api_key:
            self.get_logger().error("API key is missing!")
            return f"API key is missing for {city}!"

        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                return f"Weather in {city}:\nTemperature: {temperature:.1f}°C\nCondition: {description.capitalize()}"
            else:
                self.get_logger().error(f"Failed to get weather data for {city}: {data.get('message', 'Unknown error')}")
                return f"Failed to get weather data for {city}: {data.get('message', 'Unknown error')}"
        except requests.exceptions.RequestException as e:
            self.get_logger().error(f"Error fetching weather data for {city}: {e}")
            return f"Failed to get weather data for {city}: {e}"

    def publish_weather(self):
        # 東京と大連の天気情報を取得
        weather_tokyo = self.get_weather('Tokyo')
        weather_dalian = self.get_weather('Dalian')

        msg = String()
        msg.data = f"{weather_tokyo}\n\n{weather_dalian}"
        self.publisher_.publish(msg)
        
        # 天気情報を1回だけ表示
        self.get_logger().info(f'Publishing weather info: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    weather_node = WeatherNode()
    rclpy.spin(weather_node)
    weather_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

