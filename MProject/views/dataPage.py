import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Student Performance Dashboard')
st.write("📊 This dataset comprises various attributes related to student performance, including hours of study, practice, teamwork involvement, midterm exam scores, final exam scores, overall scores, and corresponding grades.")

# Loading the dataset
df_sample = pd.read_csv("MProject/assets/csv/Student_Grades.csv")

# Extract numeric columns for visualization
numeric_columns = df_sample.select_dtypes(include=[float, int]).columns.tolist()
selected_columns = st.sidebar.multiselect("Select columns to visualize", numeric_columns, default=numeric_columns)

# Filter by Midterm Exam Scores using a range slider
min_value, max_value = st.sidebar.slider(
    'Filter by Midterm Exam Scores (Range)',
    float(df_sample['MidTerm'].min()), 
    float(df_sample['MidTerm'].max()), 
    (float(df_sample['MidTerm'].min()), float(df_sample['MidTerm'].max()))
)

# Filter data based on the selected Midterm Exam range
df_filtered = df_sample[(df_sample['MidTerm'] >= min_value) & (df_sample['MidTerm'] <= max_value)]

# Clean data by removing rows with missing values
df_cleaned = df_filtered.dropna()

# --- Check for Empty Data ---
if df_cleaned.empty:
    st.warning("No data available after filtering. Please adjust your filters.")
else:
    # Ensure selected columns have enough data for visualization
    valid_columns = [col for col in selected_columns if len(df_cleaned[col].dropna().unique()) > 1]

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
                    fig = px.histogram(data, x=col, nbins=10, title=f"Histogram of {col}", 
                                       marginal="rug", histnorm='density', color_discrete_sequence=[color])
                    fig.update_layout(bargap=0.2, showlegend=False)
                    st.plotly_chart(fig, use_container_width=True)

        # --- Function for Plotting Heatmap ---
        def plot_heatmap(data, columns):
            if len(data[columns].columns) > 1:
                corr = data[columns].corr()
                fig_heatmap = px.imshow(corr,
                                        color_continuous_scale='Viridis',
                                        aspect='auto',
                                        title='Heatmap')
                st.plotly_chart(fig_heatmap, use_container_width=True)
            else:
                st.write("Not enough data to generate a correlation heatmap.")

        # --- Function for Plotting Box Plots Side by Side ---
        def plot_interactive_box_plots(data, columns):
            # Create two columns for side-by-side box plots
            for i in range(0, len(columns), 2):
                cols = st.columns(2)  # Create two columns
                
                for j, col in enumerate(columns[i:i+2]):  # Process two columns at a time
                    with cols[j]:  # Place each plot in a separate column
                        fig = px.box(data, y=col, title=f'Box Plot of {col}', points='all')
                        st.plotly_chart(fig, use_container_width=True)

        # Call the plotting functions
        plot_individual_histograms(df_cleaned, valid_columns)  # Plot individual histograms for each column in two columns
        plot_heatmap(df_cleaned, valid_columns)                # Plot heatmap
        plot_interactive_box_plots(df_cleaned, valid_columns)  # Plot box plots
