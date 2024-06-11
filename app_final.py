# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import geopandas as gpd
# import folium
# from streamlit_folium import folium_static

# # Load the Telangana shapefile
# telangana = gpd.read_file('ShapeFiles/TS_District_Boundary_33/TS_District_Boundary_33_FINAL.shp')

# # Ensure the GeoDataFrame has a single geometry column
# telangana = telangana.to_crs(epsg=4326)

# # Convert the GeoDataFrame to a DataFrame for Altair
# telangana['geometry'] = telangana['geometry'].apply(lambda x: x.__geo_interface__)
# telangana_df = telangana


# agriculture_files = {
#     "Ground Water Level": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Agriculture/Telangana_GrounWaterLevel_Overall/Telangana_GrounWaterLevel_Overall.csv',
#     "Suryapet Crop": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Agriculture/Suryapet_mandal_wise_crop/Suryapet_mandal_wise_crop.csv',
#     "Cash Crops": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Agriculture/Cash_crops_2016-2017/Cash_crops_2016-2017.csv',
#     "Adilabad Crop": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Agriculture/Adilabad_mandal_wise_crop/Adilabad_mandal_wise_crop.csv',
#     "Cereals and Millets": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Agriculture/Cereals_and_Millets_2016-2017/Cereals_and_Millets_2016-2017.csv'
# }

# health_files = {
#     "Urban Health Centers": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Health/Urban Health Centers.csv',
#     "Primary Health Centers": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Health/Primary Health Centers.csv',
#     "District Health Assets": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Health/District wise health general asset .csv',
#     "Area of Hospitals": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Health/Area of Hospitals .csv',
#     "Community Health Centers": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Health/Community Health Centers.csv',
#     "Overview of Hospitals": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/Health/overview_of_hospitals.csv'
# }

# infrastructure_files = {
#     "Classification of Roads": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/infrastructure/Classification of Roads.csv',
#     "Mission Kakateeya": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/infrastructure/Mission Kakateeya.csv',
#     "Electricity Connections": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/infrastructure/Electricity Connections.csv',
#     "2BHK Housing Scheme": '/Users/likithgannarapu/Desktop/MU/Sem 6/Social Computing/Streamlit/Extraction_f/infrastructure/2BHK Housing Scheme.csv'
# }


# # Define a function to load and display data
# def load_and_display_data(file_path):
#     df = pd.read_csv(file_path)
#     st.write(df)
#     return df

# # Set page configuration as the very first Streamlit command
# st.set_page_config(page_title="Telangana Open Data Dashboard", layout="wide")

# # Define the functions for each sector page
# def health():
#     st.title("Health Sector")
#     st.write("""
#         Information about health-related data and initiatives in Telangana.
#     """)

# def agriculture():
#     st.title("Agriculture Sector")
#     st.write("""
#         Insights into agricultural practices, crop yields, and farming policies.
#     """)

# def infrastructure():
#     st.title("Infrastructure Sector")
#     st.write("""
#         Details on water quality monitoring, pollution levels, and clean water initiatives.
#     """)

# def team():
#     st.title("Our Team")
#     st.subheader("Meet the team behind the dashboard")
#     # Add your team member information here
#     team_members = [ "Likki Aashritha","Likith Gannarapu", "Aniruddha Srihari", "Sreeja M", "Harsha Vardhan Reddy"]
#     # Display each team member's name
#     for member in team_members:
#         st.text(member)

# # Define the sectors page function
# def sectors():
#     st.title("Sectors")
#     sectors_list = ["Health", "Agriculture", "Infrastructure"]
#     sector_selection = st.selectbox("Choose a sector:", sectors_list)
    
#     if sector_selection == "Health":
#         sub_sectors = ["Urban Health Centers", "Primary Health Centers", "District Health Assets", "Area of Hospitals", "Community Health Centers", "Overview of Hospitals"]
#         sub_sector_selection = st.selectbox("Choose a sub-sector:", sub_sectors)

