from setuptools import setup
setup(
    name='octopus',
    version='0.0.1',
    py_modules=['myprogram'],
    entry_points={
        'console_scripts': [
            'myprogram=myprogram:main'
        ]
    }
)
