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
- **S1_DataProcessing**

This notebook focuses on illustrating how to process **RNA-seq patient metadata**. It covers several tasks such as:  
  -data cleaning, 
  - imputation,
  - advanced feature engineering

particularly emphasizing drug categorization. The notebook utilizes **GPT-4** to perform the classification of medication data. Furthermore, it merges various datasets, and performs patient aggregation and feature engineering to calculate medication durations. The outcome is a comprehensive dataframe ready for further analysis, providing insights into patient medication patterns and their implications.

Patient_Selection.ipynb
This notebook focuses on selecting patient cohorts based on specific criteria. It includes steps for loading and merging datasets to form a comprehensive patient dataset, followed by descriptive analyses to understand the demographics and medication histories of the selected patients.

MovingFilesToMountFolder.ipynb
Designed to automate the process of moving files based on ID matching, this notebook outlines a function to transfer files from a source to a target directory, guided by IDs listed in a TSV file. It's a utility notebook that simplifies file management for further analysis.

S4_CentralizingCountData.ipynb
The notebook addresses the challenge of consolidating RNA-seq count data from multiple samples into a centralized dataset. It ensures gene identifier consistency and employs an efficient data appending strategy, setting a solid foundation for downstream analysis with reduced memory demand.

S5_TranscriptomicsEDA.ipynb
Focused on exploratory data analysis (EDA) of transcriptomics data, this notebook imports necessary packages, loads raw read counts, and performs initial data processing. It aims to uncover patterns and insights from RNA-seq data through various EDA techniques.

S6_DifferentialExpression.ipynb
This notebook delves into differential expression analysis, starting with the preparation of a txdb object from a GTF file and loading RNA-seq count data. It sets the stage for identifying genes or transcripts that show significant differences in expression across conditions or treatments.

Each notebook serves a distinct purpose in the overall workflow, from data preparation and file management to in-depth analysis of RNA-seq data, offering a comprehensive toolkit for researchers.

**Running the Jupyter Notebook:**
Navigate to the directory containing the Jupyter notebook.

**Streamlit Dashboard:**
The app has been deployed in stremlit share: https://rnaseq-patient-metadata-analysis-mpc4xsqfgfyzuqr7a2pscn.streamlit.app

# Contributions

This project is led by Felipe Núñez Villena, PhD. Contributions, feedback, and issues are welcome.
