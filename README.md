# RNAseq-patient-metadata-analysis

Welcome to the GitHub repository for the analysis of RNA-seq patient metadata!.

This repository provides a comprehensive workflow that covers several tasks such as  **data preprocessing**, **feature engineering**, and **interactive visualization**.

# Project Overview

In this project, I extensively analyzed RNA-seq patient metadata. My primary focus was to derive insights from **patient medication data**, particularly the categorization of drugs between disease and non-disease modifying drugs, and those specifically for Parkinson's disease.

# Repository Structure

**Data_processing.ipynb**: A Jupyter notebook that outlines the entire data processing workflow, from data loading and cleaning to feature engineering. The detailed steps include:
Data loading for medication and RNA-seq metadata
RNAseq metadata processing and imputation
Medication data processing with topic classification using GPT-4
Feature engineering for computing medication durations
Data merging, categorization, and saving as output dataframe

**dashboard.py**: A Streamlit dashboard that provides an interactive visualization of the processed data. The dashboard features:
Filters for demographics, disease and genetic status, and other information
Pie chart visualization of the number of patients exposed to different drug categories
Box plot visualization showing the distribution of combined median time by drug bins
Detailed tabular data view
Getting Started

Prerequisites: Ensure you have the following libraries installed:
pandas, matplotlib, numpy, seaborn, streamlit, and other dependencies as mentioned in the notebook and dashboard script.

**Running the Jupyter Notebook:**
Navigate to the directory containing the Jupyter notebook.
Run the command: jupyter notebook Data_processing.ipynb

**Launching the Streamlit Dashboard:**
Navigate to the directory containing the dashboard.py script.
Run the command: streamlit run dashboard.py

# Contributions

This project is led by Felipe Núñez Villena, PhD. Contributions, feedback, and issues are welcome.
