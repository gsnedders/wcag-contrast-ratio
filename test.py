from hypothesis import given
from hypothesis.strategies import floats, tuples
import pytest

import wcag_contrast_ratio as contrast

color_channel = floats(0.0, 1.0)
color = tuples(color_channel, color_channel, color_channel)


@pytest.mark.parametrize("rgb1,rgb2,expected",
                         [[(0.0, 0.0, 0.0), (1.0, 1.0, 1.0), 21.0],
                          [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1.0],
                          [(0.0, 198/255.0, 0.0), (0.0, 0.0, 198/255.0), 5.000229313902297]])
def test_contrast(rgb1, rgb2, expected):
    c1 = contrast.rgb(rgb1, rgb2)
    c2 = contrast.rgb(rgb2, rgb1)
    assert c1 == expected
    assert c2 == expected


@pytest.mark.parametrize("c,expected,large_expected",
                         [(0.0, False, False),
                          (2.9, False, False),
                          (3.0, False, True),
                          (3.1, False, True),
                          (4.4, False, True),
                          (4.5, True, True),
                          (4.6, True, True),
                          (6.9, True, True),
                          (7.0, True, True),
                          (7.1, True, True),
                          (21.0, True, True)])
def test_passes_AA(c, expected, large_expected):
    got = contrast.passes_AA(c, large=False)
    assert got == expected
    got_large = contrast.passes_AA(c, large=True)
    assert got_large == large_expected


@pytest.mark.parametrize("c,expected,large_expected",
                         [(0.0, False, False),
                          (2.9, False, False),
                          (3.0, False, False),
                          (3.1, False, False),
                          (4.4, False, False),
                          (4.5, False, True),
                          (4.6, False, True),
                          (6.9, False, True),
                          (7.0, True, True),
                          (7.1, True, True),
                          (21.0, True, True)])
def test_passes_AAA(c, expected, large_expected):
    got = contrast.passes_AAA(c, large=False)
    assert got == expected
    got_large = contrast.passes_AAA(c, large=True)
    assert got_large == large_expected


@given(color, color)
def test_hypothesis_contrast(rgb1, rgb2):
    c1 = contrast.rgb(rgb1, rgb2)
    c2 = contrast.rgb(rgb1, rgb2)
    assert 1.0 <= c1 <= 21.0
    assert c1 == c2
