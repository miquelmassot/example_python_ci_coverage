"""
Copyright (c) 2019, University of Southampton
All rights reserved.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_module",
    version="0.0.1",
    author="Miquel Massot",
    author_email="miquel.massot-campos@soton.ac.uk",
    description="Toy project as an example of CI, testing and coverage",
    long_description=long_description,
    url="https://github.com/miquelmassot/example_python_ci_coverage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # Optional
        "console_scripts": ["my_module = my_module.my_module:main"],
    },
    install_requires=["tqdm>=4.32.2"],
)
