from setuptools import setup, find_packages

setup(
    name="core_api",
    version="0.1",
    packages=find_packages(include=["core_api.app.*"])
)
