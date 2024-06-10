import streamlit as st

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

def water_quality():
    st.title("Water Quality Sector")
    st.write("""
        Details on water quality monitoring, pollution levels, and clean water initiatives.
    """)

def team():
    st.title("Our Team")
    st.subheader("Meet the team behind the dashboard")
    # Add your team member information here
    team_members = ["Likith Gannarapu - Dashboard", "Likki Aashritha - Dashboard"]
    # Display each team member's name
    for member in team_members:
        st.text(member)

# Define the sectors page function
def sectors():
    st.title("Sectors")
    st.subheader("Select a sector to view")
    sectors_list = ["Health", "Agriculture", "Water Quality"]
    sector_selection = st.selectbox("Choose a sector:", sectors_list)
    
    if sector_selection == "Health":
        health()
    elif sector_selection == "Agriculture":
        agriculture()
    elif sector_selection == "Water Quality":
        water_quality()

# Define the home page function
def home():
    st.title("Welcome to the Telangana Open Data Dashboard")
    st.header("About")
    st.write("""
        The Telangana Open Data Dashboard is a platform designed to aggregate and present open data from various sectors in Telangana.
    """)
    st.link_button("Visit Telangana Data Portal", "https://data.telangana.gov.in/")

# Page configuration
pages = {
    "Home": home,
    "Sectors": sectors,
    "Team": team,  # Ensure 'team' function is also defined
}


def main():
    # Navigation sidebar
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    # Display the selected page with its contents
    pages[selection]()

    # Add button in the sidebar
    if selection != "Home":  # Exclude button from the Home page
        if st.sidebar.button("Future Implementations"):
            st.markdown("<script>window.open('https://wind-speed-prediction.streamlit.app/', '_blank');</script>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
