from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='nepserate',
	version='0.1.0',
	description='Get the rate of Organization',
	packages=['nepserate'],
	url='https://github.com/acsudeep/nepserate',
	author='Sudeep Acharya',
	author_email='sudeep611@gmail.com',
	license='MIT',
	keywords='nepal, nepse, nepalstock, nepalsharemarket',
	install_requires=['urllib3'],
	zip_safe=False,
    platforms='any',
	)
