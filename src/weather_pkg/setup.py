from setuptools import setup

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bun',
    maintainer_email='vlongbf@gmail.com',
    description='A ROS 2 package for publishing weather information.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weather_node = weather_pkg.weather_node:main',  # エントリーポイントの指定
        ],
    },
)

