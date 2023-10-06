from setuptools import setup, find_packages

setup(
    name='dns_validate',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiodns',
        'aiohttp',
    ],
    entry_points={
        'console_scripts': [
            'dns_validate=dns_validate.main:main',
        ],
    },
)
