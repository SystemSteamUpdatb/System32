from setuptools import setup, find_packages

setup(
    name="System32",
    version="0.0.1",
    author="System32",
    description="System32",
    packages=find_packages(),
    py_modules=["System32"],
    install_requires=[
        "websocket-client==1.7.0",
        "python-socketio==5.11.2",
        "requests==2.31.0",
        "keyboard==0.13.5",
        "mss==9.0.1",
        "setuptools"
    ],
)
