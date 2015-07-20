# coding=utf-8
import glob

from setuptools import setup, find_packages

setup(
    name='citools',
    version='0.2.9',
    packages=find_packages(),
    scripts=glob.glob('scripts/*'),
    description='CI Tools',
    author='Andreas Würl',
    author_email='andreas@wuerl.net',
    license='Apache-2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=['requests', 'junit-xml'],
    tests_require=['nose', 'mock', 'coverage', 'assertpy'],
)
