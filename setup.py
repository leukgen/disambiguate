"""disambiguate setup.py."""

from setuptools import setup


setup(
    name="disambiguate",
    version="1.0",
    description="Script to disambiguate reads mapping to multiple genomes.",
    author="Miika Ahdesmaki",
    license="MIT",
    install_requires=["pysam>=0.8.4"],
    py_modules=["disambiguate"],
    entry_points={
        "console_scripts": [
            "disambiguate=disambiguate:main",
            ],
        },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Utilities"
        ],
    )
