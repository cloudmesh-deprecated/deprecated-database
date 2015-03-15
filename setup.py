#!/usr/bin/env python

version = "1.0.2"

requirements =     [
    'cloudmesh_base',
    'sh',
    'simplejson',
    'pyaml',
    'pymongo',
    'mongoengine',
]
# from distutils.core import setup

from setuptools import setup, find_packages
from setuptools.command.install import install
import glob
import os
import shutil

try:
    from cloudmesh_base.util import banner
except:
    os.system("pip install cloudmesh_base")

from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cloudmesh_base.util import auto_create_version
from cloudmesh_base.util import auto_create_requirements


banner("Installing Cloudmesh Database Utils")

home = os.path.expanduser("~")

auto_create_version("cloudmesh_database", version)
auto_create_requirements(requirements)


class CreateRequirementsFile(install):
    """Create the requiremnets file."""

    def run(self):
        auto_create_requirements(requirements)


class UploadToPypi(install):
    """Upload the package to pypi."""

    def run(self):
        auto_create_version("cloudmesh_database", version)
        auto_create_requirements(requirements)
        os.system("make clean")
        os.system("python setup.py install")
        banner("Build Distribution")
        os.system("python setup.py sdist --format=bztar,zip upload")


class RegisterWithPypi(install):
    """Upload the package to pypi."""

    def run(self):
        banner("Register with Pypi")
        os.system("python setup.py register")


class InstallBase(install):
    """Install the package."""

    def run(self):
        auto_create_version("cloudmesh_database", version)
        auto_create_requirements(requirements)
        banner("Install Cloudmesh Base")
        install.run(self)


class InstallRequirements(install):
    """Install the requirements."""

    def run(self):
        banner("Install Cloudmesh Database Requirements")
        os.system("pip install -r requirements.txt")


class InstallAll(install):
    """Install requirements and the package."""

    def run(self):
        banner("Install Cloudmesh Databse Requirements")
        os.system("pip install -r requirements.txt")
        banner("Install Cloudmesh Base")
        install.run(self)


class CreateDoc(install):
    """Install requirements and the package."""

    def run(self):
        banner("Create Documentation")
        os.system("python setup.py install")
        os.system("sphinx-apidoc -o docs/source cloudmesh_database ")
        os.system("cd docs; make -f Makefile html")


class SetupYaml(install):
    """Upload the package to pypi."""

    def run(self):
        banner("Setup the cloudmesh_database.yaml file")

        database_yaml = path_expand("~/.cloudmesh/cloudmesh_database.yaml")

        if os.path.isfile(database_yaml):
            print ("WARNING: the file {0} already exists".format(database_yaml))
            print
            print ("If you like to reinstall it, please remove the file")
        else:
            print ("Copy file:  {0} -> {1} ".format(path_expand("etc/cloudmesh_database.yaml"), database_yaml))
            Shell.mkdir(path_expand("~/.cloudmesh"))

            shutil.copy("etc/cloudmesh_database.yaml", path_expand("~/.cloudmesh/cloudmesh_database.yaml"))


setup(
    name='cloudmesh_database',
    version=version,
    description='A set of simple database functions to manage a mongo db for programs',
    # description-file =
    #    README.rst
    author='The Cloudmesh Team',
    author_email='laszewski@gmail.com',
    url='http://github.org/cloudmesh/database',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Boot',
        'Topic :: System :: Systems Administration',
        'Framework :: Flask',
        'Environment :: OpenStack',
    ],
    packages=find_packages(),
    cmdclass={
        'install': InstallBase,
        'requirements': InstallRequirements,
        'all': InstallAll,
        'pypi': UploadToPypi,
        'pypiregister': RegisterWithPypi,
        'yaml': SetupYaml,
    },
)
