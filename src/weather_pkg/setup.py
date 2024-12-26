from setuptools import setup

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.1',
        'requests',  # requestsパッケージが必要なので追加
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    entry_points={
        'console_scripts': [
            f'weather_node = {package_name}.weather_node:main',
        ],
    },
)

