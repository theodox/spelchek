from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()


setup(name='spelchek',
      version='0.54',
      description='A pure-python Bayesian spellchecker',
      long_description=long_description,
      url='https://github.com/theodox/spelchek',
      author='Steve Theodore',
      author_email='steve@theodox.com',
      license='MIT',
      packages=['spelchek'],
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Text Processing',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: Implementation'
      ],
      install_requires=[])
