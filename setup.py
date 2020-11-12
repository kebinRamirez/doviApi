from setuptools import setup

setup(
   name='dovi',
   version='1.0',
   description='probando setup',
   author='Kebin ramirez',
   author_email='kebinr@uninorte.edu.co',
   packages=['configurations'],  #same as name
   install_requires=['numpy', 'pandas'], #external packages as dependencies
)