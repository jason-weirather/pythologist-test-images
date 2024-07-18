from setuptools import setup, find_packages
from os import path

this_folder = path.abspath(path.dirname(__file__))
with open(path.join(this_folder, 'README.md'), encoding='utf-8') as inf:
    long_description = inf.read()

setup(
    name='pythologist-test-images',
    version='1.0.2',
    description='Real and simulated data for testing image analysis software',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the type of README
    url='https://github.com/jason-weirather/pythologist-test-images',
    author='Jason L Weirather',
    author_email='jason.weirather@gmail.com',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    keywords='bioinformatics',
    packages=find_packages(),  # Automatically find packages
    extras_require={
        'h5': ['pythologist']
    },
    install_requires=[],
    python_requires='>=3.6',  # Specify the Python versions supported
)

