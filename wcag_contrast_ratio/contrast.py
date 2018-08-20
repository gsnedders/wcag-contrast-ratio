from __future__ import division

__all__ = ["rgb", "passes_AA", "passes_AAA", "rgb_as_int"]


def rgb(rgb1, rgb2):
    for r, g, b in (rgb1, rgb2):
        if not 0.0 <= r <= 1.0:
            raise ValueError("r is out of valid range (0.0 - 1.0)")
        if not 0.0 <= g <= 1.0:
            raise ValueError("g is out of valid range (0.0 - 1.0)")
        if not 0.0 <= b <= 1.0:
            raise ValueError("b is out of valid range (0.0 - 1.0)")

    l1 = _relative_luminance(*rgb1)
    l2 = _relative_luminance(*rgb2)

    if l1 > l2:
        return (l1 + 0.05) / (l2 + 0.05)
    else:
        return (l2 + 0.05) / (l1 + 0.05)


def _relative_luminance(r, g, b):
    r = _linearize(r)
    g = _linearize(g)
    b = _linearize(b)

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _linearize(v):
    if v <= 0.03928:
        return v / 12.92
    else:
        return ((v + 0.055) / 1.055) ** 2.4


def passes_AA(contrast, large=False):
    if large:
        return contrast >= 3.0
    else:
        return contrast >= 4.5


def passes_AAA(contrast, large=False):
    if large:
        return contrast >= 4.5
    else:
        return contrast >= 7.0


def translate(value, value_min_range, value_max_range, min_range, max_range):
    value_span = value_max_range - value_min_range
    span = max_range - min_range
    scaled = float(value - value_min_range) / float(value_span)
    return min_range + (scaled * span)


def rgb_as_int(rgb1, rgb2):
    n_rgb1 = tuple([translate(c, 0, 255, 0, 1) for c in rgb1])
    n_rgb2 = tuple([translate(c, 0, 255, 0, 1) for c in rgb2])
    return rgb(n_rgb1, n_rgb2)
