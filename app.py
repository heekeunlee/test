import streamlit as st
import pandas as pd
import numpy as np

# Load the data
# If seaborn is not installed, we'll create a sample dataset
try:
    from seaborn import load_dataset
    faithful = load_dataset("geyser")
except ImportError:
    # Create a sample dataset if seaborn is not available
    np.random.seed(0)
    faithful = pd.DataFrame({
        'waiting': np.random.normal(55, 15, 300).round(2),
        'eruptions': np.random.normal(3, 1, 300).round(2)
    })

# Set up the app layout
st.title("Old Faithful Geyser Data")

# Sidebar
bins = st.sidebar.slider("Number of bins:", min_value=1, max_value=50, value=30)

# Main panel
st.subheader("Histogram of waiting times")

# Generate the histogram using Streamlit's built-in chart function
hist_values, bin_edges = np.histogram(faithful['waiting'], bins=bins)
st.bar_chart(pd.DataFrame({'count': hist_values}, index=bin_edges[:-1]))

# Display some statistics
st.subheader("Dataset Statistics")
st.write(faithful.describe())

# Show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(faithful)