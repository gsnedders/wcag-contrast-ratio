from distutils.core import setup

import codecs
import os.path

_classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development'
    ]

_current_dir = os.path.dirname(__file__)
with codecs.open(os.path.join(_current_dir, 'README.rst'), 'r', 'utf8') as readme_file:
    _long_description = readme_file.read()

setup(
    name="wcag-contrast-ratio",
    version="0.9",
    url="https://github.com/gsnedders/wcag-contrast-ratio",
    license="MIT License",
    description="A library for computing contrast ratios, as required by WCAG 2.0",
    long_description=_long_description,
    classifiers=_classifiers,
    maintainer="Geoffrey Sneddon",
    maintainer_email="geoffers@gmail.com",
    packages = ["wcag_contrast_ratio"]
)
