import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(f'{here}/README.md', 'r') as f:
    descriptions = f.read()

with open(f'{here}/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='cafe-application',
    version='1.0.0',
    description='A cafe application',
    keywords='cafe, python, mysql, 3-layer',
    url='https://github.com/quangduy201/cafe-application',
    long_description=descriptions,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
