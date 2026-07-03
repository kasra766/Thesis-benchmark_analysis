"""
main.py

Entry point of the benchmark analysis project.

Workflow:
1. Parse all benchmark JSON files.
2. Build a unified DataFrame.
3. Compute descriptive statistics.
4. Export results to CSV and Excel.
"""

from pathlib import Path

from analysis.parser import BenchmarkParser
from analysis.statistics import BenchmarkStatistics
from analysis.charts import BenchmarkCharts
from analysis.inferential import InferentialStatistics

def main():
    """Execute the complete benchmark analysis pipeline."""

    # Parse benchmark results
    parser = BenchmarkParser("benchmarks")
    benchmark_df = parser.parse()

    # Compute statistical summary
    statistics = BenchmarkStatistics(benchmark_df)
    summary_df = statistics.summary()

    # Display results in the console
    print(summary_df)
    print()
    print(f"Summary rows: {len(summary_df)}")

    # Perform inferential statistical analysis
    inferential = InferentialStatistics(benchmark_df)

    inferential_df = inferential.analyze()

    print(inferential_df)

    # Create output directories if they do not exist
    csv_output = Path("outputs/csv")
    excel_output = Path("outputs/excel")
    statistics_output = Path("outputs/statistics")
    statistics_output.mkdir(parents=True, exist_ok=True)

    csv_output.mkdir(parents=True, exist_ok=True)
    excel_output.mkdir(parents=True, exist_ok=True)

    # Export CSV
    summary_df.to_csv(
        csv_output / "benchmark_summary.csv",
        index=False,
    )

    # Export Excel
    summary_df.to_excel(
        excel_output / "benchmark_summary.xlsx",
        index=False,
    )


    inferential_df.to_csv(
        statistics_output / "inferential_statistics.csv",
        index=False,
    )

    inferential_df.to_excel(
        statistics_output / "inferential_statistics.xlsx",
        index=False,
    )

    # Generate benchmark charts
    charts = BenchmarkCharts(summary_df)
    charts.generate_all()

    print("Charts generated successfully.")



if __name__ == "__main__":
    main()