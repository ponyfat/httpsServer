from setuptools import setup

setup(
    name='server',
    version='0.7',
    description='Utility for python file servers',
    url="https://github.com/ponyfat/httpsServer",
    entry_points = {
        'console_scripts': ['server=server:server'],
    },
    license='MIT'
)