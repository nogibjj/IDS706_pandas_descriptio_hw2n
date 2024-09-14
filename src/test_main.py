import os
from main import statistics, visualization, generate_pdf, read_dataset

df = read_dataset("../NBA_2021.csv")


def _file_exists_and_not_empty(filepath):
    return os.path.exists(filepath) and os.path.getsize(filepath) > 0


def test_stat():
    statistics(df)


def test_hist():
    try:
        visualization(df, "PTS", "pts_histogram.png")
        visualization(df, "AST", "ast_histogram.png")
        visualization(df, "BLK", "blk_histogram.png")
        flag = True
    except Exception as e:
        flag = False
        print(f"Plot histgram failed: {e}")
    assert flag
    assert _file_exists_and_not_empty("pts_histogram.png")
    assert _file_exists_and_not_empty("ast_histogram.png")
    assert _file_exists_and_not_empty("blk_histogram.png")


def test_pdf_gen():
    generate_pdf(df, "NBA_2021_Report.pdf")
    assert _file_exists_and_not_empty("NBA_2021_Report.pdf")
