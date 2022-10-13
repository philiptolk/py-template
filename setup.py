#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = [
    "boto3"
]

test_requirements = [
    "bandit",
    "black",
    "flake8",
    "flake8-bugbear",
    "flake8-comprehensions",
    "bump2version",
]


setup(
    author="Philip Tolk",
    author_email="philip@braincargo.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Generic template for terraform localstack devcontainers",
    entry_points={
        "console_scripts": [
            "src=main.test_me:main",
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords="template,python,devops",
    name="py-devops-template",
    packages=find_packages(include=["src", "src.*"]),
    test_suite="tests",
    tests_requires=test_requirements,
    url="https://github.com/philiptolk/py-devops-template",
    version="9010.0.0",
    zip_safe=False,
)