#         df_health = pd.read_csv(health_files[sub_sector_selection])
#         st.dataframe(df_health)
#         # Visualization for Health data
#         if 'Urban Health Centers' in sub_sector_selection:
            
#             fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='Districts', y='SITE AREA ACRES', title='Urban Health Centers by District')
#             st.plotly_chart(fig0)

#         elif sub_sector_selection == 'Primary Health Centers':
#             df_health_grouped = df_health.groupby('VILLAGE NAME', as_index=False).sum()
#             fig = px.bar(df_health_grouped, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_district_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_district_grouped, x='Districts', y='SITE AREA ACRES', title='Urban Health Centers by District')
#             st.plotly_chart(fig0)
        
#         elif sub_sector_selection == 'District Health Assets':
#             df_health_grouped = df_health.groupby('Districts_Hospital', as_index=False).sum()
#             fig = px.bar(df_health_grouped, x='Districts_Hospital', y='AREA Sq.mts', title='District Health Assets by Hospital')
#             st.plotly_chart(fig)
    
#         elif sub_sector_selection == 'Community Health Centers':
#             fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='Districts', y='SITE AREA ACRES', title='Community Health Centers by District')
#             st.plotly_chart(fig0)

#         elif sub_sector_selection == 'Overview of Hospitals':
#             data = df_health
#             fig = px.bar(data, x='hospitals', y='health_subcentres', title='Number of health_subcentres by District')
#             st.plotly_chart(fig)

#             top_districts_doctors = (data.groupby('hospitals')['doctors_in_all_hospitals']
#                                      .sum().nlargest(5).reset_index())
#             st.subheader("Top 5 Districts with Most Doctors")
#             fig = px.line(top_districts_doctors, x='hospitals', y='doctors_in_all_hospitals', title='Top 5 Districts with Most Doctors')
#             st.plotly_chart(fig)
#             st.write("This line chart highlights the top 5 districts with the highest number of doctors.")
    
#         elif sub_sector_selection == 'Area of Hospitals':
#             fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_grouped = df_health.groupby('District')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='District', y='SITE AREA ACRES', title='Community Health Centers by District')
#             st.plotly_chart(fig0)
        
#     elif sector_selection == "Agriculture":
#         sub_sectors = ["Ground Water Level", "Suryapet Crop", "Cash Crop", "Adilabad Crop", "Cereals and Millets"]
#         sub_sector_selection = st.selectbox("Choose a sub-sector:", sub_sectors)
#         df_agriculture = pd.read_csv(agriculture_files[sub_sector_selection])
#         st.dataframe(df_agriculture)

#         if sub_sector_selection == "Ground Water Level":
#             fig = px.bar(df_agriculture, x='mandal', y='value', title='Ground Water Level by Mandal')
#             st.plotly_chart(fig)

#             df_grouped = df_agriculture.groupby('district')['value'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='district', y='value', title='Ground Water Level by District')
#             st.plotly_chart(fig0)

#         if sub_sector_selection == "Suryapet Crop":

                
#             def load_and_aggregate_data(df):
#                 aggregated_df = df.groupby(['year', 'crop'])['actualareasown'].sum().reset_index()
#                 return aggregated_df

#             aggregated_df = load_and_aggregate_data(df_agriculture)

#             # Create a line chart showing the trend of actual areas owned over the years for each crop
#             fig = px.line(aggregated_df, x="year", y="actualareasown",
#             color="crop", title='Trend of Actual Areas Owned Over the Years by Crop',
#             labels={'actualareasown': 'Actual Areas Owned'})

#             # Display the plot in Streamlit
#             st.plotly_chart(fig)

#             # fig = px.bar(df_agriculture, x='mandalname', y='actualareasown', title='Actual area sown Crop Area by Mandal')
#             # st.plotly_chart(fig)

#             # fig0 = px.bar(df_agriculture, x='mandalname', y='normalareasown', title='Normal area sown Crop Area by Mandal')
#             # st.plotly_chart(fig0)
    
    
            
