"""Adapted from Streamlit’s Create an app tutorial; first 10,000 source records."""
from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st
ROOT=Path(__file__).resolve().parent
@st.cache_data
def load_data():
    data=pd.read_csv(ROOT/'data/uber_10000.csv')
    data.columns=data.columns.str.lower()
    data['date/time']=pd.to_datetime(data['date/time'])
    return data
st.set_page_config(page_title='Uber pickups in NYC',layout='wide')
st.title('Uber pickups in NYC')
st.caption('Streamlit tutorial · First 10,000 rows of the September 2014 source file; this is not a full-month estimate.')
data=load_data()
if st.checkbox('Show raw data',key='show_data'):
    st.dataframe(data)
st.subheader('Number of pickups by hour')
counts=np.histogram(data['date/time'].dt.hour,bins=24,range=(0,24))[0]
st.bar_chart(pd.DataFrame({'Hour':range(24),'Pickups':counts}).set_index('Hour'),y_label='Pickups (records)')
hour=st.slider('Hour of day',0,23,17,key='hour')
selected=data.loc[data['date/time'].dt.hour==hour]
st.subheader(f'Pickup locations at {hour:02d}:00')
st.metric('Pickups in selected hour',len(selected))
if selected.empty:st.info('No pickups in this hour in the bundled sample.')
else:st.map(selected[['lat','lon']])
st.download_button('Download selected pickups',selected.to_csv(index=False),'pickups.csv','text/csv')
st.caption('Locations are pickup coordinates, not inferred home addresses. Map tiles need internet; the records and charts are bundled.')
st.markdown('[Tutorial and source](https://docs.streamlit.io/get-started/tutorials/create-an-app) · [Original data](https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz)')
