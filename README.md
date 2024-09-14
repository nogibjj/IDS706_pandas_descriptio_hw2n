# IDS706_pandas_description_hw2
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/CICD.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/format.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/lint.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/test.yml/badge.svg)

## Requirements
* Python script using Polars for descriptive statistics
* Read a dataset (CSV or Excel)
* Generate summary statistics (mean, median, standard deviation)
* Create at least one data visualization

## Brief Introduction

### Dataset
<img src="https://seeklogo.com/images/N/nba-logo-59F0731E03-seeklogo.com.png" alt="NBA logo" width="400" />

#### [`NBA_2021.csv`](NBA_2021.csv)
This is the NBA 2021 global statistics table, which includes data for every player, such as PT (points), BL (blocks), and AT (assists).

### Python Scripts

In [`src/main.py`](src/main.py), This main.py script is used to read data from a CSV file, perform statistical analysis, and generate a data report. The script will generate three images and a PDF report. The three images are histograms showing the distribution of points, assists, and blocks for all players. Additionally, a PDF file with the report will be generated [here](NBA_2021_Report.pdf).

#### Descriptive Statistics

In [`src/main.py`](src/main.py), function `statistics()` will generate descriptive of the dataset, the output looks like:

- [Click here to find out what each column represents](https://www.nba.com/stats/help/glossary#pctfga)

|         | Age        | G          | GS         | MP         | FG         | FGA        | FG%        | 3P         | 3PA        | ORB        | DRB        | TRB        | AST        | STL        | BLK        | TOV        | PF         | PTS        |
|---------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
| count   | 705        | 705        | 705        | 705        | 705        | 705        | 703        | 705        | 705        | 705        | 705        | 705        | 705        | 705        | 705        | 705        | 705        | 705        |
| mean    | 25.870922  | 37.368794  | 16.941844  | 19.435887  | 3.166099   | 6.944681   | 0.443486   | 0.959858   | 2.714043   | 0.805816   | 2.774043   | 3.579291   | 1.933617   | 0.612199   | 0.416170   | 1.073759   | 1.622979   | 8.616596   |
| std     | 4.094976   | 21.269180  | 21.603760  | 9.155005   | 2.278288   | 4.718210   | 0.112544   | 0.877718   | 2.227645   | 0.729362   | 1.818019   | 2.384859   | 1.813998   | 0.393439   | 0.408948   | 0.812583   | 0.761734   | 6.272808   |
| min     | 19.000000  | 1.000000   | 0.000000   | 1.800000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   | 0.000000   |
| 25%     | 23.000000  | 19.000000  | 0.000000   | 12.500000  | 1.400000   | 3.500000   | 0.397000   | 0.200000   | 0.900000   | 0.300000   | 1.500000   | 1.900000   | 0.700000   | 0.300000   | 0.100000   | 0.500000   | 1.100000   | 4.000000   |
| 50%     | 25.000000  | 37.000000  | 5.000000   | 19.300000  | 2.600000   | 5.900000   | 0.439000   | 0.700000   | 2.200000   | 0.600000   | 2.500000   | 3.100000   | 1.400000   | 0.600000   | 0.300000   | 0.900000   | 1.600000   | 7.200000   |
| 75%     | 28.000000  | 57.000000  | 29.000000  | 26.900000  | 4.300000   | 9.300000   | 0.495500   | 1.500000   | 4.100000   | 1.000000   | 3.700000   | 4.800000   | 2.500000   | 0.900000   | 0.600000   | 1.400000   | 2.100000   | 11.700000  |
| max     | 40.000000  | 72.000000  | 72.000000  | 37.600000  | 11.200000  | 23.000000  | 1.000000   | 5.300000   | 12.700000  | 4.700000   | 10.100000  | 14.300000  | 11.700000  | 2.100000   | 3.400000   | 5.000000   | 4.000000   | 32.000000  |

#### points histogram

![pts_histogram.png](pts_histogram.png)

#### assists histogram

![ast_histogram.png](ast_histogram.png)

#### blocks histogram

![blk_histogram.png](blk_histogram.png)

### Extra Credit

All the images and report.pdf in this repo are not initially  submitted by me, but by CI/CD. In [CICD workflow](.github/workflows/CICD.yml), it will setup environment, check the format, run the test, run main.py, commit the output by github bot and push it to this repo.