# # Define the home page function
# def home():
#     st.title('')
#     st.markdown("""
#         <div style='text-align: center;'>
#             <img src='https://th-i.thgim.com/public/news/cities/Hyderabad/xqc285/article68242644.ece/alternates/FREE_1200/Telangana%20State%20emblem.jpg' 
#                  width='150'>
#         </div>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#         <h1 style='text-align: center;'>Telangana Open Data Dashboard</h1>
#     """, unsafe_allow_html=True)
#     st.markdown("""
#         <div style='text-align: center;'>
#             <p style='font-size: 12px;'>
#                 Telangana, known for its vibrant culture and rapid development, is a state in southern India. 
#                 Explore the data dashboard to uncover insights into Telangana's key sectors—Agriculture, Health, and Infrastructure.
#                 Discover valuable information and gain actionable insights for informed decision-making.
#             </p>
#             <div style="display: flex; justify-content: center;">
#                 <img src="https://images.moneycontrol.com/static-mcnews/2023/03/Article-3-Image1-770x433.jpg?impolicy=website&width=770&height=431" style="width: 150px; margin-right: 10px;">
#                 <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRO_9Grw3i0fLlsfzCWkiiVI0RmwOhW3KhfEulsq-2RE4yxRg8mxT1wKuTef-y94K5_C2M&usqp=CAU" style="width: 150px; margin-right: 10px;">
#                 <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd9UfRxGcFnJZdVMlPqfhFvv29ODHhUSCScw&s" style="width: 150px;">
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

#     st.markdown("<h2 style='text-align: center; font-size: 12px;'>Welcome to the Visual Space!</h2>", unsafe_allow_html=True)
#     st.markdown("""
#         ### Overview
#         Explore Telangana's diverse sectors—Agriculture, Health, and Infrastructure—with interactive data visualizations.
#         Gain valuable insights and make informed decisions with our comprehensive data analysis tools.""")

#     # Load shapefiles
#     districts = gpd.read_file('ShapeFiles/TS_District_Boundary_33/TS_District_Boundary_33_FINAL.shp')
#     mandals = gpd.read_file('ShapeFiles/TS_Mandal_Boundary_632/TS_Mandal_Boundary_632_FINAL.shp')
    
#     # Streamlit app
#     # st.title("Telangana Districts and Mandals")

#     # Create a map centered around Telangana
#     telangana_map = folium.Map(location=[18.1124, 79.0193], zoom_start=7)

#     # Add districts to the map
#     district_layer = folium.GeoJson(
#         districts,
#         name="Districts",
#         style_function=lambda feature: {
#             'fillColor': 'transparent',
#             'color': 'red',
#             'weight': 2
#         },
#         tooltip=folium.GeoJsonTooltip(fields=['DISTRICT_N'], aliases=['District Name:'])  # Adjust fields as per your dataset
#     ).add_to(telangana_map)

#     # Add mandals to the map
#     mmandal_layer = folium.GeoJson(
#         mandals,
#         name="Mandals",
#         style_function=lambda feature: {
#             'fillColor': 'transparent',
#             'color': 'green',
#             'weight': 1
#         },
#         tooltip=folium.GeoJsonTooltip(fields=['MANDAL_NAM', 'DISTRICT_N'], aliases=['Mandal Name:', 'District Name:'])
#     ).add_to(telangana_map)

#     # Add a layer control
#     folium.LayerControl().add_to(telangana_map)
#     # Display the map in Streamlit
#     folium_static(telangana_map)

#     st.markdown("""

#         ### About Us
#         We are a team of 5 passionate individuals dedicated to providing easy access to valuable data with enhanced data visualization and analysis capabilities. Our goal is to empower users with insightful tools to explore and understand Telangana's key sectors.

#         Click below to go to official Open Data Portal of Telangana
#     """)
#     st.link_button("Tealngana Open Data", "https://data.telangana.gov.in/")

