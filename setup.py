from setuptools import setup

print('start')
setup(
    name='server',
    version=0.1,
    description='Utilite for python file servers',
    entry_points = {
        'console_scripts': ['server=server.httpServer:main'],
    },
    license='MIT'
)