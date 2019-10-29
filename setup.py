from setuptools import setup

setup(
    name='server',
    version=0.1,
    description='Utility for python file servers',
    url="https://github.com/ponyfat/httpsServer",
    entry_points = {
        'console_scripts': ['server=server.httpServer:main'],
    },
    license='MIT'
)