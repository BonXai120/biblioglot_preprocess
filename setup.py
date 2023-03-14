from setuptools import setup

setup(
    name='biblioglot-preprocessor',
    version='1.0.0',
    packages=['myproject'],
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'mycommand = myproject.mymodule:main'
        ]
    }
)