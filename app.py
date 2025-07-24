# app.py
import streamlit as st
import plotly.express as px
import pandas as pd

# Load the PCA-clustered dataset
df = pd.read_csv("df_pca_clustered_4_train.csv")

# Normalize PC4 for better 3D sizing
df['PC4_scaled_train'] = 10 + 40 * (df['PC4'] - df['PC4'].min()) / (df['PC4'].max() - df['PC4'].min())

# Build interactive plot
fig = px.scatter_3d(
    df,
    x='PC1', y='PC2', z='PC3',
    color='Cluster',
    size='PC4_scaled_train',
    title='Interactive 3D Cluster View (4 clusters)',
    opacity=0.7
)

# Streamlit app layout
st.title("Interactive 3D PCA Clustering View")
st.plotly_chart(fig, use_container_width=True)
