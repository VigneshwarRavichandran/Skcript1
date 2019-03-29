
from setuptools import setup


setup(name='logic',
      version='1.0',
	  entry_points={
        'console_scripts': [
            'magic = cli:magic',
            'longest = cli:longest'
        ],
    })
