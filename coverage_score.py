""" Module to get coverage score."""

import sys
from xml.dom import minidom
from colorsys import hsv_to_rgb


def interpolate(weight, x, y):
    """Linear interpolation between x and y, given a weight."""
    return x * weight + (1 - weight) * y


def score_to_rgb_color(score, score_min, score_max):
    """Convert a score to a color."""
    normalized_score = max(0, (score - score_min) / (score_max - score_min))
    hsv_color = (interpolate(normalized_score, 0.33, 0), 1, 1)
    rgb_color = hsv_to_rgb(*hsv_color)
    rgb_color = tuple(int(255 * value) for value in rgb_color)
    return f"rgb{rgb_color}"


if __name__ == "__main__":
    file = minidom.parse("coverage.xml")
    coverage = file.getElementsByTagName("coverage")
    coverage = float(coverage[0].attributes["line-rate"].value)
    coverage_min, coverage_max = 0, 1
    if sys.argv[1] == "--score":
        print(f"{coverage:.1%}")
    elif sys.argv[1] == "--color":
        print(score_to_rgb_color(coverage, coverage_min, coverage_max))
    else:
        raise ValueError(f"Unknowed argument: {sys.argv[1]}")
