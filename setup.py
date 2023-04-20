import os
import subprocess
import sys
import venv

import pkg_resources
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

try:
    venv.create('venv', with_pip=True)
except Exception:
    pass

with open(f'{here}/README.md', encoding="utf-8") as f:
    descriptions = f.read()

with open(f'{here}/requirements.txt') as f:
    requirements = f.read().splitlines()

# installed = {pkg.key for pkg in pkg_resources.working_set}
# missing = {*requirements} - installed

# if missing:
#     subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

setup(
    name='cafe-application',
    version='1.0.0',
    description='A cafe application',
    keywords='cafe, python, opencv, mysql, 3-layer',
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
