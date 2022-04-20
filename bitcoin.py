import requests
import pandas as pd
import streamlit as st
from PIL import Image


st.markdown("<h1 style='text-align: center; color: #008080;'><strong><u>Bitcoin Prices Application</u></strong></h1>", unsafe_allow_html=True)

image = Image.open('bitcoin.jpg')
st.image(image,width=700)
days =  st.slider('Enter the number of days',1,365) 
currency = st.radio("Currency",('CAD' , 'US', 'INR'))
a = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency='+str(currency)+'&days='+str(days)+'&interval=daily').json()         
df = pd.DataFrame(a['prices'])
df[0]= pd.to_datetime(df[0], unit='ms')
df.columns = ['timestamp', currency]
df = df.set_index('timestamp')
st.line_chart(df)

st.write('Average price during this time was ' + str((df[currency].sum())/days)) 
