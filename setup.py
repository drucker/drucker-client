# Copyright 2018 The Drucker Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

VERSION = "0.4.0"
PACKAGE_NAME = "drucker_client"
DEVELOPMENT_STATUS = "3 - Alpha"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

EXTRAS = {}
REQUIRES = []
with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        if ';' in line:
            requirement, _, specifier = line.partition(';')
            for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
            for_specifier.append(requirement)
        else:
            REQUIRES.append(line)

with open('test-requirements.txt') as f:
    TESTS_REQUIRES = f.readlines()

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="A Python gRPC client for Drucker.",
    author_email="",
    author="Drucker",
    license="Apache License Version 2.0",
    url="https://github.com/drucker/drucker-client",
    keywords=["Drucker", "Kubernetes"],
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRES,
    extras_require=EXTRAS,
    packages=['drucker_client', 'drucker_client.logger',
              'drucker_client.protobuf'],
    include_package_data=True,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: %s" % DEVELOPMENT_STATUS,
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        ],
)