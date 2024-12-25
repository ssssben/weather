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

    def get_weather(self):
        # APIキーを環境変数から取得
        api_key = os.getenv('OPENWEATHERMAP_API_KEY', None)
        if not api_key:
            self.get_logger().error("API key is missing!")
            return "API key is missing!"

        city = 'Tokyo'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()

            # APIレスポンスの内容をデバッグ出力
            self.get_logger().info(f"API Response: {data}")

            if response.status_code == 200:
                if 'main' in data and 'temp' in data['main']:
                    temperature = data['main']['temp']
                    description = data['weather'][0]['description']
                    # 見やすくフォーマットされた天気情報を返す
                    return (f"Weather in {city}:\n"
                            f"Temperature: {temperature:.1f}°C\n"
                            f"Condition: {description.capitalize()}")
                else:
                    self.get_logger().error("Response data format is incorrect or missing 'main' key.")
                    return "Invalid weather data format"
            else:
                self.get_logger().error(f"Failed to get weather data: {data.get('message', 'Unknown error')}")
                return f"Failed to get weather data: {data.get('message', 'Unknown error')}"
        except requests.exceptions.RequestException as e:
            self.get_logger().error(f"Error fetching weather data: {e}")
            return f"Failed to get weather data: {e}"

    def publish_weather(self):
        weather_info = self.get_weather()
        msg = String()
        msg.data = weather_info
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing weather info:\n{weather_info}')

def main(args=None):
    rclpy.init(args=args)
    weather_node = WeatherNode()
    rclpy.spin(weather_node)
    weather_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

