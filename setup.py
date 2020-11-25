import json
import os
from shutil import copyfile
from sys import platform

from setuptools import find_packages
from setuptools import setup


def is_pi() -> bool:
    result = os.uname()
    if len(result) >= 5:
        return result[4].startswith('arm')
    return False


__version__ = ''  # To avoid resolved reference '__version__'.
with open('version.py') as f:
    exec(f.read())

all_requirements = [
    'Appium-Python-Client>=1.0.2',
    'websockets',
    'requests>=2.22.0',
    'selenium>=3.9.0',
    'GitPython>=2.1',
    'pyserial>=3.4',
    'jsonschema>=2.6.0',
    'pandas>=0.22.0',
    'aloe>=0.1.16',
    'behave>=1.2.6',
    'xlrd>=1.1.0',
    'python-ntlm3>=1.0.2',
    'cffi>=1.11.5',
    'beautifulsoup4>=4.6.0',
    'python-miio==0.4.8',
    'pexpect>=4.6.0',
    'pytest>=4.3.0',
    'pytest-cov>=2.6.1',
    'openpyxl==2.5.1',  # to be in line with RoboticsBehaviourAuto requirement
    'keyboard>=0.13.3',
    'paho-mqtt>=1.4.0',
    'AWSIoTPythonSDK>=1.4.4',
    'junitparser>=1.3.2',
    'pyHS100>=0.3.5',
    'pyperclip>=1.7.0',
    'psutil>=5.6.1',
    'xmltodict>=0.12.0',
    'scp>=0.13.2',
    'paramiko>=2.6.0',
    'xlsxwriter>=1.2.2',
    'jira>=2.0.0',
    'urllib3>=1.25.3',
    'smbus2',
    'dash>=1.6.0',
    'transitions>=0.7.1',
    'rpyc==4.1.4',
    'Pillow>=5.0.0',
    'scikit-image>=0.15.0',
    'jinja2>=2.11.1',
    'pyzmq>=18.1.0',
    'dwf>=0.1.0'
]

windows_requirements = [
    'pypiwin32>=220',
    'pywin32>=224',
    'PyQt5==5.13.0',
    'PyQt5-tools==5.15.1.3',
    'win32wifi>=0.1.0'
]

pi_requirements = [

]

linux_requirements = [
    'PyQt5==5.10',  # Ubuntu 14.04 needs 5.10 for compatibility with libdbus (robot test).
]

darwin_requirements = [
    'PyQt5==5.13.0'
]

if platform.startswith('win'):
    all_requirements.extend(windows_requirements)
elif platform.startswith('linux'):
    if is_pi():
        all_requirements.extend(pi_requirements)
    else:
        all_requirements.extend(linux_requirements)
elif platform == 'darwin':  # MacOS
    all_requirements.extend(darwin_requirements)

setup(
    name='tusi-example',
    version=__version__,
    packages=find_packages(),
    install_requires=all_requirements,
    license='GNU GENERAL PUBLIC LICENSE',
    author='Bradly Malitam',
    author_email='bradlymalitam@tusicloud.com',
    description='Workshop modules',
    entry_points={

    }
)


