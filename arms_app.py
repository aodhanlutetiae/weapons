import pandas as pd
import streamlit as st

# text
st.title('UK arms export licences, 2008-23')
st.subheader("How many arms licences has the UK issued for a country?")

# load data and create column for Year
df = pd.read_csv('smaller_arms_file.csv')

# make list of countries, sort alphabetically and use for dropdown
countries = df.destination.unique().tolist()
c_sorted = sorted(countries)
option = st.selectbox("Choose a country to see the number of weapons items approved for export to it, over the period", c_sorted)

# count using year to keep a small df
country1 = df[df.destination == option].groupby('year').destination.count()
st.line_chart(country1)

# print link to the README on the github repo
st.markdown('[About](https://github.com/aodhanlutetiae/arms/blob/main/README.md)')
st.link_button('Source', 'https://github.com/caatdata/uk-arms-export-data',  use_container_width=False)

