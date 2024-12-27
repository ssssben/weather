from setuptools import setup
import os
from glob import glob

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bun',
    maintainer_email='vlongbf@gmail.com',
    description='課題2用',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weather_note = weather_pkg.weather_note:main', 
        ],
    },
)

