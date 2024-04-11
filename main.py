import streamlit as st

st.title('Weather Forecast for the next days')
place = st.text_input('Place:')
days = st.slider('Forcast days:',
                 min_value=1,
                 max_value=5,
                 help='Select the number of forcasted days ')
option = st.selectbox('Select da to view', ('Temeperature', 'Sky'))
if place:
    st.subheader(f'{option} for the next {days} days in {place}')
