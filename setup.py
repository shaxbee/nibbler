from setuptools import setup, find_packages

setup(
    name='nibbler',
    version='1.0',
    description='ZMQ-Protobuf Websocket Bridge',
    packages=find_packages(),
    scripts=['scripts/nibbler'],
    setup_requires=['nose>=1.0'],
    install_requires=['pyzmq', 'protobuf', 'cherrypy', 'ws4py', 'docopt']
)
