from setuptools import find_packages, setup

setup(
    name = 'GenAI Medical ChatBot',
    version = '0.0.0',
    author = 'Subin Krishna K T',
    author_email = 'example@gmail.com',
    packages = find_packages(),
    install_requires = []
)

# Setup this project as local package.
# Here the folder containing __init__.py is considered as local package and we can import functions from it.
# Why do we need local package, because sometimes your other projects may require your scripts in this project so we can avoid creating new files instead we can import modules from this.(Reusability)
# For this we have to do "pip install e ." or add "e ." inside requirements.txt
"""
You have two options to create local package
1) pip install .
2) pip install e .

In 1 you will install the local package and after installing you did some change in one of your code for example "helper.py" to capture this change in the module yoou will have to reinstall the module again by typeing "pip install ."
But in 2 we get a link to the "helper.py" we dont have to install every time when we make change to "helper.py", this is called editable mode.
"""