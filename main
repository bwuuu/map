import streamlit as st
import pandas as pd
import seaborn as sns

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

# Heatmap
st.subheader('Heatmap')
heatmap_fig = sns.heatmap(data=df, x='District', y='Count', annot=True, cmap='YlGnBu', fmt='d')
st.pyplot(heatmap_fig.figure)

# Table
st.subheader('Table')
st.table(df)