# def future_implementations():
#         st.write("""Here we are using Adilabad weather data to predict wind speed using temperature and humidity as inputs. This can be extended to any other districts data. """)
#         st.link_button("Click here for the prediction","https://wind-speed-prediction.streamlit.app/")


# # Page configuration
# pages = {
#     "Home": home,
#     "Sectors": sectors,
#     "Future Implementations": future_implementations,
#     "Team": team
# }

# def main():
#     # Navigation sidebar
#     st.sidebar.title("Navigation")
#     selection = st.sidebar.radio("", list(pages.keys()))
    
#     # Display the selected page with its contents
#     pages[selection]()

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import folium
from streamlit_folium import folium_static

# Load the Telangana shapefile
telangana = gpd.read_file('ShapeFiles/TS_District_Boundary_33/TS_District_Boundary_33_FINAL.shp')
# Ensure the GeoDataFrame has a single geometry column
telangana = telangana.to_crs(epsg=4326)

# Convert the GeoDataFrame to a DataFrame for Altair
telangana['geometry'] = telangana['geometry'].apply(lambda x: x.__geo_interface__)
telangana_df = telangana


agriculture_files = {
    
    "Ground Water Level": 'DataSets/Agriculture/Telangana_GrounWaterLevel_Overall/Telangana_GrounWaterLevel_Overall.csv',
    "Suryapet Crop": 'DataSets/Agriculture/Suryapet_mandal_wise_crop/Suryapet_mandal_wise_crop.csv',
    "Cash Crop": 'DataSets/Agriculture/Cash_crops_2016-2017/Cash_crops_2016-2017.csv',
    "Adilabad Crop": 'DataSets/Agriculture/Adilabad_mandal_wise_crop/Adilabad_mandal_wise_crop.csv',
    "Cereals and Millets": 'DataSets/Agriculture/Cereals_and_Millets_2016-2017/Cereals_and_Millets_2016-2017.csv'
}

health_files = {
    "Urban Health Centers": 'DataSets/Health/Urban Health Centers.csv',
    "Primary Health Centers": 'DataSets/Health/Primary Health Centers.csv',
    "District Health Assets": 'DataSets/Health/District wise health general asset .csv',
    "Area of Hospitals": 'DataSets/Health/Area of Hospitals .csv',
    "Community Health Centers": 'DataSets/Health/Community Health Centers.csv',
    "Overview of Hospitals": 'DataSets/Health/overview_of_hospitals.csv'
}

infrastructure_files = {
    "Classification of Roads": 'DataSets/infrastructure/Classification of Roads.csv',
    "Mission Kakateeya": 'DataSets/infrastructure/Mission Kakateeya.csv',
    "Electricity Connections": 'DataSets/infrastructure/Electricity Connections.csv',
    "2BHK Housing Scheme": 'DataSets/infrastructure/2BHK Housing Scheme.csv',
    "Gram Panchayat Roads": 'DataSets/infrastructure/Gram Pamchayat (Roads).csv'
}

# Define a function to load and display data
def load_and_display_data(file_path):
    df = pd.read_csv(file_path)
    st.write(df)
    return df

# Set page configuration as the very first Streamlit command
st.set_page_config(page_title="Telangana Open Data Dashboard", layout="wide")

# Define the functions for each sector page
def health():
    st.title("Health Sector")
    st.write("""
        Information about health-related data and initiatives in Telangana.
    """)

def agriculture():
    st.title("Agriculture Sector")
    st.write("""
        Insights into agricultural practices, crop yields, and farming policies.
    """)

def infrastructure():
    st.title("Infrastructure Sector")
    st.write("""
        Details on water quality monitoring, pollution levels, and clean water initiatives.
    """)

def team():
    st.title("Our Team")
    st.subheader("Meet the team behind the dashboard")
    # Add your team member information here
    team_members = [ "Likki Aashritha","Likith Gannarapu", "Aniruddha Srihari", "Sreeja M", "Harsha Vardhan Reddy"]
    # Display each team member's name
    for member in team_members:
        st.text(member)

