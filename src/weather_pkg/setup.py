from setuptools import setup

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=['weather_pkg'],
    install_requires=['setuptools', 'rclpy', 'requests'],
    zip_safe=True,
    maintainer='Bun',
    maintainer_email='vlongbf@gmail.com',
    description='A package for weather information',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weather_node = weather_pkg.weather_pkg.weather_node:main',
        ],
    },
)

