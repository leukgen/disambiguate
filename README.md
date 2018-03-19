# disambiguate

[![pypi badge][pypi_badge]][pypi_base]
[![travis badge][travis_badge]][travis_base]
[![codecov badge][codecov_badge]][codecov_base]
[![Paper][paper_badge]][paper]
[![DOI][zenodo_badge]][zenodo_base]

Disambiguation algorithm for reads aligned to two species (e.g. human and mouse genomes) from
Tophat, Hisat2, STAR or BWA mem.

⚠️ &nbsp; **IMPORTANT**: This repo is a fork of the original [`AstraZeneca-NGS/disambiguate`]. We fixed a couple of bugs, added CI testing, and automated deployment to [`PyPi`][pypi_base]. We are not the core developers but we may be able to help.

## Usage

This is a `python 2` abd `python 3` compatible program, install from `PyPi` with:

    # will install pysam
    pip install disambiguate

    # see usage
    disambiguate --help

## C++ Implementation

The C++ implementation depends on the availability of zlib and the Bamtools C++ API. For STAR alignments it is highly recommended to include the NM tag in the output when performing alignment (in fact this is a requirement for the C++ version). To compile the C++ program, use the following syntax in the same folder where the code is:

```bash
c++ -I /path/to/bamtools_c_api/include/ -I./ -L /path/to/bamtools_c_api/lib/ -o disambiguate dismain.cpp -lz -lbamtools
```

## Differences between the Python and C++ versions

1. The Python version can do natural name sorting of the reads (a necessary step) internally but for the C++ version the input BAM files _must_ be natural name sorted (internal natural name sorting not supported).

1. The flag -s (samplename prefix) must be provided as an input parameter to the C++ binary

A pre-compiled binary is also available in bioconda http://bioconda.github.io/recipes/ngs-disambiguate/README.html

## Citing

Ahdesmäki MJ, Gray SR, Johnson JH and Lai Z. Disambiguate: An open-source application for disambiguating two species in next generation sequencing data from grafted samples. F1000Research 2016, 5:2741, [DOI:10.12688/f1000research.10082.1][paper]

<!-- references -->
[`AstraZeneca-NGS/disambiguate`]: https://github.com/AstraZeneca-NGS/disambiguate
[codecov_badge]: https://codecov.io/gh/leukgen/disambiguate/branch/master/graph/badge.svg
[codecov_base]: https://codecov.io/gh/leukgen/disambiguate
[paper_badge]: https://img.shields.io/badge/paper-%F0%9F%93%84-blue.svg
[paper]: http://dx.doi.org/10.12688/f1000research.10082.1
[pypi_badge]: https://img.shields.io/pypi/v/disambiguate.svg
[pypi_base]: https://pypi.python.org/pypi/disambiguate
[travis_badge]: https://img.shields.io/travis/leukgen/disambiguate.svg
[travis_base]: https://travis-ci.org/leukgen/disambiguate
[zenodo_badge]: https://zenodo.org/badge/DOI/10.5281/zenodo.166017.svg
[zenodo_base]: https://doi.org/10.5281/zenodo.166017
