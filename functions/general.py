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


def display_temperatures(filtered_data, days):
    if days == 1:
        st.subheader(f'Temperatures for the next {days} day:')

    else:
        st.subheader(f'Temperatures for the next {days} days:')

    temperatures = [item['values']['temperature'] for item in filtered_data]
    dates = [item['time'] for item in filtered_data]
    figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
    st.plotly_chart(figure, use_container_width=True)


def display_conditions(filtered_data, days):
    if days == 1:
        st.subheader(f'Condition for the next {days} day:')

    else:
        st.subheader(f'Condition for the next {days} days:')


    conditions = [item['values']['weatherCode'] for item in filtered_data]
    images = [f'resources/images/{condition}0.png' for condition in conditions]

    dates = [format_datetime(item['time']) for item in filtered_data]
    st.image(images, caption=dates, width=50)
