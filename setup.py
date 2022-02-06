from setuptools import setup, find_packages
from pathlib import Path


TESTS_DIRECTORY = 'test'

def get_requirements():
    return []
    with Path("./requirements.txt").open('r') as fd:
        return fd.readlines()


setup(
    name='lenticular_cloud',
    version='0.0.1',
    description='A useful module',
    author='tuxcoder',
    author_email='git@o-g.at',
    packages=find_packages(exclude=(TESTS_DIRECTORY,)),
    include_package_data=True,
    install_requires=get_requirements(), # external packages as dependencies
    entry_points = {
        'console_scripts': ['lenticular_cloud-cli=lenticular_cloud.cli:entry_point']
    }
)

