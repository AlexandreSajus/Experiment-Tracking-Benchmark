""" Module to get pylint score."""

from pylint.lint import Run
from utils import score_to_rgb_color

if __name__ == "__main__":
    options = ["pyflow", "--output-format=pylint_score.MyReporterClass"]
    results = Run(options, exit=False)
    score = results.linter.stats.global_note
    score_min = 0
    score_max = 10
    print(score_to_rgb_color(score, score_min=score_min, score_max=score_max))
