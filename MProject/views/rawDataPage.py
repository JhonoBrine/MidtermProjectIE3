import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

st.title('Insert Raw Data Dashboard')
st.write('You will be able to create your own table, and see it live immediately with the three data visualizations.')

# Initialize session state for data storage if it doesn't exist
if 'data' not in st.session_state:
    # Initialize with one default column and three default rows
    st.session_state.data = pd.DataFrame({"Column1": ["", "", ""]})

# --- Sidebar for Adding a New Column and Adding a New Row ---
st.sidebar.header("Manage Data")

# --- User Input Form for Adding a New Column ---
new_column_name = st.sidebar.text_input("Enter new column name (leave blank to skip):", "")
if st.sidebar.button("Add Column") and new_column_name:
    if new_column_name not in st.session_state.data.columns:
        st.session_state.data[new_column_name] = [""] * len(st.session_state.data)  # Initialize with empty strings
        st.sidebar.success(f"Column '{new_column_name}' added successfully.")
    else:
        st.sidebar.warning(f"Column '{new_column_name}' already exists.")

# --- Button to Add a New Row ---
if st.sidebar.button("Add Row"):
    new_row_df = pd.DataFrame({col: [""] for col in st.session_state.data.columns}, index=[0])  # Create a DataFrame for the new row
    st.session_state.data = pd.concat([st.session_state.data, new_row_df], ignore_index=True)  # Concatenate the new row
    st.sidebar.success("Row added successfully.")

# Before plotting, convert columns to numeric types
st.session_state.data = st.session_state.data.apply(pd.to_numeric, errors='coerce')

# --- Data Editing ---
st.write("### Current Data:")
# Allow users to edit the DataFrame directly
edited_data = st.data_editor(st.session_state.data, height=300, key='data_editor')

# Update session state with edited data
if not edited_data.equals(st.session_state.data):
    st.session_state.data = edited_data

# --- Functionality to Delete a Row ---
if not st.session_state.data.empty:
    selected_row = st.sidebar.selectbox("Select row to delete:", st.session_state.data.index, key='delete_row_select')
    if st.sidebar.button("Delete Selected Row"):
        st.session_state.data = st.session_state.data.drop(index=selected_row).reset_index(drop=True)
        st.sidebar.success("Row deleted successfully.")
else:
    st.sidebar.warning("No rows to delete.")

# --- Functionality to Delete a Column ---
if len(st.session_state.data.columns) > 1:  # Ensure there's more than one column to delete
    columns_to_delete = st.sidebar.selectbox("Select a column to delete:", st.session_state.data.columns)
    if st.sidebar.button("Delete Column"):
        st.session_state.data = st.session_state.data.drop(columns=[columns_to_delete])
        st.sidebar.success(f"Column '{columns_to_delete}' deleted successfully.")
else:
    st.sidebar.warning("You cannot delete the only remaining column.")

# --- Export Data to CSV ---
if st.sidebar.button("Export to CSV"):
    csv = st.session_state.data.to_csv(index=False)
    st.sidebar.download_button(label="Download CSV", data=csv, file_name='current_data.csv', mime='text/csv')

# --- Plotting Functions ---
def plot_histograms(data):
    try:
        if not data.empty and data.select_dtypes(include=['float', 'int']).shape[1] > 0:
            hist_data = [data[col].dropna() for col in data.select_dtypes(include=['float', 'int']).columns]
            group_labels = data.select_dtypes(include=['float', 'int']).columns.tolist()
            fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.5] * len(group_labels))
            fig.update_layout(title="Histogram") 
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Not enough numeric data to generate histograms.")
    except ValueError as e:
        st.error(f"Error plotting histograms: {e}")

def plot_heatmap(data):
    try:
        if len(data.select_dtypes(include=['float', 'int']).columns) > 1:
            corr = data.corr()
            fig_heatmap = px.imshow(corr, color_continuous_scale='Viridis', aspect='auto', title='Heatmap')
            st.plotly_chart(fig_heatmap, use_container_width=True)
    except Exception as e:
        st.error(f"Error plotting heatmap: {e}")

def plot_interactive_box_plots(data):
    try:
        if len(data.columns) > 0:
            for i in range(0, len(data.columns), 2):
                cols = st.columns(2)
                for j, col in enumerate(data.columns[i:i + 2]):
                    with cols[j]:
                        fig = px.box(data, y=col, title=f'Box Plot of {col}', points='all')
                        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error plotting box plots: {e}")

# --- Call the Plotting Functions ---
plot_histograms(st.session_state.data)
plot_heatmap(st.session_state.data)
plot_interactive_box_plots(st.session_state.data)
