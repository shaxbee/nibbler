from setuptools import setup, find_packages

setup(
    name='nibbler',
    version='1.0',
    description='ZMQ-Protobuf Websocket Bridge',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={'nibbler': ['static/*']},
    scripts=['scripts/nibbler'],
    setup_requires=['nose>=1.0'],
    install_requires=['pyzmq', 'protobuf', 'cherrypy', 'ws4py', 'docopt', 'bidict']
)
