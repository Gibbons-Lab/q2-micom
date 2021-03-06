"""Test if visualizations work."""

import os.path as path
import pandas as pd
import qiime2 as q2
import q2_micom as q2m
from tempfile import TemporaryDirectory

this_dir = q2m.tests.this_dir

results = q2.Artifact.load(path.join(this_dir, "data", "growth.qza"))


def test_growth_plots():
    r = results.view(q2m._formats_and_types.MicomResultsDirectory)
    with TemporaryDirectory(prefix="q2-micom-") as d:
        q2m.plot_growth(str(d), r)
        assert q2m.tests.check_viz(str(d))


def test_exchanges_per_sample():
    r = results.view(q2m._formats_and_types.MicomResultsDirectory)
    with TemporaryDirectory(prefix="q2-micom-") as d:
        q2m.exchanges_per_sample(str(d), r)
        assert q2m.tests.check_viz(str(d))


def test_exchanges_per_taxon():
    r = results.view(q2m._formats_and_types.MicomResultsDirectory)
    with TemporaryDirectory(prefix="q2-micom-") as d:
        q2m.exchanges_per_taxon(str(d), r)
        assert q2m.tests.check_viz(str(d))
