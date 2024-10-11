import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Performance Dashboard")
st.write(
    "📊 This dataset comprises various attributes related to student performance, including hours of study, practice, teamwork involvement, midterm exam scores, final exam scores, overall scores, and corresponding grades."
)

# Loading the dataset
df_sample = pd.read_csv("MProject/assets/csv/Student_Grades.csv")

# Extract numeric columns for visualization
numeric_columns = df_sample.select_dtypes(include=[float, int]).columns.tolist()
selected_columns = st.sidebar.multiselect(
    "Select columns to visualize", numeric_columns, default=numeric_columns
)

# Filter by Midterm Exam Scores using a range slider
min_value, max_value = st.sidebar.slider(
    "Filter by Midterm Exam Scores (Range)",
    float(df_sample["MidTerm"].min()),
    float(df_sample["MidTerm"].max()),
    (float(df_sample["MidTerm"].min()), float(df_sample["MidTerm"].max())),
)

# Filter data based on the selected Midterm Exam range
df_filtered = df_sample[
    (df_sample["MidTerm"] >= min_value) & (df_sample["MidTerm"] <= max_value)
]

# Clean data by removing rows with missing values
df_cleaned = df_filtered.dropna()

# --- Check for Empty Data ---
if df_cleaned.empty:
    st.warning("No data available after filtering. Please adjust your filters.")
else:
    # Ensure selected columns have enough data for visualization
    valid_columns = [
        col for col in selected_columns if len(df_cleaned[col].dropna().unique()) > 1
    ]

    if not valid_columns:
        st.warning("Please select columns with sufficient data to visualize.")
    else:
        # Define a list of colors to use for the histograms
        colors = px.colors.qualitative.Plotly  # Get a predefined color set from Plotly

        # --- Function for Plotting Individual Histograms in Two Columns ---
        def plot_individual_histograms(data, columns):
            cols = st.columns(2)  # Create two columns for side-by-side display
            for i, col in enumerate(columns):
                color = colors[i % len(colors)]  # Cycle through the colors
                with cols[i % 2]:  # Alternate between the two columns
                    fig = px.histogram(
                        data,
                        x=col,
                        nbins=10,
                        title=f"Histogram of {col}",
                        marginal="rug",
                        histnorm="density",
                        color_discrete_sequence=[color],
                    )
                    fig.update_layout(bargap=0.2, showlegend=False)
                    st.plotly_chart(fig, use_container_width=True)

        # --- Function for Plotting Heatmap ---
        def plot_heatmap(data, columns):
            if len(data[columns].columns) > 1:
                corr = data[columns].corr()
                fig_heatmap = px.imshow(
                    corr,
                    color_continuous_scale="Viridis",
                    aspect="auto",
                    title="Heatmap",
                )
                st.plotly_chart(fig_heatmap, use_container_width=True)
            else:
                st.write("Not enough data to generate a correlation heatmap.")

        # --- Function for Plotting Box Plots Side by Side ---
        def plot_interactive_box_plots(data, columns):
            # Create two columns for side-by-side box plots
            for i in range(0, len(columns), 2):
                cols = st.columns(2)  # Create two columns

                for j, col in enumerate(
                    columns[i : i + 2]
                ):  # Process two columns at a time
                    with cols[j]:  # Place each plot in a separate column
                        fig = px.box(
                            data, y=col, title=f"Box Plot of {col}", points="all"
                        )
                        st.plotly_chart(fig, use_container_width=True)

        # Call the plotting functions
        plot_individual_histograms(df_cleaned, valid_columns)
        st.write(
            "In this visualization, one commonality across all categories is the presence of a bimodal to multimodal distribution of values, except for the 'Teamwork' category. In the 'Teamwork' category, the lowest value occurs most frequently, indicating a right-skewed distribution. The visualization also reveals that, in all categories, the highest frequency of data points is concentrated near the minimum value. Overall, the charts suggest that students are experiencing limited collaboration, with lower scores being the most prevalent."
        )
        plot_heatmap(df_cleaned, valid_columns)
        st.write(
            "In this correlation matrix, we can see that all categories have a strong correlations to each other. Final exam has a correlation of 1 with the Scores and the midterm having 0.99 with the Scores. The rest of the categories range correlation values of 0.83 to 0.92 which means that a student having high value in this category will like have a high value in the other category. Example will be that the correlation between Hours and Scores is 0.98, it means that a student that spends more time studying will likely to earn higher scores."
        )
        plot_interactive_box_plots(df_cleaned, valid_columns)
        st.write(
            """
        Each box plot consists of five important parts that correspond to key statistical values, which match the 25th, 50th, and 75th percentiles, as seen in the data table. These values also match the results shown in Image 2.1, which displays the box plot, and Image 1.0, which shows the results from the snippet of code.

        - **Count**: Number of entries in the dataset.
        - **Mean**: The average value.
        - **Standard deviation (std)**: The spread or variability of the data.
        - **Minimum (min)**: The smallest value in the dataset.
        - **25th, 50th, 75th percentiles**: These represent the data distribution, giving an idea of where most values lie.
        - **Maximum (max)**: The largest value in the dataset.

        Below is the summary of these statistics for the student performance dataset:
        """
        )

        st.write(
            """
        ### Summary Statistics

        The summary statistics provide a quick overview of the key attributes in the dataset. For each numeric column, you can see:

        1. Whiskers:
        - The lower whisker represents the minimum value of the dataset, matching the minimum value in the table and Image 2.1.
        - The upper whisker represents the maximum value of the dataset, aligning with the maximum value in the table and as seen in Image 2.1.

        2. Boxes:
        - The lower box reflects the first quartile (Q1), representing the 25th percentile of the data. This matches the Q1 value in the table and the code output in Image 1.0.
        - The upper box reflects the third quartile (Q3), representing the 75th percentile, which also matches the values in the table and Image 2.1.
        """
        )
