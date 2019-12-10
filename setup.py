from setuptools import find_packages
from setuptools import setup

setup(
    name="TomParis",
    version="0.1",
    description="Configurator and wrapper for kubectl",
    packages=find_packages(),
    install_requires=["pyyaml"],
    tests_require=[],
    long_description=__doc__,
    author='Dominik "Socek" Długajczyk',
    author_email="msocek@gmail.com",
    license="Apache 2.0",
    zip_safe=False,
    url="http://github.com/socek/tomparis",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Framework :: AsyncIO",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
