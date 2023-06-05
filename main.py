import streamlit as st
import pandas as pd

# Data
data = {
    'City': ['Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City', 'Taipei City'],
    'District': ['Beitou', 'Daan', 'Songshan', 'Datong', 'Zhongzheng', 'Zhingshan', 'Neihu', 'Shilin', 'Xinyi', 'Wanhua', 'Wenshan', 'Nangang'],
    'Count': [201, 50, 19, 38, 15, 68, 29, 128, 32, 17, 20, 12]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Header
st.header('Volume of Each District in Taipei City')

# Map
st.subheader('Map')
st.map(df)

# Table
st.subheader('Table')
st.table(df)
