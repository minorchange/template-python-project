from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.0.1",
    url="https://github.com/mypackage.git",
    author="minorchange",
    description="Description of the package",
    packages=find_packages(),
    install_requires=["numpy >= 1.23.1", "matplotlib >= 3.5.2"],
)
