from setuptools import setup

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=['weather_pkg'],
    data_files=[
        ('share/ament_index/resource_index/ament_libraries', ['resource/weather_pkg']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'requests'],
    zip_safe=True,
    maintainer='Bun',
    maintainer_email='vlongbf@gmail.com',
    description='A package for weather information',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weather_node = weather_pkg.weather_node:main',
        ],
    },
)

