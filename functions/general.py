import datetime
import streamlit as st
import plotly.express as px

def format_datetime(date_str):
    date_time = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_time.strftime("%d.%m.\n %H:%M")
    return formatted_date

def filter_data(data, days):
    nr_values = 24 * days
    filtered_data = data[:nr_values]

    return filtered_data
def display_temperatures(filtered_data, days, place):
    if days == 1:
        st.subheader(f'Temperatures for the next {days} day in {place}')
    else:
        st.subheader(f'Temperatures for the next {days} days in {place}')
    temperatures = [dict['values']['temperature'] for dict in filtered_data]
    dates = [dict['time'] for dict in filtered_data]
    figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'},
                     width=800, height=400)
    st.plotly_chart(figure)

def display_conditions(filtered_data, days, place):
    if days == 1:
        st.subheader(f'Condition for the next {days} day in {place}')
    else:
        st.subheader(f'Condition for the next {days} days in {place}')

    conditions = [dict['values']['weatherCode'] for dict in filtered_data]
    images = [f'resources/images/{condition}0.png' for condition in conditions]

    dates = dates = [format_datetime(dict['time']) for dict in filtered_data]
    st.image(images,caption=dates, width=50)
