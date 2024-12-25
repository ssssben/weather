from setuptools import setup

package_name = 'weather_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools', 'requests'],  # 依存関係のパッケージをここに記述
    zip_safe=True,
    author='Your Name',  # ここは適切な名前に変更
    author_email='your_email@example.com',  # あなたのメールアドレス
    maintainer='Your Name',  # あなたの名前
    maintainer_email='your_email@example.com',  # あなたのメールアドレス
    description='ROS2 package to fetch weather data from OpenWeatherMap API.',
    license='License',  # 必要に応じてライセンスを設定
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'weather_node = weather_pkg.weather_node:main',
        ],
    },
)

