import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
fig, ax = plt.subplots()
heatmap = ax.imshow(df['Count'].values.reshape(1, -1), cmap='YlGnBu')
ax.set_xticks(range(len(df['District'])))
ax.set_xticklabels(df['District'], rotation=90)
ax.set_yticks([])
ax.set_xlabel('District')
ax.set_ylabel('Count')
fig.colorbar(heatmap)
st.pyplot(fig)

# Table
st.subheader('Table')
st.table(df)
