"""
statistics.py

This module computes descriptive statistics from the parsed benchmark
results. The generated summary is used for charts, tables, and the
performance evaluation chapter of the thesis.
"""

import pandas as pd


class BenchmarkStatistics:
    """
    Computes descriptive statistics for benchmark results.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize with the parsed benchmark DataFrame.

        Args:
            dataframe: Raw benchmark results.
        """
        self.df = dataframe

    def summary(self) -> pd.DataFrame:
        """
        Calculate summary statistics grouped by architecture,
        benchmark scenario, and number of virtual users.

        Returns:
            DataFrame containing aggregated benchmark statistics.
        """

        grouped = (
            self.df.groupby(
                ["architecture", "scenario", "vus"],
                as_index=False,
            )
            .agg(
                # Average latency across the three runs
                avg_latency=("avg_ms", "mean"),

                # Standard deviation of latency
                std_latency=("avg_ms", "std"),

                # Minimum observed latency
                min_latency=("avg_ms", "min"),

                # Maximum observed latency
                max_latency=("avg_ms", "max"),

                # Average median response time
                median_latency=("med_ms", "mean"),

                # Average 95th percentile response time
                p95_latency=("p95_ms", "mean"),

                # Average throughput
                avg_requests=("req_per_sec", "mean"),

                # Average iterations per second
                avg_iterations=("iter_per_sec", "mean"),

                # Average error rate
                avg_error_rate=("error_rate", "mean"),
            )
            .round(2)
        )

        return grouped