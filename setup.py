import os
from setuptools import setup, find_packages


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding='utf-8')
    except TypeError:
        file = open(path)
    return file.read()


def get_install_requires():
    install_requires = ['Django']

    try:
        import importlib  # NOQA
    except ImportError:
        install_requires.append('importlib')

    try:
        from collections import OrderedDict  # NOQA
    except ImportError:
        install_requires.append('ordereddict')

    return install_requires


setup(
    name='rs-django-jet',
    version=__import__('jet').VERSION,
    description='Fork of django-jet with customizations',
    long_description=read('README.rst'),
    author='Govind Sharma',
    author_email='me.govindsharma@gmail.com',
    maintainer='Govind Sharma',
    maintainer_email='me.govindsharma@gmail.com',
    url='https://github.com/govindsharma7/gds-django-jet',
    packages=find_packages(),
    license='AGPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Environment :: Web Environment',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=get_install_requires()
)
