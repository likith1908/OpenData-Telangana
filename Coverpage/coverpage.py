import streamlit as st

st.title("Social Computing Project")
# team member names
st.write("### Team :")
st.write("- Likki Aashritha - SE21UCSE262")
st.write("- Likith Gannarapu - SE21UARI076")
st.write("- Sreeja M - SE21UARI077")
st.write("- Harsha Vardhan Reddy Ailuri - SE21UARI043")
st.write("- Aniruddha Srihari Bachmanchi - SE21UARI012")
# course name
st.write("### Course:")
st.write("Social Computing - CS222")

st.write("### Institution:")
st.write("Mahindra University")

# brief description of the project
st.write("### Project Description:")
st.write("""
This project proposes an online dashboard to aggregate and analyze Telangana's open government data. Interactive visualizations and geospatial maps empower citizens, policymakers, and researchers to explore crucial information. The dashboard leverages user feedback and AI/ML for predictive analytics, fostering data-driven decision-making for Telangana's development.
""")

st.link_button("Get Started!!", "https://opendata-telangana1.streamlit.app/")
