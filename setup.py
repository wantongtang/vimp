from setuptools import setup

setup(
    name="vimp",
    version="0.0.1",
    author="Christian Stigen Larsen",
    author_email="csl@csl.name",
    keywords="vim",
    packages=["vimp", "vimp.test"],
    scripts=["bin/vimp"],
    url="https://github.com/cslarsen/vimp",
    license="LICENSE.txt",
    description="Command-line package manager or vim.",
    long_description=open("README.md").read(),
    zip_safe=True,
)
