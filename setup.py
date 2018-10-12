# Copyright 2018 NAVER Corp.
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

from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import sys

__version__ = "0.0.1-alpha"

with open("requirements.txt") as f:
    require_packages = [line[:-1] for line in f]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != __version__:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, __version__
            )
            sys.exit(info)


setup(
    name="kor2vec",
    version=__version__,
    author='Junseong Kim',
    author_email='codertimo@gmail.com',
    packages=find_packages(),
    install_requires=require_packages,
    url="https://github.com/codertimo/kor2vec",
    description="Char-CNN based Korean Word Embedding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'kor2vec = kor2vec.__main__:kor2vec_main',
            'kor2vec-context = kor2vec.__main__:kor2vec_context_main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
