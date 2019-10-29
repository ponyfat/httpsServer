from setuptools import setup

setup(
    name='server',
    version='0.0.3',
    description='Utility for python file servers',
    url="https://github.com/ponyfat/httpsServer",
    entry_points = {
        'console_scripts': ['server=httpsServer:main'],
    },
    license='MIT'
)