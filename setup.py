from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="unbirthday",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        #no packages needed
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)