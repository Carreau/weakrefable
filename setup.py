from setuptools import setup, Extension

module1 = Extension('_weakrefable',
                    sources = ['_canweakref.c'])

with open('readme.rst') as f:
    description = f.read()

setup(name = 'weakrefable',
       version = '0.0.1',
       long_description = description,
       author = 'Matthias Bussonnier', 
       author_email = 'bussonniermatthias@gmail.com',
       liscense = 'MIT',
       keywords = 'weakref CPython', 
       url = 'https://github.com/Carreau/weakrefable',
       python_requires ='>=3.4',
       ext_modules = [module1],
       py_modules=['weakrefable']
    )
