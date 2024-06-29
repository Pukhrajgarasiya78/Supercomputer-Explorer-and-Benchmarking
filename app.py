import streamlit as st
import pandas as pd

# Load processed data from pickle files
df = pd.read_pickle('combined_data.pkl')
df_2022_merged = pd.read_pickle('merged_data_2022.pkl')

# Function to filter data based on user input
def filter_data(input_type, input_value, num_rows):
    if input_type == 'Year':
        filtered_df = df[df['Year'] == int(input_value)].head(num_rows)
    elif input_type == 'Country':
        df_filtered = df.dropna(subset=['Country'])
        filtered_df = df_filtered[df_filtered['Country'].str.contains(input_value, case=False)].head(num_rows)
    elif input_type == 'Manufacturer':
        df_filtered = df.dropna(subset=['Manufacturer'])
        filtered_df = df_filtered[df_filtered['Manufacturer'].str.contains(input_value, case=False)].head(num_rows)
    elif input_type == 'Computer/System Model':
        df_filtered = df_2022_merged.dropna(subset=['Computer/System Model'])
        filtered_df = df_filtered[df_filtered['Computer/System Model'].str.contains(input_value, case=False)].head(num_rows)
    elif input_type == 'Power (kW)':
        df_filtered = df_2022_merged.dropna(subset=['Power (kW)'])
        filtered_df = df_filtered[df_filtered['Power (kW)'].astype(str).str.contains(input_value, case=False)].head(num_rows)
    elif input_type == 'Continent':
        df_filtered = df.dropna(subset=['Continent'])
        filtered_df = df_filtered[df_filtered['Continent'].str.contains(input_value, case=False)].head(num_rows)
    elif input_type == 'Processor Technology':
        df_filtered = df.dropna(subset=['Processor Technology'])
        filtered_df = df_filtered[df_filtered['Processor Technology'].str.contains(input_value, case=False)].head(num_rows)
    elif input_type == 'Total Cores':
        filtered_df = df[df['Total Cores'].astype(str).str.contains(input_value, case=False)].head(num_rows)
    elif input_type == 'Segment':
        df_filtered = df.dropna(subset=['Segment'])
        filtered_df = df_filtered[df_filtered['Segment'].str.contains(input_value, case=False)].head(num_rows)
    else:  # Assume input_type == 'Computer Name'
        df_filtered = df_2022_merged.dropna(subset=['Name'])
        filtered_df = df_filtered[df_filtered['Name'].str.contains(input_value, case=False)].head(num_rows)
    
    return filtered_df.iloc[:, :23]  # Limit columns to the first 23 for display

# Streamlit UI
def main():
    st.set_page_config(page_title='Supercomputer Benchmarking', layout='wide')

    # Custom CSS styles
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #080800; /* Sidebar background color (blue) */
            padding: 10px;
        }
        .reportview-container .main .block-container {
            background-color: #080800; /* Main content background color (light blue) */
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3, h4, h5, h6 {
            color: white; /* Text color for headings */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Supercomputer Explorer and Benchmarking')

    # Sidebar for user input
    with st.sidebar.expander('Input Options', expanded=True):
        input_type = st.selectbox('Select Input Type', ['Computer Name','Year', 'Country', 'Manufacturer', 'Computer/System Model', 'Power (kW)', 'Continent', 'Processor Technology', 'Total Cores', 'Segment'])

        num_rows = st.slider('Number of Rows', min_value=1, max_value=20, value=5)

    if input_type == 'Year':
        year_options = df['Year'].unique().tolist()
        year = st.selectbox('Select Year', year_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Year', year, num_rows)
            st.header(f'Top {num_rows} Supercomputers in {year}')
            st.dataframe(filtered_df)

    elif input_type == 'Country':
        country_options = df['Country'].dropna().unique().tolist()
        country = st.selectbox('Select Country', country_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Country', country, num_rows)
            st.header(f'Top {num_rows} Supercomputers in {country}')
            st.dataframe(filtered_df)

    elif input_type == 'Manufacturer':
        manufacturer_options = df['Manufacturer'].dropna().unique().tolist()
        manufacturer = st.selectbox('Select Manufacturer', manufacturer_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Manufacturer', manufacturer, num_rows)
            st.header(f'Top {num_rows} Supercomputers by {manufacturer}')
            st.dataframe(filtered_df)

    elif input_type == 'Computer/System Model':
        model_options = df_2022_merged['Computer/System Model'].dropna().unique().tolist()
        model = st.selectbox('Select Computer/System Model', model_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Computer/System Model', model, num_rows)
            st.header(f'Top {num_rows} Supercomputers with {model}')
            st.dataframe(filtered_df)

    elif input_type == 'Power (kW)':
        power_options = df_2022_merged['Power (kW)'].dropna().unique().tolist()
        power = st.selectbox('Select Power (kW)', power_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Power (kW)', power, num_rows)
            st.header(f'Top {num_rows} Supercomputers with {power} kW')
            st.dataframe(filtered_df)

    elif input_type == 'Continent':
        continent_options = df['Continent'].dropna().unique().tolist()
        continent = st.selectbox('Select Continent', continent_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Continent', continent, num_rows)
            st.header(f'Top {num_rows} Supercomputers in {continent}')
            st.dataframe(filtered_df)

    elif input_type == 'Processor Technology':
        processor_options = df['Processor Technology'].dropna().unique().tolist()
        processor = st.selectbox('Select Processor Technology', processor_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Processor Technology', processor, num_rows)
            st.header(f'Top {num_rows} Supercomputers with {processor} Processor Technology')
            st.dataframe(filtered_df)

    elif input_type == 'Total Cores':
        core_options = df['Total Cores'].astype(str).dropna().unique().tolist()
        cores = st.selectbox('Select Total Cores', core_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Total Cores', cores, num_rows)
            st.header(f'Top {num_rows} Supercomputers with {cores} Total Cores')
            st.dataframe(filtered_df)

    elif input_type == 'Segment':
        segment_options = df['Segment'].dropna().unique().tolist()
        segment = st.selectbox('Select Segment', segment_options)
        if st.button('Show Top Computers'):
            filtered_df = filter_data('Segment', segment, num_rows)
            st.header(f'Top {num_rows} Supercomputers in {segment} Segment')
            st.dataframe(filtered_df)

    elif input_type == 'Computer Name':
        computer_options = df_2022_merged['Name'].dropna().unique().tolist()
        computer_name = st.selectbox('Select Computer Name', computer_options)
        if st.button('Show Computer Specifications'):
            filtered_df = filter_data('Computer Name', computer_name, num_rows)
            st.header(f'Specifications of {computer_name}')
            st.dataframe(filtered_df)

if __name__ == '__main__':
    main()
