# Student Performance: EDA and Process Improvement

This project demonstrates my exploratory data analysis (EDA), analytical reasoning, and ability to communicate findings through a professional stakeholder report. Using a **synthetic student performance dataset**, I examine patterns associated with exam scores and develop process-improvement recommendations concerning attendance, study habits, and access to resources.

The primary emphasis is the progression from data exploration and analytical decisions to findings and stakeholder communication. The project culminates in a written report presented as a Quarto webpage. The synthetic data support a practice case study; the findings alone do not justify action in a real school.

## Start here

| Artifact | Location and purpose |
| --- | --- |
| Exploratory analysis | [notebooks/data_explore.ipynb](notebooks/data_explore.ipynb): data inspection, cleaning decisions, descriptive statistics, correlations, and visual exploration |
| Report workflow | [notebooks/workflow.ipynb](notebooks/workflow.ipynb): performance snapshot metrics and attendance visualization using the saved processed dataset |
| Final Word report | [reports/Data_Driven_Process_Improvement_Report_EDITED.docx](reports/Data_Driven_Process_Improvement_Report_EDITED.docx): edited stakeholder report |
| Original Word report | [reports/Data_Driven_Process_Improvement_Report_RAW.docx](reports/Data_Driven_Process_Improvement_Report_RAW.docx): preserved original report |
| Web report source | [index.qmd](index.qmd): Quarto presentation of the completed report; local rendering produces `_site/index.html` |
| Markdown conversion | [reports/report.md](reports/report.md): retained Markdown version of the Word report |

## From raw data to stakeholder communication

1. **Inspect the raw data.** The source file is `data/raw/StudentPerformanceFactors.csv`. The EDA notebook records the Kaggle dataset identifier `lainguyn123/student-performance-factors`. Each row represents a student and factors associated with exam performance.
2. **Document preparation decisions.** In `notebooks/data_explore.ipynb`, I inspect missing values, standardize column names, assign categorical types, and examine an exam score above 100. The notebook records my decision to retain that extreme value and saves cleaned data to `data/processed/silver_data.csv`.
3. **Explore relationships and interpret findings.** The EDA uses distributions, group summaries, correlations, and visualizations to examine exam scores and related factors. Supporting working notes are preserved in [reports/data_explore.md](reports/data_explore.md) and [reports/descriptive_analysis.md](reports/descriptive_analysis.md).
4. **Prepare report evidence.** `notebooks/workflow.ipynb` reads the existing `data/processed/gold_df.parquet` for report metrics and an attendance chart. The checked-in notebooks do not document the export that created this Parquet file, so this repository should not be treated as a fully automated end-to-end pipeline.
5. **Communicate findings and recommendations.** The Word report brings the findings, figures, interpretations, and supporting references together for stakeholders. [reports/dashboard.md](reports/dashboard.md) preserves the audience and report-planning notes. The completed report was converted to Markdown/Quarto for web presentation.

## Repository organization

- `notebooks/`: the analytical work and report workflow, including saved outputs.
- `data/raw/` and `data/processed/`: local source and prepared datasets. The `data/` directory is excluded from Git, so these files are not included in a fresh clone.
- `reports/`: Word reports, the Markdown conversion, working notes, the saved profiling report (`raw_spf_profile.html`), and the existing editorial helper in `editorial_qa/`.
- `reports/figures/`: images referenced by `reports/report.md`.
- `figures/`: images referenced by the Quarto report. Both figure locations are retained to preserve existing links.
- `index.qmd`, `_quarto.yml`, and `styles.css`: web report content, render configuration, and styling.
- `project_1_dashboard/`: shared path configuration and retained starter-template scripts. The analytical workflow lives in the notebooks; the template scripts are not a completed analysis or model-training pipeline.
- `pyproject.toml` and `uv.lock`: existing Python dependency configuration and lockfile.
- `technical_fluency_project_refresher.xlsx`: supporting project workbook.
- `docs/`, `models/`, and `references/`: retained template placeholder directories.

## Render the web report locally

With the Quarto CLI installed and available on your PATH, run from the repository root:

```sh
quarto render index.qmd --no-execute
```

Open `_site/index.html` to read the rendered report. This builds the webpage from the existing report text and figures without executing analysis. The project configuration renders only `index.qmd`; it does not render the notebooks. Generated `_site/` output and `.quarto/` cache files are excluded from Git. Rendering locally does not publish or deploy the report.

The local datasets and Python environment are needed to execute the notebooks, but are not needed to render the report. Reviewing the saved notebooks and report does not require rerunning the analysis.

## AI Use Disclosure

I personally performed the EDA, made the analytical decisions, interpreted the findings, and wrote the original report, including its conclusions and recommendations. AI served as a supporting tool for grammar and readability editing, Python syntax and visualization-code assistance, formatting and citation cleanup, conversion of the completed Word report to Markdown/Quarto, Quarto webpage styling, and repository/documentation support. Final analytical decisions, interpretations, and conclusions remained mine.
