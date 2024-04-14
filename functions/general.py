import datetime
import streamlit as st
import plotly.express as px


def format_date_time(date_str):
    date_time = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    formatted_date = date_time.strftime('%d.%m.')
    formatted_time =  date_time.strftime('%H:%M')
    return formatted_date, formatted_time


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

    dates = [format_date_time(item['time']) for item in filtered_data]
    dates_headers = sorted({date[0] for date in dates})

    for date in dates_headers:
        st.subheader(date)
        data_for_date = [item for item in filtered_data if
                      format_date_time(item['time'])[0] == date]

        conditions = [item['values']['weatherCode'] for item in data_for_date]
        images = [f'resources/images/{condition}0.png' for condition in conditions]
        hours = [format_date_time(item['time'])[1] for item in data_for_date]
        st.image(images, caption=hours, width=50)