# Define the sectors page function
# def sectors():
#     st.title("Sectors")
#     sectors_list = ["Health", "Agriculture", "Infrastructure"]
#     sector_selection = st.selectbox("Choose a sector:", sectors_list)
    
#     if sector_selection == "Health":
#         sub_sectors = ["Urban Health Centers", "Primary Health Centers", "District Health Assets", "Area of Hospitals", "Community Health Centers", "Overview of Hospitals"]
#         sub_sector_selection = st.selectbox("Choose a sub-sector:", sub_sectors)

#         df_health = pd.read_csv(health_files[sub_sector_selection])
#         st.dataframe(df_health)
#         # Visualization for Health data
#         if 'Urban Health Centers' in sub_sector_selection:
            
#             fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='Districts', y='SITE AREA ACRES', title='Urban Health Centers by District')
#             st.plotly_chart(fig0)

#         elif sub_sector_selection == 'Primary Health Centers':
#             df_health_grouped = df_health.groupby('VILLAGE NAME', as_index=False).sum()
#             fig = px.bar(df_health_grouped, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_district_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_district_grouped, x='Districts', y='SITE AREA ACRES', title='Urban Health Centers by District')
#             st.plotly_chart(fig0)
        
#         elif sub_sector_selection == 'District Health Assets':
#             df_health_grouped = df_health.groupby('Districts_Hospital', as_index=False).sum()
#             fig = px.bar(df_health_grouped, x='Districts_Hospital', y='AREA Sq.mts', title='District Health Assets by Hospital')
#             st.plotly_chart(fig)
    
#         elif sub_sector_selection == 'Community Health Centers':
#             fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='Districts', y='SITE AREA ACRES', title='Community Health Centers by District')
#             st.plotly_chart(fig0)

#         elif sub_sector_selection == 'Overview of Hospitals':
#             data = df_health
#             fig = px.bar(data, x='hospitals', y='health_subcentres', title='Number of health_subcentres by District')
#             st.plotly_chart(fig)

#             top_districts_doctors = (data.groupby('hospitals')['doctors_in_all_hospitals']
#                                      .sum().nlargest(5).reset_index())
#             st.subheader("Top 5 Districts with Most Doctors")
#             fig = px.line(top_districts_doctors, x='hospitals', y='doctors_in_all_hospitals', title='Top 5 Districts with Most Doctors')
#             st.plotly_chart(fig)
#             st.write("This line chart highlights the top 5 districts with the highest number of doctors.")
    
#         elif sub_sector_selection == 'Area of Hospitals':
#             fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
#             st.plotly_chart(fig)

#             df_grouped = df_health.groupby('District')['SITE AREA ACRES'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='District', y='SITE AREA ACRES', title='Community Health Centers by District')
#             st.plotly_chart(fig0)
        
#     elif sector_selection == "Agriculture":
#         sub_sectors = ["Ground Water Level", "Suryapet Crop", "Cash Crop", "Adilabad Crop", "Cereals and Millets"]
#         sub_sector_selection = st.selectbox("Choose a sub-sector:", sub_sectors)
#         df_agriculture = pd.read_csv(agriculture_files[sub_sector_selection])
#         st.dataframe(df_agriculture)

#         if sub_sector_selection == "Ground Water Level":
#             fig = px.bar(df_agriculture, x='mandal', y='value', title='Ground Water Level by Mandal')
#             st.plotly_chart(fig)

#             df_grouped = df_agriculture.groupby('district')['value'].sum().reset_index()
#             fig0 = px.bar(df_grouped, x='district', y='value', title='Ground Water Level by District')
#             st.plotly_chart(fig0)

#         if sub_sector_selection == "Suryapet Crop":

                
#             def load_and_aggregate_data(df):
#                 aggregated_df = df.groupby(['year', 'crop'])['actualareasown'].sum().reset_index()
#                 return aggregated_df

#             aggregated_df = load_and_aggregate_data(df_agriculture)

