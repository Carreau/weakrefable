from setuptools import setup, Extension, find_packages

module1 = Extension('_weakrefable',
                    sources = ['_canweakref.c'])

with open('readme.rst') as f:
    description = f.read()

packages = find_packages()
print(packages)

setup(name = 'weakrefable',
       version = '0.0.1',
       long_description = description,
       author = 'Matthias Bussonnier', 
       author_email = 'bussonniermatthias@gmail.com',
       license = 'MIT',
       keywords = 'weakref CPython', 
       url = 'https://github.com/Carreau/weakrefable',
       python_requires ='>=3.4',
       ext_modules = [module1],
       packages=packages
    )
