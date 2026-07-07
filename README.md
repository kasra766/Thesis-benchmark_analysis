# Benchmark Analysis

Benchmark Analysis is a Python-based data analysis project developed for the thesis *Performance Comparison of Monolithic and Microservices Architectures*. It processes raw k6 benchmark results and produces descriptive statistics, inferential statistical analysis, publication-quality charts, and Excel reports.

## Features

* Parse raw k6 benchmark outputs
* Compute descriptive statistics
* Generate latency and throughput charts
* Perform inferential statistical analysis (Welch's t-test, confidence intervals, Cohen's d)
* Export CSV and Excel reports
* Produce publication-ready PNG and PDF figures

## Project Structure

```
benchmark-analysis/
├── analysis/
├── data/
├── outputs/
│   ├── charts/
│   ├── reports/
│   └── statistics/
├── main.py
└── requirements.txt
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place benchmark results inside the `data/` directory and run:

```bash
python main.py
```

Generated outputs are written to the `outputs/` directory.

## Technologies

* Python
* Pandas
* NumPy
* SciPy
* Matplotlib
* OpenPyXL

## Purpose

This project automates the statistical analysis of benchmark results collected from the monolithic and microservices implementations used in the thesis.

