# TODO: Find a way to correctly implement this thing at some point
from setuptools import setup
setup(
    name='airoctopus',
    version='0.0.1',
    py_modules=['myprogram'],
    entry_points={
        'console_scripts': [
            'myprogram=myprogram:main'
        ]
    }
)