#             # Create a line chart showing the trend of actual areas owned over the years for each crop
#             fig = px.line(aggregated_df, x="year", y="actualareasown",
#             color="crop", title='Trend of Actual Areas Owned Over the Years by Crop',
#             labels={'actualareasown': 'Actual Areas Owned'})

#             # Display the plot in Streamlit
#             st.plotly_chart(fig)

#             # fig = px.bar(df_agriculture, x='mandalname', y='actualareasown', title='Actual area sown Crop Area by Mandal')
#             # st.plotly_chart(fig)

#             # fig0 = px.bar(df_agriculture, x='mandalname', y='normalareasown', title='Normal area sown Crop Area by Mandal')
#             # st.plotly_chart(fig0)
        
def sectors():
    st.title("Sectors")
    sectors_list = ["Health", "Agriculture", "Infrastructure"]
    sector_selection = st.selectbox("Choose a sector:", sectors_list)
    
    if sector_selection == "Health":
        sub_sectors = ["Urban Health Centers", "Primary Health Centers", "District Health Assets", "Area of Hospitals", "Community Health Centers", "Overview of Hospitals"]
        sub_sector_selection = st.selectbox("Choose a sub-sector:", sub_sectors)
        
        df_health = pd.read_csv(health_files[sub_sector_selection])
        st.dataframe(df_health)
        
        if sub_sector_selection == "Urban Health Centers":
            fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Urban Health Centers by Villages')
            st.plotly_chart(fig)
            df_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
            fig0 = px.bar(df_grouped, x='Districts', y='SITE AREA ACRES', title='Urban Health Centers by District')
            st.plotly_chart(fig0)
        
        elif sub_sector_selection == "Primary Health Centers":
            df_health_grouped = df_health.groupby('VILLAGE NAME', as_index=False).sum()
            fig = px.bar(df_health_grouped, x='VILLAGE NAME', y='SITE AREA ACRES', title='Primary Health Centers by Villages')
            st.plotly_chart(fig)
            df_district_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
            fig0 = px.bar(df_district_grouped, x='Districts', y='SITE AREA ACRES', title='Primary Health Centers by District')
            st.plotly_chart(fig0)
        
        elif sub_sector_selection == "District Health Assets":
            df_health_grouped = df_health.groupby('Districts_Hospital', as_index=False).sum()
            fig = px.bar(df_health_grouped, x='Districts_Hospital', y='AREA Sq.mts', title='District Health Assets by Hospital')
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Community Health Centers":
            fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Community Health Centers by Villages')
            st.plotly_chart(fig)
            df_grouped = df_health.groupby('Districts')['SITE AREA ACRES'].sum().reset_index()
            fig0 = px.bar(df_grouped, x='Districts', y='SITE AREA ACRES', title='Community Health Centers by District')
            st.plotly_chart(fig0)
        
        elif sub_sector_selection == "Overview of Hospitals":
            data = df_health
            fig = px.bar(data, x='hospitals', y='health_subcentres', title='Number of Health Subcentres by District')
            st.plotly_chart(fig)
            top_districts_doctors = (data.groupby('hospitals')['doctors_in_all_hospitals']
                                     .sum().nlargest(5).reset_index())
            st.subheader("Top 5 Districts with Most Doctors")
            fig = px.line(top_districts_doctors, x='hospitals', y='doctors_in_all_hospitals', title='Top 5 Districts with Most Doctors')
            st.plotly_chart(fig)
            st.write("This line chart highlights the top 5 districts with the highest number of doctors.")
        
        elif sub_sector_selection == "Area of Hospitals":
            fig = px.bar(df_health, x='VILLAGE NAME', y='SITE AREA ACRES', title='Area of Hospitals by Village')
            st.plotly_chart(fig)
            df_grouped = df_health.groupby('District')['SITE AREA ACRES'].sum().reset_index()
            fig0 = px.bar(df_grouped, x='District', y='SITE AREA ACRES', title='Area of Hospitals by District')
            st.plotly_chart(fig0)
        
    elif sector_selection == "Agriculture":
        sub_sectors = ["Ground Water Level", "Suryapet Crop", "Cash Crop", "Adilabad Crop", "Cereals and Millets"]
        sub_sector_selection = st.selectbox("Choose a sub-sector:", sub_sectors)
        df_agriculture = pd.read_csv(agriculture_files[sub_sector_selection])
        st.dataframe(df_agriculture)
        
        if sub_sector_selection == "Ground Water Level":
            fig = px.bar(df_agriculture, x='mandal', y='value', title='Ground Water Level by Mandal')
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Suryapet Crop":
            def load_and_aggregate_data(df):
                aggregated_df = df.groupby(['year', 'crop'])['actualareasown'].sum().reset_index()
                return aggregated_df
            aggregated_df = load_and_aggregate_data(df_agriculture)
            fig = px.line(aggregated_df, x="year", y="actualareasown", color="crop", title='Trend of Actual Areas Owned Over the Years by Crop',
                          labels={'actualareasown': 'Actual Areas Owned'})
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Cash Crop":
            fig = px.bar(df_agriculture, x='crop', y='area_total', title='Cash Crops Area by Crop')
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Adilabad Crop":
            # fig = px.bar(df_agriculture, x='mandal_name', y='actual_area', title='Adilabad Crop Area by Mandal')
            # st.plotly_chart(fig)
            fig = px.bar(df_health, x='mandal_name', y='actual_area', title='Adilabad Crop Area by Mandal')
            st.plotly_chart(fig)
            df_grouped = df_health.groupby('District')['actual_area'].sum().reset_index()
            fig0 = px.bar(df_grouped,x='mandal_name', y='actual_area', title='Adilabad Crop Area by District')
            st.plotly_chart(fig0)
        
        elif sub_sector_selection == "Cereals and Millets":
            fig = px.bar(df_agriculture, x='crop', y='area_total', title='Cereals and Millets Area by Crop')
            st.plotly_chart(fig)
        
    elif sector_selection == "Infrastructure":
        sub_sectors = ["2BHK Housing Scheme", "Classification of Roads", "Electricity Connections", "Gram Panchayat Roads", "Mission Kakateeya"]
        sub_sector_selection = st.selectbox("Choose a sub-sector:", sub_sectors)
        df_infrastructure = pd.read_csv(infrastructure_files[sub_sector_selection])
        st.dataframe(df_infrastructure)
        
        if sub_sector_selection == "2BHK Housing Scheme":
            fig = px.bar(df_infrastructure, x='Districts', y=['Houses Allotted', 'Houses Allotted Rural', 'Houses Allotted Urban', 'Houses Sanctioned'],
                         title='2BHK Housing Scheme by District')
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Classification of Roads":
            fig = px.bar(df_infrastructure, x='District', y=['Four Lane Roads', 'Double Lane Roads', 'Intermediate Lane Roads', 'Single Lane Roads'],
                         title='Classification of Roads by District')
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Electricity Connections":
            fig = px.bar(df_infrastructure, x='Districts', y=['Domestic Connections', 'Industrial Connections', 'Agriculture Connections', 'Commercial Connections', 'Other Connections'],
                         title='Electricity Connections by District')
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Gram Panchayat Roads":
            fig = px.bar(df_infrastructure, x='Districts', y=['GPs having BT roads', 'GPs to be covered with BT roads', 'Total Habitations (other than GPs)', 
                                                             'Habitations having all weather roads', 'Habitations not having all weather roads   '],
                         title='Gram Panchayat Roads by District')
            st.plotly_chart(fig)
        
        elif sub_sector_selection == "Mission Kakateeya":
            fig = px.bar(df_infrastructure, x='Districts', y=['Minor Irrigation Tanks', 'Sanctions Mission Kakatiya Phase-I', 'Sanctions Mission Kakatiya Phase-II'],
                         title='Mission Kakateeya by District')
            st.plotly_chart(fig)    
       
    
            
