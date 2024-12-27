import unittest
from unittest.mock import patch
from weather_pkg.weather_node import WeatherNode

class TestWeatherNode(unittest.TestCase):

    @patch('weather_pkg.weather_node.requests.get')
    def test_get_weather(self, mock_get):
        mock_response = {
            'main': {'temp': 25.0},
            'weather': [{'description': 'clear sky'}]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        node = WeatherNode()
        city = "Tokyo"
        result = node.get_weather(city)
        expected = "Weather in Tokyo: 25.0°C, Clear sky"
        self.assertEqual(result, expected)

    def test_missing_api_key(self):
        with patch.dict('os.environ', {'OPENWEATHERMAP_API_KEY': ''}):
            with self.assertRaises(SystemExit):
                WeatherNode()

if __name__ == '__main__':
    unittest.main()

