# RNAseq-patient-metadata-analysis

Welcome to the GitHub repository for the analysis of RNA-seq patient metadata!.

This repository provides a comprehensive workflow that covers several tasks such as  **data preprocessing**, **feature engineering**, and **interactive visualization**.

# Project Overview

In this project, I extensively analyzed RNA-seq data. The analysis focused on the creation of several notebooks that spans from:

- **data pre-processing**
- **patient selection**
- **file management**
- **exploratory analyses** to
- **differential expression**

Our objective is to leverage this rich dataset to identify biomarkers for patients with Parkinson Disease (PD).

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

**Streamlit Dashboard:**
The app has been deployed in stremlit share: https://rnaseq-patient-metadata-analysis-mpc4xsqfgfyzuqr7a2pscn.streamlit.app

# Contributions

This project is led by Felipe Núñez Villena, PhD. Contributions, feedback, and issues are welcome.
