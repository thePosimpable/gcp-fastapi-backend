from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if __name__ == '__main__':
    setup(install_requires = requirements, py_modules=[])