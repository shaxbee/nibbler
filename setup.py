from setuptools import setup, find_packages

setup(
	name='zmqprotows',
	version='1.0',
	description='ZMQ-Protobuf Websocket Bridge',
	packages=find_packages(),
	scripts=['scripts/zpws'],
	install_requires=['pyzmq', 'protobuf', 'cherrypy', 'ws4py', 'docopt']
)

