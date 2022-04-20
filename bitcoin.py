import requests
import pandas as pd
import streamlit as st
st.markdown("<h1 style='text-align: center; color: #008080;'><strong><u>Bitcoin Prices Application</u></strong></h1>", unsafe_allow_html=True)
st.image("https://www.reuters.com/resizer/NG2ZJTm2O12wRboyCvuLURRZ1E8=/1200x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/P7RD6UHCKZPGZAOSQQZ2ZICBJQ.jpg",width=700,)
days =  st.slider('Enter the number of days',1,365) 
currency = st.radio("Currency",('CAD' , 'USD', 'INR'))
a = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency='+str(currency)+'&days='+str(days)+'&interval=daily').json()         
df = pd.DataFrame(a['prices'])
df[0]= pd.to_datetime(df[0], unit='ms')
df.columns = ['timestamp', currency]
df = df.set_index('timestamp')
st.line_chart(df)
st.write('Average price during this time was ' + str((df[currency].sum())/days)) 
st.subheader("The application and code is copyright ©  Vinamra Mathur")