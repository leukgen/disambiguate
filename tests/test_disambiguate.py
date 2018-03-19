"""Disambiguate tests."""

from argparse import Namespace
from os.path import join
from os.path import dirname
from os.path import abspath
from os.path import isfile

import disambiguate

ROOT = abspath(dirname(__file__))
DATA = join(ROOT, "data")


def test_disambiguate(tmpdir):
    parser = disambiguate.get_parser()
    args = [
        join(DATA, "human.bam"),
        join(DATA, "mouse.bam"),
        "-o", tmpdir.strpath,
        ]

    args = parser.parse_args(args)
    disambiguate.run_disambiguate(args)
    assert "50" in tmpdir.join("human_summary.txt").read()
