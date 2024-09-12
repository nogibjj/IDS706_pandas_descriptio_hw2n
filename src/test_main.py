from main import statistics, visualization, read_dataset

df = read_dataset("../NBA_2021.csv")


def test_stat():
    statistics(df)


def test_hist():
    visualization(df, "PTS", "pts_histogram.png")
    visualization(df, "AST", "ast_histogram.png")
    visualization(df, "BLK", "blk_histogram.png")
