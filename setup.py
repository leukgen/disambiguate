"""disambiguate setup.py."""

from setuptools import setup


setup(
    name="_disambiguate",
    version="1.0.1",
    description=(
        "Disambiguate reads mapping to multiple genomes. "
        "This is a frozen release with some bug fixes of the original "
        "AstraZeneca-NGS/disambiguate v1.0."
        ),
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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities",
        ],
    extras_require={
        "test": [
            "pytest-cov>=2.5.1",
            ]
        },
    )
