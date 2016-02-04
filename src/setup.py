from setuptools import setup

setup(
    name='alamo',
    version='0.1',
    install_requires=['Click'],
    entry_points={'console_scripts': ['alamo=alamo:cli']},
)


