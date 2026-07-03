"""
report.py

Generate publication-ready benchmark reports.

The report is exported as a single Excel workbook with one worksheet
per benchmark scenario and an additional worksheet containing the
inferential statistics.
"""

from pathlib import Path

import pandas as pd


class BenchmarkReport:
    """
    Generates benchmark summary reports for the thesis.
    """

    def __init__(
        self,
        summary_df: pd.DataFrame,
        inferential_df: pd.DataFrame,
    ):
        """
        Initialize report generator.

        Args:
            summary_df: Output of BenchmarkStatistics.
            inferential_df: Output of InferentialStatistics.
        """
        self.summary_df = summary_df
        self.inferential_df = inferential_df

    def generate(self):
        """
        Generate the benchmark report workbook.
        """

        output = Path("outputs")
        output.mkdir(exist_ok=True)

        report_path = output / "benchmark_report.xlsx"

        with pd.ExcelWriter(report_path) as writer:

            scenarios = sorted(
                self.summary_df["scenario"].unique()
            )

            for scenario in scenarios:
                self._write_scenario_sheet(
                    writer,
                    scenario,
                )

            self.inferential_df.to_excel(
                writer,
                sheet_name="Inferential Statistics",
                index=False,
            )

        print(f"Report written to {report_path}")

    def _write_scenario_sheet(
        self,
        writer,
        scenario: str,
    ):
        """
        Create one worksheet for a benchmark scenario.
        """

        scenario_df = self.summary_df[
            self.summary_df["scenario"] == scenario
        ]

        mono = (
            scenario_df[
                scenario_df["architecture"] == "mono"
            ]
            .sort_values("vus")
            .reset_index(drop=True)
        )

        micro = (
            scenario_df[
                scenario_df["architecture"] == "micro"
            ]
            .sort_values("vus")
            .reset_index(drop=True)
        )

        report = pd.DataFrame(
            {
                "Virtual Users": mono["vus"],

                "Mono Avg (ms)": mono["avg_latency"],
                "Micro Avg (ms)": micro["avg_latency"],

                "Mono P95 (ms)": mono["p95_latency"],
                "Micro P95 (ms)": micro["p95_latency"],

                "Mono Req/s": mono["avg_requests"],
                "Micro Req/s": micro["avg_requests"],

                "Mono Error (%)":
                    mono["avg_error_rate"] * 100,

                "Micro Error (%)":
                    micro["avg_error_rate"] * 100,
            }
        )

        report["Latency Difference (ms)"] = (
            report["Mono Avg (ms)"]
            - report["Micro Avg (ms)"]
        ).round(2)

        report["Lower Latency"] = report[
            "Latency Difference (ms)"
        ].apply(
            lambda diff:
                "Microservices"
                if diff > 0
                else "Monolithic"
        )

        report.to_excel(
            writer,
            sheet_name=scenario.replace("-", " ").title(),
            index=False,
        )