# Define the home page function
def home():
    st.title('')
    st.markdown("""
        <div style='text-align: center;'>
            <img src='https://th-i.thgim.com/public/news/cities/Hyderabad/xqc285/article68242644.ece/alternates/FREE_1200/Telangana%20State%20emblem.jpg' 
                 width='150'>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h1 style='text-align: center;'>Telangana Open Data Dashboard</h1>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <p style='font-size: 12px;'>
                Telangana, known for its vibrant culture and rapid development, is a state in southern India. 
                Explore the data dashboard to uncover insights into Telangana's key sectors—Agriculture, Health, and Infrastructure.
                Discover valuable information and gain actionable insights for informed decision-making.
            </p>
            <div style="display: flex; justify-content: center;">
                <img src="https://images.moneycontrol.com/static-mcnews/2023/03/Article-3-Image1-770x433.jpg?impolicy=website&width=770&height=431" style="width: 150px; margin-right: 10px;">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRO_9Grw3i0fLlsfzCWkiiVI0RmwOhW3KhfEulsq-2RE4yxRg8mxT1wKuTef-y94K5_C2M&usqp=CAU" style="width: 150px; margin-right: 10px;">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd9UfRxGcFnJZdVMlPqfhFvv29ODHhUSCScw&s" style="width: 150px;">
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; font-size: 12px;'>Welcome to the Visual Space!</h2>", unsafe_allow_html=True)
    st.markdown("""
        ### Overview
        Explore Telangana's diverse sectors—Agriculture, Health, and Infrastructure—with interactive data visualizations.
        Gain valuable insights and make informed decisions with our comprehensive data analysis tools.""")

 
    # Load shapefiles
    districts = gpd.read_file('ShapeFiles/TS_District_Boundary_33/TS_District_Boundary_33_FINAL.shp')
    mandals = gpd.read_file('ShapeFiles/TS_Mandal_Boundary_632/TS_Mandal_Boundary_632_FINAL.shp')
    # Streamlit app
    # st.title("Telangana Districts and Mandals")

    # Create a map centered around Telangana
    telangana_map = folium.Map(location=[18.1124, 79.0193], zoom_start=7)

    # Add districts to the map
    district_layer = folium.GeoJson(
        districts,
        name="Districts",
        style_function=lambda feature: {
            'fillColor': 'transparent',
            'color': 'red',
            'weight': 2
        },
        tooltip=folium.GeoJsonTooltip(fields=['DISTRICT_N'], aliases=['District Name:'])  # Adjust fields as per your dataset
    ).add_to(telangana_map)

    # Add mandals to the map
    mmandal_layer = folium.GeoJson(
        mandals,
        name="Mandals",
        style_function=lambda feature: {
            'fillColor': 'transparent',
            'color': 'green',
            'weight': 1
        },
        tooltip=folium.GeoJsonTooltip(fields=['MANDAL_NAM', 'DISTRICT_N'], aliases=['Mandal Name:', 'District Name:'])
    ).add_to(telangana_map)

    # Add a layer control
    folium.LayerControl().add_to(telangana_map)
    # Display the map in Streamlit
    folium_static(telangana_map)

    st.markdown("""

        ### About Us
        We are a team of 5 passionate individuals dedicated to providing easy access to valuable data with enhanced data visualization and analysis capabilities. Our goal is to empower users with insightful tools to explore and understand Telangana's key sectors.

        Click below to go to official Open Data Portal of Telangana
    """)
    st.link_button("Tealngana Open Data", "https://data.telangana.gov.in/")

def future_implementations():
        st.write("""Here we are using Adilabad weather data to predict wind speed using temperature and humidity as inputs. This can be extended to any other districts data. """)
        st.link_button("Click here for the prediction","https://wind-speed-prediction.streamlit.app/")


# Page configuration
pages = {
    "Home": home,
    "Sectors": sectors,
    "Future Implementations": future_implementations,
    "Team": team
}

def main():
    # Navigation sidebar
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", list(pages.keys()))
    
    # Display the selected page with its contents
    pages[selection]()

if __name__ == "__main__":
    main()
