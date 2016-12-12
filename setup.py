from setuptools import setup, Extension

module1 = Extension('weakreable',
                    sources = ['canweakref.c'])

with open('readme.rst') as f:
    description = f.read()

setup(name = 'weakrefable',
       version = '0.1',
       description = description,
       author = 'Matthias Bussonnier', 
       author_email = 'bussonniermatthias@gmail.com',
       liscense = 'MIT',
       keywords = 'weakref CPython', 
       url = 'https://github.com/Carreau/weakreable',
       python_requires ='>=3.4',
       ext_modules = [module1]
    )
