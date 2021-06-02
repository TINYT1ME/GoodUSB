from setuptools import setup


# used for pypi.org
setup(
    name='GoodUSB',
    version='1.0',
    description='Prevent BadUSB attacks',
    license="MIT",
    author='TINYT1ME',
    long_description=open('README.md', 'r', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/TINYT1ME/GoodUSB",
    packages=['GoodUSB'],
    install_requires=['pyWinhook-1.6.2-cp39-cp39-win_amd64.whl', 'pythoncom', 'keyboard']
)


