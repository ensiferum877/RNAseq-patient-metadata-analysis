
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Insert custom CSS to adjust column widths
st.set_page_config(layout="wide")

# Change the color of the sidebar
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #838b8b;
    }
</style>
""", unsafe_allow_html=True)



# Load the data
def load_data():
    return pd.read_csv('Outputs/DF_03102023_v2.csv')

data = load_data()
data = data.drop(columns=['Unnamed: 0'])

# Dropdown filters in the sidebar with titles
st.sidebar.header("Filters")

# Demographics
st.sidebar.subheader("Demographics")
selected_sex = st.sidebar.selectbox("Select Sex", ["All"] + sorted(data['Sex'].dropna().unique()))
selected_race = st.sidebar.selectbox("Select Race", ["All"] + sorted(data['Race'].dropna().unique()))
selected_age_bin = st.sidebar.selectbox("Select Age Bin", ["All"] + sorted(data['Age (Bin)'].dropna().unique()))

# Disease and Genetic Status
st.sidebar.subheader("Disease and Genetic Status")
selected_disease_status = st.sidebar.selectbox("Select Disease Status", ["All"] + sorted(data['Disease Status'].dropna().unique()))
selected_genetic_status = st.sidebar.selectbox("Select Genetic Status", ["All"] + sorted(data['Genetic Status'].dropna().unique()))
selected_diagnosis = st.sidebar.selectbox("Select Diagnosis", ["All"] + sorted(data['Diagnosis'].dropna().unique()))

# Other Information
st.sidebar.subheader("Other Information")
selected_case_control = st.sidebar.selectbox("Select Case Control", ["All"] + sorted(data['Case Control'].dropna().unique()))
selected_month = st.sidebar.selectbox("Select Month", ["All"] + sorted(data['Month'].dropna().unique()))
selected_drug_category = st.sidebar.selectbox('Select Drug Category', ['All'] + list(data['Drug_Category'].unique()))

# Filter the data based on dropdown selections
if selected_sex != "All":
    data = data[data['Sex'] == selected_sex]
if selected_race != "All":
    data = data[data['Race'] == selected_race]
if selected_age_bin != "All":
    data = data[data['Age (Bin)'] == selected_age_bin]
if selected_disease_status != "All":
    data = data[data['Disease Status'] == selected_disease_status]
if selected_genetic_status != "All":
    data = data[data['Genetic Status'] == selected_genetic_status]
if selected_diagnosis != "All":
    data = data[data['Diagnosis'] == selected_diagnosis]
if selected_case_control != "All":
    data = data[data['Case Control'] == selected_case_control]
if selected_month != "All":
    data = data[data['Month'] == selected_month]
if selected_drug_category != 'All':
    data = data[data['Drug_Category'] == selected_drug_category]

# SECTION 1
# Calculate metrics for filtered data
unique_patno_count = data['PATNO'].nunique()
filtered_rows_with_patno = data['PATNO'].count()
medication_columns = ['Disease_modifying_drug', 'PD_indicated_drug',
                      'Non_disease_modifying_drug', 'Disease-modifying-drugs_time(Median)',
                      'Non-disease-modifying-drugs_time(Median)', 'parkinson_medication_time']
missing_medication_data_count = data[data[medication_columns].isna().all(axis=1)]['PATNO'].nunique()

# Streamlit App with centered title
st.markdown("<h1 style='text-align: center;background-color:#0066cc;'>PPMI Data Dashboard</h1>", unsafe_allow_html=True)


# Display numbers with colored bar plot for Diagnosis using matplotlib
col1, col2, col3 = st.columns([0.8, 1, 1])
with col1:
    st.markdown("<h5 style='text-align: center;'>Data in numbers</h3>", unsafe_allow_html=True)
    st.write("Number of patients: ")
    st.markdown(f"<h1 style='text-align: center; color: white;'>{unique_patno_count}</h1>", unsafe_allow_html=True)
    st.write("Patients with RNA-seq data but missing medication Information: ")
    st.markdown(f"<h1 style='text-align: center; color: red;'>{missing_medication_data_count}</h1>", unsafe_allow_html=True)
    st.write("Total of RNA-seq samples: ")
    st.markdown(f"<h1 style='text-align: center; color: blue;'>{filtered_rows_with_patno}</h1>", unsafe_allow_html=True)
with col2:
    st.markdown("<h5 style='text-align: center;'>Distribution of Samples by Diagnosis</h3>", unsafe_allow_html=True)
    diagnosis_counts = data['Diagnosis'].value_counts()
    colors = plt.cm.viridis(np.linspace(0, 1, len(diagnosis_counts)))
    plt.figure(figsize=(10,11)) # Modify figure sizes
    plt.bar(diagnosis_counts.index, diagnosis_counts.values, color=colors)
    plt.xticks(rotation=45, ha="right",fontsize=30)
    plt.yticks(fontsize=30)
    st.pyplot(plt)
with col3:
    # Line-dot plot for "Distribution of Samples by Month"
    st.markdown("<h5 style='text-align: center;'>Distribution of Samples by Month</h3>", unsafe_allow_html=True)
    month_counts = data['Month'].value_counts().sort_index()
    plt.figure(figsize=(12.1,16))
    plt.plot(month_counts.index, month_counts.values, marker='o', linestyle='-', color='blue', markersize=8)
    plt.xticks(rotation=45, ha="right", fontsize=30)
    plt.yticks(fontsize=30)
    st.pyplot(plt)
    

# Separating line
st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)

# SECTION 2
# Display numbers with colored bar plot for Diagnosis using matplotlib
col4, col5 = st.columns([1, 1])

with col4:
    st.markdown("<h5 style='text-align: center;'>Number of Patients Exposed to Different Drug Categories</h3>", unsafe_allow_html=True)

    drug_category_counts = data.groupby('Drug_Category')['PATNO'].nunique()
    
    labels = drug_category_counts.index.tolist()
    sizes = drug_category_counts.values.tolist()
    colors = plt.cm.Paired(range(len(sizes)))

    # Custom function to display absolute numbers on the pie chart
    def func(pct, allsizes):
        absolute = int(pct/100.*np.sum(allsizes))
        return "{:.1f}%\n({:d} patients)".format(pct, absolute)

    # Plotting the Pie Chart
    fig, ax = plt.subplots(figsize=(8,10))
    wedges, texts, autotexts = ax.pie(sizes, autopct=lambda pct: func(pct, sizes),
        startangle=90,
        colors=colors,
        wedgeprops=dict(width=0.45),
        pctdistance=1.2,  # Adjusted distance for external annotations
        textprops={'fontsize': 13})

    # Drawing arrows connecting the text to the pie slices
    for text, autotext, wedge in zip(texts, autotexts, wedges):
        x, y = wedge.center
        x1, y1 = autotext.get_position()
        # Compute a point that's a fraction of the way between the pie slice and the annotation
        frac = 0.6 # Adjust this value to change the arrow starting point
        x2 = x + frac * (x1 - x)
        y2 = y + frac * (y1 - y)
        ax.annotate("", xy=(x1, y1), xytext=(x2, y2),
                    arrowprops=dict(arrowstyle="-", color="black"))

    ax.legend(labels, loc="center", prop={'size': 12})
    st.pyplot(fig)


with col5:
    st.markdown("<h5 style='text-align: center;'>'Distribution of Combined Median Time by Total Drug Bins'</h3>", unsafe_allow_html=True)
    bins_total = [-1, 2, 5, 10, 20, 50, 100]
    labels_total = ['0-2', '3-5', '6-10', '11-20', '21-50', '51-100']

    data['Total_Drug_Bins'] = pd.cut(data['Total_Drugs'], bins=bins_total, labels=labels_total)

    # List of columns to keep
    selected_columns = ['Total_Drug_Bins', 'Total_Drugs','Total_Drugs_Time(Median)','PATNO', 'Disease Status', 'Genetic Status', 'Diagnosis', 
                    'Case Control', 'Clinical Event', 'Month', 'Sex', 'Race', 'Age (Bin)', 'Drug_Category']

    # Filter the data
    filtered_data = data[selected_columns]

    # Drop duplicates based on PATNO
    filtered_data_unique = filtered_data.drop_duplicates(subset='PATNO', keep='last')


    # Generating the box plot with overlaid individual data points
    plt.figure(figsize=(8.5, 8.3))
    sns.boxplot(x='Total_Drug_Bins', y='Total_Drugs_Time(Median)', data=filtered_data_unique, palette="coolwarm", width=0.5)

    # Adding data points with horizontal jitter
    for i, bin_name in enumerate(labels_total):
        y_values = filtered_data_unique[filtered_data_unique['Total_Drug_Bins'] == bin_name]['Total_Drugs_Time(Median)'].values
        x_values = [i + np.random.uniform(-0.15, 0.15) for _ in range(len(y_values))]
        plt.plot(x_values, y_values, 'o', color=".25", markersize=2.5, alpha=0.7, linestyle='None')

    plt.xlabel('Total Number of Drugs (Bins)', fontsize=12)
    plt.ylabel('Combined Median Time of Exposure', fontsize=12)
    st.pyplot(plt)

# SECTION 3
# Separating line
st.markdown("<hr style='height:2px;border-width:0;color:gray;background-color:gray'>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left;'>Detailed data view </h3>", unsafe_allow_html=True)
st.dataframe(data, width=1400, height=400)
