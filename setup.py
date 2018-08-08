import os
from setuptools import setup, find_packages

def getversion():
    """Reads version from VERSION file"""
    with open(os.path.join(os.path.dirname(__file__), 'kimanalysis', 'VERSION')) as f:
        return f.read().strip()

def getreadme():
    with open('README.rst') as readme_file:
        return readme_file.read()
   
setup(name = 'kimanalysis',
      version = getversion(),
      description = "Python-based access of the openKIM project's databases"
      long_description = getreadme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Physics'
      ],
      keywords = [
        'atom', 
        'atomic', 
        'atomistic', 
        'molecular dynamics', 
        'openKIM', 
        'interatomic'
      ], 
      #url = 'https://github.com/lmhale99/kimanalysis',
      author = 'Lucas Hale',
      author_email = 'lucas.hale@nist.gov',
      packages = find_packages(),
      install_requires = [
        'numericalunits',
        'numpy', 
        'pandas',
        'requests',
        'bibtexparser',
        'edn_format',
        'lxml',
      ],
      package_data={'': ['*']},
      zip_safe = False)