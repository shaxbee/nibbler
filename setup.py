from distutils.core import setup

setup(
	name='zmqprotows',
	version='1.0',
	description='ZMQ-Protobuf Websocket Bridge',
	packages=['zmqprotows', 'zmqprotows.cherrypy'],
	requires=['pyzmq', 'protobuf', 'ws4py']
)

