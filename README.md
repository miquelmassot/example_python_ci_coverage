# Example python project

This is an exciting python project with two nice features

- Continuous integration using GitHub workflows. Badge to prove it: [![CI & Coverage](https://github.com/miquelmassot/python_package_with_ci_and_coverage/actions/workflows/python.yaml/badge.svg?branch=main)](https://github.com/miquelmassot/python_package_with_ci_and_coverage/actions/workflows/python.yaml)
- Code testing and coverage using codecov.io. Badge to prove it: [![codecov](https://codecov.io/gh/miquelmassot/python_package_with_ci_and_coverage/graph/badge.svg?token=BzwqnEQKP4)](https://codecov.io/gh/miquelmassot/python_package_with_ci_and_coverage)

With them, you can get to know the status of your code, and add these cool badges to it.
Feel free to reuse any part of this package for your own projects

## Installation

To install this package, run the following command in the root directory of the project

```bash
pip install -U --user -e .
```

The flags are:

- `-U` to upgrade the package if it is already installed
- `--user` to install the package in the user directory
- `-e` to install the package in editable mode, so that changes in the code are immediately available

## Entry point

The file setup.py contains the entry point of the package. This means that when you install the package with `pip`, it will create a command line entry point with the name `my_module`. This will call the function `main` of the file `my_module.py`. You can change the name of the entry point in the file `setup.py`.
