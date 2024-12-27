import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bun/ros2_weather_ws/src/weather_pkg/install/weather_pkg'
