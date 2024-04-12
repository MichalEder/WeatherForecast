import streamlit as st


from backend import get_data
from functions.general import display_conditions, display_temperatures, filter_data


API_KEYS = [
    st.secrets["api_keys"]["api_keys"]]
print(API_KEYS)


if 'key_index' not in st.session_state:
    st.session_state['key_index'] = 0

if 'reloads_counter' not in st.session_state:
    st.session_state['reloads_counter'] = 0

if 'place' not in st.session_state:
    st.session_state['place'] = None

if 'weather_data' not in st.session_state:
    st.session_state['weather_data'] = None

CURRENT_KEY_INDEX = st.session_state['key_index']

st.set_page_config(layout="wide")

st.title('Weather Forecast for the next days')
st.subheader('Hi and welcome to my little weather forcast app.')

place = st.text_input('Place:')
days = st.slider('Forcast days:',
                 min_value=1,
                 max_value=5,
                 help='Select the number of forcasted days ')


if place == st.session_state['place'] and st.session_state['weather_data']:
    filtered_data = filter_data(st.session_state['weather_data'], days)

elif place:
    data_hourly = get_data(place, API_KEYS[CURRENT_KEY_INDEX])
    if not data_hourly:
        st.subheader('Please enter place of your choice :)')

    elif data_hourly == '400' and st.session_state['place']:
        st.write(f'I am not capable of providing weather information for this place ({place}) :(')
        st.write(f'Please check for typos.')

    elif data_hourly == '429':
        if st.session_state['reloads_counter'] < 5:
            st.write('Try the reload button please.')
            st.button('Reload')
            st.session_state['reloads_counter'] = (st.session_state['reloads_counter'] + 1)

            while data_hourly == '429':
                st.session_state['key_index'] = (st.session_state['key_index'] + 1) % len(API_KEYS)
                data_hourly = get_data(place, API_KEYS[CURRENT_KEY_INDEX])
        else:
            st.write('The connection to data provider dried out, due to too many usage, try it later.')

    else:
        filtered_data = filter_data(data_hourly, days)
        st.session_state['weather_data'] = data_hourly
        st.session_state['place'] = place
else:
    st.subheader('Enter place and days please.')
try:
    col1, col2, col3 = st.columns([4, 0.1, 4])

    with col1:
        display_temperatures(filtered_data, days, place)

    with col3:
        display_conditions(filtered_data, days, place)

except NameError:
    pass
