import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Cardiology Patient Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel file)", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    # Preview of the dataset
    st.write("### Preview of the Dataset")
    st.subheader("First Few Data Samples")
    st.dataframe(df.head())
    st.subheader("Last Few Data Samples")
    st.dataframe(df.tail())

    # Step 3: Statistical summary
    st.subheader("Statistical Summary")
    st.dataframe(df.describe())

    # Calculate and visualize admissions per month
    st.subheader("Admissions per Month")

    if "month year" in df.columns:
        # Requirement #4: Calculate number of admissions per month
        monthly = df.groupby("month year").size()

        # DISPLAY the monthly counts (this was missing)
        st.write("### Number of Admissions per Month")
        st.dataframe(monthly.reset_index(name="Admissions"))

        # Requirement #5: Visualize (your original plot)
        fig, ax = plt.subplots()
        monthly.plot(ax=ax, marker='o')
        ax.set_ylabel("Number of Admissions")
        ax.set_xlabel("Month - Year")
        ax.set_title("Admissions Over Time")
        plt.xticks(rotation=45)

        st.pyplot(fig)

    else:
        st.error("Column 'month year' not found in dataset.")

else:
    st.info("Please upload a dataset to begin.")


