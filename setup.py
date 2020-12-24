from os import path
from setuptools import setup

# Read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='census-data',
    version='0.1.0',
    description="Download U.S. census data and reformat it for humans",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Geoff Hing',
    author_email='geoffhing@gmail.com',
    url='http://www.github.com/ghing/census-data',
    license="MIT",
    packages=(
        "census_data",
    ),
    install_requires=(
        "pandas",
        "census",
        "click",
    ),
    entry_points="""
        [console_scripts]
        downloadpep=census_data.cli:download_pep_cmd
    """,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
)