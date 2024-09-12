"""
IDS706 Miniproject Two

This module reads an NBA dataset, calculates statistics, generates visualizations,
and creates a PDF report with statistics on player performance.test
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


def read_dataset(path):
    """Read dataset from path."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, path)
    df = pd.read_csv(dataset_path)
    return df


def statistics(df):
    """Print dataset statistics."""
    print(df.describe())


def visualization(df, column_name, save_path):
    """Visualize dataset statistics."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[column_name], bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Distribution of {column_name} for NBA Players")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()


def generate_pdf(df, pdf_path="NBA_2021_Report.pdf"):
    """Generate dataset statitics report and save it to pdf."""
    pdf = FPDF()
    mean_pts, median_pts, std_pts = (
        df["PTS"].mean(),
        df["PTS"].median(),
        df["PTS"].std(),
    )
    mean_ast, median_ast, std_ast = (
        df["AST"].mean(),
        df["AST"].median(),
        df["AST"].std(),
    )
    mean_blk, median_blk, std_blk = (
        df["BLK"].mean(),
        df["BLK"].median(),
        df["BLK"].std(),
    )

    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="NBA 2021 Statistics Report", ln=True, align="C")

    pdf.set_font("Arial", "B", 12)
    pdf.cell(
        200,
        10,
        txt="Descriptive Statistics for Points (PTS), Assists (AST), and Blocks (BLK)",
        ln=True,
        align="L",
    )

    pdf.cell(200, 10, txt=f"Mean Points: {mean_pts:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Median Points: {median_pts:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Standard Deviation of Points: {std_pts:.2f}", ln=True)

    pdf.cell(200, 10, txt=f"Mean Assists: {mean_ast:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Median Assists: {median_ast:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Standard Deviation of Assists: {std_ast:.2f}", ln=True)

    pdf.cell(200, 10, txt=f"Mean Blocks: {mean_blk:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Median Blocks: {median_blk:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Standard Deviation of Blocks: {std_blk:.2f}", ln=True)

    pdf.cell(200, 10, txt="Distribution of Points", ln=True)
    pdf.image("pts_histogram.png", x=10, y=70, w=190)

    pdf.add_page()
    pdf.cell(200, 10, txt="Distribution of Assists", ln=True)
    pdf.image("ast_histogram.png", x=10, y=70, w=190)

    pdf.add_page()
    pdf.cell(200, 10, txt="Distribution of Blocks", ln=True)
    pdf.image("blk_histogram.png", x=10, y=70, w=190)

    pdf.output(pdf_path)
    print(f"PDF report generated: {pdf_path}")


def main():
    """Entrance to functions."""
    dataset_path = "../NBA_2021.csv"
    df = read_dataset(dataset_path)
    statistics(df)
    visualization(df, "PTS", "pts_histogram.png")
    visualization(df, "AST", "ast_histogram.png")
    visualization(df, "BLK", "blk_histogram.png")

    generate_pdf(df)


if __name__ == "__main__":
    main()
