#! /usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="canonicalwebteam.discourse_docs",
    version="0.1.1",
    author="Canonical webteam",
    author_email="webteam@canonical.com",
    url="https://github.com/canonical-webteam/canonicalwebteam.docs",
    description=(
        "Flask extension to integrate discourse content generated "
        "to docs to your website."
    ),
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "Flask>=1.0.2",
        "canonicalwebteam.http",
        "beautifulsoup4",
        "humanize",
        "python-dateutil",
    ],
    tests_require=["responses", "requests-mock"],
)
