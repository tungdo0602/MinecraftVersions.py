# -*- coding: utf-8 -*-
from setuptools import setup

config = {}

with open("minecraftVersions/__init__.py", "r") as f:
    for i in f.readlines():
        if "__version__" in i:
            config.update({"version": i.split("=")[1].replace("\n", "").replace('"', "").strip()})
        if "__author__" in i:
            config.update({"author": i.split("=")[1].replace("\n", "").replace('"', "").strip()})
        if "__title__" in i:
            config.update({"name": i.split("=")[1].replace("\n", "").replace('"', "").strip()})
        if "__license__" in i:
            config.update({"license": i.split("=")[1].replace("\n", "").replace('"', "").strip()})

with open("README.md", "r") as f:
    config.update({"readme": f.read()})

setup(
    name=config["name"],
    version=config["version"],    
    description="A simple minecraft version wrapper written in python",
    url="https://github.com/tungdo0602/MinecraftVersions.py",
    project_urls={
        'Issue tracker': 'https://github.com/tungdo0602/MinecraftVersions.py/issues',
    },
    long_description=config["readme"],
    long_description_content_type="text/markdown",
    author=config["author"],
    license=config["license"],
    packages=["minecraftVersions"],
    install_requires=["requests"],
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
)